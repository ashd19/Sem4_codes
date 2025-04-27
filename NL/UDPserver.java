import java.net.*;
import java.io.*;

public class UDPServer {
    public static void main(String[] args) {
        DatagramSocket socket = null;
        try {
            socket = new DatagramSocket(9876);
            byte[] buffer = new byte[1024];
            
            while (true) {
                DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
                socket.receive(packet);
                String input = new String(packet.getData(), 0, packet.getLength());
                
                int number = Integer.parseInt(input);
                int result = number * number;
                
                String response = "The square of " + number + " is " + result;
                packet = new DatagramPacket(response.getBytes(), response.length(), packet.getAddress(), packet.getPort());
                socket.send(packet);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (socket != null && !socket.isClosed()) {
                socket.close();
            }
        }
    }
}
