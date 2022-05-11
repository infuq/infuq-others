
import org.openjdk.jol.info.ClassLayout;

public class Example {
    
    public static void main(String[] args) {

//        Integer arr[] = new Integer[4];
        int[] arr = new int[7];
        System.out.println(ClassLayout.parseInstance(arr).toPrintable());

//        Object obj = new Object();
//        System.out.println(ClassLayout.parseInstance(obj).toPrintable());

    }



}
