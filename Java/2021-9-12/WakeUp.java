import java.net.InetSocketAddress;
import java.nio.channels.SelectionKey;
import java.nio.channels.Selector;
import java.nio.channels.ServerSocketChannel;

public class WakeUp {

    public static void main(String[] args) throws Exception {

        ServerSocketChannel serverSocketChannel;

        Selector selector = Selector.open();
        serverSocketChannel = ServerSocketChannel.open();

        serverSocketChannel.socket().bind(new InetSocketAddress("127.0.0.1", 8080), 64);
        serverSocketChannel.configureBlocking(false);
        serverSocketChannel.register(selector, SelectionKey.OP_ACCEPT);

        new Thread() {
            @Override
            public void run() {
                try {
                    System.out.print("Thread[" + Thread.currentThread().getName() + "]invoke select\r\n");
                    int readyChannels = selector.select();
                } catch (Exception x) {
                    x.printStackTrace();
                }
                System.out.print("Success...\r\n");
            }
        }.start();

        Thread.sleep(5_60_000);
        System.out.print("Thread[" + Thread.currentThread().getName() + "]invoke wakeup\r\n");

        selector.wakeup();

    }
}
