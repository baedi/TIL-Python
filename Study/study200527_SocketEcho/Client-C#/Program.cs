using static System.Console;
using System.Net;
using System.Net.Sockets;

namespace EchoClient_ {

    /** Main Class **/
    class Program {

        /** Variable **/
        static SockClient client;
        static string serverIP;

        /** Main **/
        static void Main(string[] args) {

            // Input server IP, Port        
            Write("Input server IP : "); serverIP = ReadLine();

            // Connection ready...          
            client = new SockClient(serverIP, 50000);
            client.Connect();

            // Input message                
            Write("Client : ");
            client.SendMessage(ReadLine() + "\n");

            client.SocketClose();
        }

    }
}
