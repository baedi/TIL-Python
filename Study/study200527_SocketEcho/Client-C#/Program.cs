using static System.Console;
using System.Net;
using System.Net.Sockets;

namespace EchoClient_ {

    /** Main Class **/
    class Program {

        /** Variable **/
        static SockClient client;
        static string serverIP;
        static string message;

        /** Main **/
        static void Main(string[] args) {

            // Input server IP, Port        
            Write("Input server IP : "); serverIP = ReadLine();

            // Connection ready...          
            client = new SockClient(serverIP, 50000);
            client.Connect();

            // Input message                
            do {
                Write("> "); message = ReadLine();
                client.SendMessage(message + "\n");
            } while (!message.Equals(" "));

            client.SocketClose();
        }

    }
}
