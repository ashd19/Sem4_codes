import java.io.*;
import java.net.*;
import java.util.Scanner;

class clienttcp{
    public static void main(String args[]) throws IOException {
        Scanner sc = new Scanner(System.in);
        Socket socket = new Socket("localhost", 5173);

        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

        // Setup input stream to receive data from the server
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

        System.out.print("Enter Two Numbers: ");
        int a = sc.nextInt();
        int b = sc.nextInt();

        // Send message to the server
        out.println(Integer.toString(a));
        out.println(Integer.toString(b));

        // Receive response from the server
        String response = in.readLine();
        System.out.println("Server says: " + response);
sc.close();
        socket.close();
        
    }
}
