#include "interrupt.h"
#include "print.h"
#include "stdint.h"
#include "global.h"
#include "io.h"

#define PIC_M_CTRL 0x20 //主片[控制]端口
#define PIC_M_DATA 0x21 //主片[数据]端口
#define PIC_S_CTRL 0xa0 //从片[控制]端口
#define PIC_S_DATA 0xa1 //从片[数据]端口

#define IDT_DESC_CNT 0x81    //目前总共支持的中断数(129个)

#define EFLAGS_IF   0x00000200       // eflags寄存器中的IF位为1
#define GET_EFLAGS(EFLAG_VAR) asm volatile("pushfl; popl %0" : "=g" (EFLAG_VAR))



// 中断门描述符结构体(8个字节). 此结构与中断门描述符格式一一对应
struct gate_desc
{
    uint16_t func_offset_low_word;
    uint16_t selector; // 选择子
    uint8_t  dcount;
    uint8_t  attribute;
    uint16_t func_offset_high_word;
};

// 静态函数声明,非必须
static void make_idt_desc(struct gate_desc *p_gdesc, uint8_t attr, intr_handler function);
// 中断门描述符表的数组
static struct gate_desc idt[IDT_DESC_CNT];
// 用于保存异常名
char *intr_name[IDT_DESC_CNT];
// 定义中断处理程序数组,在kernel.asm中定义的intrXXentry只是中断处理程序的入口,最终调用idt_table中的处理程序
intr_handler idt_table[IDT_DESC_CNT];
// 声明引用定义在kernel.asm中的中断处理函数入口数组
extern intr_handler intr_entry_table[IDT_DESC_CNT];

extern uint32_t syscall_handler();




// 初始化可编程中断控制器 8259A
static void pic_init()
{
    /*初始化主片 */
    outb (PIC_M_CTRL, 0x11); // ICW1: 边沿触发,级联8259, 需要ICW4
    outb (PIC_M_DATA, 0x20); // ICW2: 起始中断向量号为0x20, 也就是IR[0-7] 为 0x20 ～ 0x27
    outb (PIC_M_DATA, 0x04); // ICW3: IR2 接从片
    outb (PIC_M_DATA, 0x01); // ICW4: 8086 模式, 正常EOI

    /*初始化从片 */
    outb (PIC_S_CTRL, 0x11); // ICW1: 边沿触发,级联8259, 需要ICW4
    outb (PIC_S_DATA, 0x28); // ICW2: 起始中断向量号为0x28, 也就是IR[8-15]为0x28 ～ 0x2F
    outb (PIC_S_DATA, 0x02); // ICW3: 设置从片连接到主片的IR2 引脚
    outb (PIC_S_DATA, 0x01); // ICW4: 8086 模式, 正常EOI



    /* 接受时钟中断 */ // 键盘中断未打开
    outb (PIC_M_DATA, 0xfe);
    outb (PIC_S_DATA, 0xff);


    put_str("      pic_init done\n");
}

//创建中断门描述符
static void make_idt_desc(struct gate_desc *p_gdesc, uint8_t attr, intr_handler function)
{
    p_gdesc->func_offset_low_word = (uint32_t)function & 0x0000FFFF;
    p_gdesc->selector = SELECTOR_K_CODE;
    p_gdesc->dcount = 0;
    p_gdesc->attribute = attr;
    p_gdesc->func_offset_high_word = ((uint32_t)function & 0xFFFF0000) >> 16;
}

// 初始化中断(门)描述符表
static void idt_desc_init()
{
    int i;
    int lastindex = IDT_DESC_CNT - 1;
    for (i = 0; i < IDT_DESC_CNT; i++)
    {
        // intr_entry_table数组在kernel.asm中已经初始化完成
        make_idt_desc(&idt[i], IDT_DESC_ATTR_DPL0, intr_entry_table[i]);
    }

    // 单独处理系统调用
    make_idt_desc(&idt[lastindex], IDT_DESC_ATTR_DPL3, syscall_handler);

    put_str("      idt_desc_init done\n");
}



