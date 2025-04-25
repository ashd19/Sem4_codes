import java.net.*;

public class serverudp {
    public static void main(String[] args) throws Exception {
        // Create a DatagramSocket bound to port 9876 to listen for incoming UDP packets.
        DatagramSocket serverSocket = new DatagramSocket(9876);
        System.out.println("UDP Server is running on port 9876");

        // Buffer to store incoming data from the client.
        byte[] receiveBuffer = new byte[1024];
        byte[] sendBuffer;

        // Create a DatagramPacket to receive data from the client.
        DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);

        // Wait for a single client request.
        System.out.println("Waiting for client data...");
        serverSocket.receive(receivePacket);

        // Extract the data from the received packet and convert it to a string.
        String clientData = new String(receivePacket.getData(), 0, receivePacket.getLength());
        System.out.println("Received from client: " + clientData);

        // Split the received data to extract two numbers.
        String[] numbers = clientData.split(" ");
        int num1 = Integer.parseInt(numbers[0]); // Parse the first number.
        int num2 = Integer.parseInt(numbers[1]); // Parse the second number.

        // Calculate the sum of the two numbers.
        int sum = num1 + num2;
        String responseData = "Sum: " + sum;

        // Convert the response data to bytes for sending back to the client.
        sendBuffer = responseData.getBytes();

        // Retrieve the client's address and port from the received packet.
        InetAddress clientAddress = receivePacket.getAddress();
        int clientPort = receivePacket.getPort();

        // Create a DatagramPacket to send the response back to the client.
        DatagramPacket sendPacket = new DatagramPacket(sendBuffer, sendBuffer.length, clientAddress, clientPort);

        // Send the response packet to the client.
        serverSocket.send(sendPacket);
        System.out.println("Response sent to client: " + responseData);

        // Close the server socket after handling the single request.
        serverSocket.close();
        System.out.println("Server has shut down.");
    }
}
