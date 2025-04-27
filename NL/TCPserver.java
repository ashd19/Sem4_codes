import java.io.*;
import java.net.*;

public class TCPserver {
    public static void main(String[] args) throws Exception {
        ServerSocket serverSocket = new ServerSocket(5000);
        System.out.println("Server Started. Waiting for client...");
        Socket socket = serverSocket.accept();
        System.out.println("Client Connected.");

        DataInputStream dis = new DataInputStream(socket.getInputStream());
        DataOutputStream dos = new DataOutputStream(socket.getOutputStream());

        dos.writeUTF("Server Connected");
        String clientMessage = dis.readUTF();
        System.out.println(clientMessage);

        int num1 = dis.readInt();
        int num2 = dis.readInt();
        System.out.println("Received numbers: " + num1 + " and " + num2);

        int product = num1 * num2;
        dos.writeInt(product);
        System.out.println("Product sent to client: " + product);

        socket.close();
        serverSocket.close();
    }
}
