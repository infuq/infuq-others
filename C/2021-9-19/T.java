import java.lang.Thread;

public class T {

    public static void main(String[] args) throws Exception {
    
    
        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    Thread.sleep(20000);
                } catch(Exception x) {}
                System.out.println("Thread-A");
            }
        }, "Thread-A").start();    
    
        Thread.sleep(30000);
        



        System.out.println("main");
    
       // System.exit(0);
       return;
    }

}
