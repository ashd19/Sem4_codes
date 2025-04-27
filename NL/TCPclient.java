import java.io.*;
import java.net.*;
import java.util.Scanner;

public class TCPclient {
    public static void main(String[] args) throws Exception {
        Socket socket = new Socket("localhost", 5000);

        DataInputStream dis = new DataInputStream(socket.getInputStream());
        DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
        Scanner sc = new Scanner(System.in);

        String serverMessage = dis.readUTF();
        System.out.println(serverMessage);
        dos.writeUTF("Client Ready");

        System.out.print("Enter first number: ");
        int num1 = sc.nextInt();
        System.out.print("Enter second number: ");
        int num2 = sc.nextInt();

        dos.writeInt(num1);
        dos.writeInt(num2);

        int product = dis.readInt();
        System.out.println("Product is: " + product);

        socket.close();
        sc.close();
    }
}
