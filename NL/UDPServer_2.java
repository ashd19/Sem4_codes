import java.net.*;

public class UDPServer {
    public static void main(String[] args) throws Exception {
        DatagramSocket serverSocket = new DatagramSocket(5000);
        byte[] receiveData = new byte[1024];
        byte[] sendData = new byte[1024];

        DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
        serverSocket.receive(receivePacket);

        String clientMessage = new String(receivePacket.getData(), 0, receivePacket.getLength());
        System.out.println(clientMessage);

        receivePacket = new DatagramPacket(receiveData, receiveData.length);
        serverSocket.receive(receivePacket);
        String numbers = new String(receivePacket.getData(), 0, receivePacket.getLength());
        String[] parts = numbers.split(" ");
        int num1 = Integer.parseInt(parts[0]);
        int num2 = Integer.parseInt(parts[1]);
        System.out.println("Received numbers: " + num1 + " and " + num2);

        int product = num1 * num2;
        InetAddress IPAddress = receivePacket.getAddress();
        int port = receivePacket.getPort();
        sendData = String.valueOf(product).getBytes();
        DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, port);
        serverSocket.send(sendPacket);

        serverSocket.close();
    }
}
