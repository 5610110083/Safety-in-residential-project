using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using CSockets;
using System.Net;

namespace Server
{
    public partial class Form1 : Form
    {
        delegate void SetTextCallback(string text);
        CServerSocket server;
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int port;
            if (int.TryParse(textBox2.Text,out port))
            {
                server = new CServerSocket(port);
                server.OnConnect += new CServerSocket.ConnectionDelegate(server_OnConnect);
                server.OnListen += new CServerSocket.ListenDelegate(server_OnListen);
                server.OnRead += new CServerSocket.ConnectionDelegate(server_OnRead);
                server.OnDisconnect += new CServerSocket.ConnectionDelegate(server_OnDisconnect);
                server.Active();
            }
        }

        void server_OnDisconnect(System.Net.Sockets.Socket soc)
        {
            string indice = server.IndexOf(soc).ToString();
            RemoveLast(indice);
        }
        private void RemoveLast(string text)
        {
            if (this.comboBox1.InvokeRequired)
            {
                SetTextCallback d = new SetTextCallback(RemoveLast);
                this.Invoke(d, new object[] { text });
            }
            else
            {
                this.comboBox1.Items.RemoveAt(comboBox1.Items.Count - 1);
            }
        }

        void server_OnRead(System.Net.Sockets.Socket soc)
        {
            textBox4.Text += server.ReceivedText + "\n\r";
        }

        void server_OnListen()
        {
            MessageBox.Show("Start wait");
            
        }

        void server_OnConnect(System.Net.Sockets.Socket soc)
        {
            comboBox1.Items.Add(server.IndexOf(soc));
        }

        private void button1_Click(object sender, EventArgs e)
        {
            server.SendText(textBox3.Text, comboBox1.SelectedIndex);

        }

        private void button3_Click(object sender, EventArgs e)
        {
            server.CloseConnection(comboBox1.SelectedIndex);
        }
    }
}