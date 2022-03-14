
import org.jctools.util.UnsafeAccess;
import sun.misc.Unsafe;

public class Test {

    static {
        System.loadLibrary("jninativememory");
    }

    public static void main(String[] args) throws Exception {
        JNINativeMemory caller = new JNINativeMemory();
        caller.allocateMemory();

        Unsafe unsafe = UnsafeAccess.UNSAFE;
        // 32MB
        long addr = unsafe.allocateMemory(32 * 1024 * 1024);
        System.out.println("Java 申请:\t 0x" + Long.toHexString(addr));


        Thread.sleep(3600 * 1000);
    }

}
