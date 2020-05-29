using static System.Console;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace EchoClient_ {

    /** Client Class **/
    class SockClient {

        /** Member Variable **/
        private Socket clientSocket;
        private string serverIP;
        private int serverPort;
        private byte[] buffer;
        private Thread thread;


        /** Initialization **/
        public SockClient(string ip, int port) {
            serverIP = ip;
            serverPort = port;
            thread = new Thread(new ThreadStart(ReceiveMessage));

            WriteLine("SockClient initialization!");
        }


        /** Server Connect **/
        public void Connect() {

            // Socket mode :: TCP       
            clientSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);

            // Connect                  
            WriteLine("Connect...");
            IPEndPoint endPoint = new IPEndPoint(IPAddress.Parse(serverIP), serverPort);
            clientSocket.Connect(endPoint);
        }


        /** Send Message **/
        public void SendMessage(string message) {
            buffer = Encoding.UTF8.GetBytes(message);
            clientSocket.Send(System.BitConverter.GetBytes(buffer.Length));
            clientSocket.Send(buffer);
        }


        /** Receive Message **/
        public void ReceiveMessage() {
            while (true) {
                int ea = clientSocket.Receive(buffer);
                WriteLine("Server : " + Encoding.UTF8.GetString(buffer, 0, ea));
            }
        }


        /** Disconnect. **/
        public void SocketClose() {
            clientSocket.Close();
        }
    }
}
