public class Test {

    static {
        System.loadLibrary("jninativememory");
    }

    public static void main(String[] args) throws Exception {
        JNINativeMemory caller = new JNINativeMemory();
        caller.allocateMemory();
        Thread.sleep(3600 * 1000);
    }

}