// 通用的中断处理函数,一般用在异常出现时的处理
static void general_intr_handler(uint8_t vec_nr)
{

    if(vec_nr == 0x27 || vec_nr == 0x2f)
    {
        return;
    }


    set_cursor(0);
    int cursor_pos = 0;
    while (cursor_pos < 320)
    {
        put_char(' ');
        cursor_pos++;
    }

    set_cursor(0);
    put_str("--- exception message begin ---\n");
    set_cursor(88);
    put_str(intr_name[vec_nr]);
    if (vec_nr == 14) // PageFault
    {
        int page_fault_vaddr = 0;
        asm ("movl %%cr2, %0" : "=r" (page_fault_vaddr));
        put_str("\npage fault addr = 0x");
        put_int(page_fault_vaddr);
    }
    put_str("\n--- exception message end ---\n");
    while(1);
  
}


// 完成一般中断处理函数注册及异常名称注册
static void exception_init()
{
    int i;
    for (i = 0; i < IDT_DESC_CNT; i++)
    {
        // 默认为这个,以后会由 register_handler 来注册具体处理函数
        idt_table[i] = general_intr_handler;
        intr_name[i] = "unknown";
    }
    intr_name[0] = "#DE Divide Error"; 
    intr_name[1] = "#DB Debug Exception"; 
    intr_name[2] = "NMI Interrupt"; 
    intr_name[3] = "#BP Breakpoint Exception"; 
    intr_name[4] = "#OF Overflow Exception"; 
    intr_name[5] = "#BR BOUND Range Exceeded Exception"; 
    intr_name[6] = "#UD Invalid Opcode Exception"; 
    intr_name[7] = "#NM Device Not Available Exception"; 
    intr_name[8] = "#DF Double Fault Exception"; 
    intr_name[9] = "Coprocessor Segment Overrun"; 
    intr_name[10] = "#TS Invalid TSS Exception"; 
    intr_name[11] = "#NP Segment Not Present"; 
    intr_name[12] = "#SS Stack Fault Exception"; 
    intr_name[13] = "#GP General Protection Exception"; 
    intr_name[14] = "#PF Page-Fault Exception"; 
    // intr_name[15] 第 15 项是 intel 保留项,未使用
    intr_name[16] = "#MF x87 FPU Floating-Point Error"; 
    intr_name[17] = "#AC Alignment Check Exception"; 
    intr_name[18] = "#MC Machine-Check Exception"; 
    intr_name[19] = "#XF SIMD Floating-Point Exception";
}


/* 开中断,并返回开中断前的状态*/
enum intr_status intr_enable()
{
    
    if (INTR_ON == intr_get_status())
    {
        return INTR_ON;
    }
    else
    {
        asm volatile("sti");     // 开中断,sti指令将IF位置1
        return INTR_OFF;
    }

}


/* 关中断,并返回关中断前的状态 */
enum intr_status intr_disable()
{

    if (INTR_ON == intr_get_status())
    {
        asm volatile("cli" : : : "memory"); // 关中断,cli指令将IF位置0
        return INTR_ON;
    }
    else
    {
        return INTR_OFF;
    }


}


/* 将中断状态设置为status */
enum intr_status intr_set_status(enum intr_status status)
{
    return status & INTR_ON ? intr_enable() : intr_disable();
}

/* 获取当前中断状态 */
enum intr_status intr_get_status()
{
    uint32_t eflags = 0; 
    GET_EFLAGS(eflags);
    return (EFLAGS_IF & eflags) ? INTR_ON : INTR_OFF;
}


// 完成有关中断到所有初始化工作
void idt_init()
{
    
    put_str("   idt_init start\n");

    idt_desc_init();      // 初始化中断描述符表. 即初始化idt数组
    exception_init();     // 初始化通用中断处理函数. 即初始化idt_table数组
    pic_init();           // 初始化8259A

    // 加载idt
	uint64_t idt_operand = ((sizeof(idt) - 1) | ((uint64_t)(uint32_t)idt << 16));
    asm volatile("lidt %0" : : "m" (idt_operand));

    put_str("   idt_init done\n");

}



 
// 注册中断处理函数
void register_handler(uint8_t vector_no, intr_handler function)
{
    idt_table[vector_no] = function;
}

