
import sun.misc.Unsafe;
import java.lang.reflect.Field;

public class ObjectAddress {

    private String address = "Jiangsu";


    private static final Unsafe UNSAFE;
    static {
        Unsafe instance = null;
        try {
            final Field field = Unsafe.class.getDeclaredField("theUnsafe");
            field.setAccessible(true);
            instance = (Unsafe) field.get(null);
        } catch (Exception ignored) {

        }
        UNSAFE = instance;
    }

    static long getBaseAddress(Object obj){
        Object[] array = new Object[]{ obj };
        long baseOffset = UNSAFE.arrayBaseOffset(Object[].class);
        return UNSAFE.getLong(array, baseOffset);
    }


    public static void main(String[] args) throws Exception {

        for (int i = 0; i < 1000; i++) {
            new ObjectAddress();
        }


        ObjectAddress obj = new ObjectAddress();
        // 堆空间地址
        System.out.println( "0x" + Long.toHexString(getBaseAddress(obj)) );


        // 直接内存地址
        long direct = UNSAFE.allocateMemory(1024);
        System.out.println( "0x" + Long.toHexString(direct) );

        // #1 获取属性在类中的偏移地址
        long valueOffset = UNSAFE.objectFieldOffset(ObjectAddress.class.getDeclaredField("address"));
        // #2
        UNSAFE.putObject(obj, valueOffset, "hagnzhou");




        System.out.println(obj.address);


        System.out.println("MainThread...");
        Thread.sleep(50000);



    }



}
