
import java.io.IOException;
import java.net.Socket;

public class RedisExample {

    private static final String host = "127.0.0.1";
    private static final int port = 6379;
    private static final String CRLF = "\r\n";

    public static void main(String[] args) throws IOException {

        connnectRedis("k2", "v2");

    }

    public static void connnectRedis(String key, String value) throws IOException {

        // 建立连接
        Socket client = new Socket(host, port);

        StringBuilder command = new StringBuilder();

        // *<参数个数> CRLF
        String number = "*3" + CRLF;
        command.append(number);
        
        // $<参数字节数>CRLF<参数>CRLF
        String cmd = "$3" + CRLF + "SET" + CRLF;
        command.append(cmd);
        
        // $<参数字节数>CRLF<参数>CRLF
        cmd = "$" + key.getBytes().length + CRLF + key + CRLF;
        command.append(cmd);

        // $<参数字节数>CRLF<参数>CRLF
        cmd = "$" + value.getBytes().length + CRLF + value + CRLF;
        command.append(cmd);

        // 向服务器发送命令
        client.getOutputStream().write(command.toString().getBytes());

        // 接收服务器响应
        byte[] response = new byte[1024];
        client.getInputStream().read(response);
        System.out.println(new String(response, 0, response.length));

    }
}
