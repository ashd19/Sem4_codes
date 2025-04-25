import java.net.*;
import java.io.*;


class servertcp{
    public static void main(String args[]) throws IOException {
        ServerSocket serverSocket = new ServerSocket(5173);
        System.out.println("Server is Running on port 5173");

        Socket clientSocket = serverSocket.accept();
        System.out.println("Client Connected");

        // Setup input and output streams for communication with the client
        BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);

        // Read message from client
        int a = Integer.parseInt(in.readLine());
        int b = Integer.parseInt(in.readLine());

        int sum = a + b;
        System.out.println("Client says: " + a + " + " + b);

        // Send response to the client
        out.println("Sum of " + a + " and " + b + " is " + sum);

        // Close the client and server sockets
        clientSocket.close();
        serverSocket.close();
    }
}
