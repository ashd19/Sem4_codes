import java.io.*; // Provides classes for input and output, such as BufferedReader and PrintWriter.
import java.net.*; // Provides classes for networking, such as Socket.
import java.util.Scanner; // Provides the Scanner class for reading user input.

class clienttcp {
    public static void main(String args[]) throws IOException {
        // Creates a Scanner object to read input from the user.
        Scanner sc = new Scanner(System.in);

        // Creates a socket to connect to the server running on localhost (127.0.0.1) at port 5173.
        Socket socket = new Socket("localhost", 5173);

        // Sets up a PrintWriter to send text data to the server through the output stream of the socket.
        // The second argument `true` enables auto-flushing, meaning data is sent immediately without needing to call `flush()`.
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

        // Sets up a BufferedReader to receive text data from the server through the input stream of the socket.
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

        // Prompts the user to enter two numbers.
        System.out.print("Enter Two Numbers: ");
        int a = sc.nextInt(); // Reads the first integer from the user.
        int b = sc.nextInt(); // Reads the second integer from the user.

        // Sends the two numbers to the server as strings.
        out.println(Integer.toString(a)); // Sends the first number.
        out.println(Integer.toString(b)); // Sends the second number.

        // Receives the response from the server.
        String response = in.readLine(); // Reads a line of text sent by the server.
        System.out.println("Server says: " + response); // Prints the server's response.

        // Closes the Scanner object to release resources.
        sc.close();

        // Closes the socket, ending the connection with the server.
        socket.close();
    }
}