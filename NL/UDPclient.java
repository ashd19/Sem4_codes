import java.net.*;
import java.io.*;

public class UDPclient {
    public static void main(String[] args) {
        DatagramSocket socket = null;
        try {
            socket = new DatagramSocket();
            InetAddress serverAddress = InetAddress.getByName("localhost");
            byte[] buffer;
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            
            System.out.print("Enter a number: ");
            String input = reader.readLine();
            buffer = input.getBytes();
            DatagramPacket packet = new DatagramPacket(buffer, buffer.length, serverAddress, 9876);
            socket.send(packet);
            
            buffer = new byte[1024];
            packet = new DatagramPacket(buffer, buffer.length);
            socket.receive(packet);
            String result = new String(packet.getData(), 0, packet.getLength());
            System.out.println("Result from server: " + result);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (socket != null && !socket.isClosed()) {
                socket.close();
            }
        }
    }
}
