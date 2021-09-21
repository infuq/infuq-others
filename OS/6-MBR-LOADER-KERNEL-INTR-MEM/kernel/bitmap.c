#include "bitmap.h" 
#include "stdint.h" 
#include "string.h" 
#include "print.h" 
#include "interrupt.h" 


// 位图初始化,把每一位都设置为0
void bitmap_init(struct bitmap *btmp)
{
    memset(btmp->bits, 0, btmp->btmp_bytes_len);
}


// 判断bit_idx位是否为1,若为1,则返回true
bool bitmap_scan_test(struct bitmap *btmp, uint32_t bit_idx)
{
    uint32_t byte_idx = bit_idx / 8;
    uint32_t bit_odd = bit_idx % 8;
    return (btmp->bits[byte_idx] & (1 << bit_odd));
}


// 在位图中申请连续cnt个位,成功则返回起始位下标,失败返回-1
int bitmap_scan(struct bitmap *btmp, uint32_t cnt)
{
    uint32_t idx_byte = 0;
    
    // 逐个字节比较
    while ((0xff == btmp->bits[idx_byte]) && (idx_byte < btmp->btmp_bytes_len))
    {
        idx_byte++;
    }

    // 未找到空闲位,返回-1
    if (idx_byte == btmp->btmp_bytes_len)
    {
        return -1;
    }

    // 某字节中找到了空闲位
    int idx_bit = 0;
    while ((uint8_t)(1 << idx_bit) & btmp->bits[idx_byte])
    {
        idx_bit++;
    }

    int bit_idx_start = idx_byte * 8 + idx_bit;
    // 只需要1位直接返回
    if (cnt == 1)
    {
        return bit_idx_start;
    }

    // if cnt >1,还得继续判断
    uint32_t bit_left = (btmp->btmp_bytes_len * 8 - bit_idx_start);
    uint32_t next_bit = bit_idx_start + 1;
    uint32_t count = 1; // 已找到的空闲位

    bit_idx_start = -1;
    while (bit_left-- > 0)
    {
        if (!(bitmap_scan_test(btmp, next_bit)))
        {
            count++;
        }
        else
        {
            count = 0;
        }

        // 找到连续的cnt个空位
        if (count == cnt)
        {
            bit_idx_start = next_bit - cnt + 1;
            break;
        }

        next_bit++;
    }
    
    return bit_idx_start;
}


// 将位图btmp的bit_idx位设置为value
void bitmap_set(struct bitmap *btmp, uint32_t bit_idx, int8_t value) {
    uint32_t byte_idx = bit_idx / 8;
    uint32_t bit_odd = bit_idx % 8;
    
    if (value)
    {
        // value为1
        btmp->bits[byte_idx] |= (1 << bit_odd);
    }
    else
    {
        btmp->bits[byte_idx] &= ~(1 << bit_odd);
    }
}

