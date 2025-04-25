import java.net.*; // Provides classes for networking, such as ServerSocket and Socket.
import java.io.*;  // Provides classes for input and output, such as BufferedReader and PrintWriter.

class servertcp {
    public static void main(String args[]) throws IOException {
        // Creates a server socket bound to port 5173. This socket listens for incoming client connections.
        ServerSocket serverSocket = new ServerSocket(5173);
        System.out.println("Server is Running on port 5173");

        // Waits for a client to connect. This method blocks until a connection is established.
        Socket clientSocket = serverSocket.accept();
        System.out.println("Client Connected");

        // Sets up a BufferedReader to read text data sent by the client through the input stream of the socket.
        BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

        // Sets up a PrintWriter to send text data to the client through the output stream of the socket.
        // The second argument `true` enables auto-flushing, buffered data is sent imm,meaning data is sent immediately without needing to call `flush()`.
        PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);

        // Reads a line of text from the client, converts it to an integer, and stores it in variable `a`.
        int a = Integer.parseInt(in.readLine());

        // Reads another line of text from the client, converts it to an integer, and stores it in variable `b`.
        int b = Integer.parseInt(in.readLine());

        // Calculates the sum of the two integers received from the client.
        int sum = a + b;

        // Prints the received numbers and their sum to the server console.
        System.out.println("Client says: " + a + " + " + b);

        // Sends the result of the sum back to the client as a response.
        out.println("Sum of " + a + " and " + b + " is " + sum);

        // Closes the client socket, ending the connection with the client.
        clientSocket.close();

        // Closes the server socket, stopping the server from accepting further connections.
        serverSocket.close();
    }
}
