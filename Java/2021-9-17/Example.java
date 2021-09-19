import java.lang.Thread;

public class Example {


    public static void main(String[] args) throws Exception {
        
        
        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
//                    Thread.sleep(1000000000);
                } catch (Exception x) {}     
                System.out.println("I'm Thread-1");
            
            }
        }, "Thread-1").start();
    
    
        System.out.println("I'm main");
    
    }

}
