using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using CSockets;
namespace Client
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        CClientSocket client;
        private void BT_Connect_A_Click(object sender, EventArgs e)
        {
            client = new CClientSocket(txt_ip.Text, int.Parse(txt_port.Text));
            client.OnConnect += new CClientSocket.ConnectionDelegate(client_OnConnect);
            client.OnRead += new CClientSocket.ConnectionDelegate(client_OnRead);
            client.OnDisconnect += new CClientSocket.ConnectionDelegate(client_OnDisconnect);
            client.Connect();
        }

        void client_OnDisconnect(System.Net.Sockets.Socket soc)
        {
            txt_client.Text += "\nDisconnect";
        }

        void client_OnRead(System.Net.Sockets.Socket soc)
        {
            txt_client.Text += client.ReceivedText+"\n";
        }

        void client_OnConnect(System.Net.Sockets.Socket soc)
        {
            MessageBox.Show("Connected");
        }

        private void BT_SendText_A_Click(object sender, EventArgs e)
        {
            client.SendText(LE_SendText_A.Text);
        }
    }
}