import java.net.*;
import java.util.Scanner;

public class UDPClient {
    public static void main(String[] args) throws Exception {
        DatagramSocket clientSocket = new DatagramSocket();
        InetAddress IPAddress = InetAddress.getByName("localhost");
        byte[] sendData = new byte[1024];
        byte[] receiveData = new byte[1024];
        Scanner sc = new Scanner(System.in);

        String greeting = "Client Ready";
        sendData = greeting.getBytes();
        DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, 5000);
        clientSocket.send(sendPacket);

        System.out.print("Enter first number: ");
        int num1 = sc.nextInt();
        System.out.print("Enter second number: ");
        int num2 = sc.nextInt();
        String numbers = num1 + " " + num2;
        sendData = numbers.getBytes();
        sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, 5000);
        clientSocket.send(sendPacket);

        DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
        clientSocket.receive(receivePacket);
        String result = new String(receivePacket.getData(), 0, receivePacket.getLength());
        System.out.println("Product received from server: " + result);

        clientSocket.close();
    }
}
