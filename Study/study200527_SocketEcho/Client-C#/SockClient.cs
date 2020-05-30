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
        private byte[] receiveBuffer = new byte[1024];
        private byte[] sendBuffer;
        private StringBuilder strBuilder = new StringBuilder();


        /** Initialization **/
        public SockClient(string ip, int port) {
            serverIP = ip;
            serverPort = port;

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

            clientSocket.BeginReceive(receiveBuffer, 0, receiveBuffer.Length, SocketFlags.None, ReceiveMessage, this);
        }


        /** Send Message **/
        public void SendMessage(string message) {
            sendBuffer = Encoding.UTF8.GetBytes(message);
            clientSocket.Send(System.BitConverter.GetBytes(sendBuffer.Length));
            clientSocket.Send(sendBuffer);
        }


        /** Receive Message **/
        public void ReceiveMessage(System.IAsyncResult result) {
            int size = clientSocket.EndReceive(result);
            strBuilder.Append(Encoding.UTF8.GetString(receiveBuffer, 0, size));

            WriteLine(strBuilder.ToString());
            strBuilder.Clear();

            clientSocket.BeginReceive(receiveBuffer, 0, receiveBuffer.Length, SocketFlags.None, ReceiveMessage, this);

        }


        /** Disconnect. **/
        public void SocketClose() {
            clientSocket.Close();
        }
    }
}
