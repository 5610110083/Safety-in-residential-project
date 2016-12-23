namespace Client
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.GB_CS_A = new System.Windows.Forms.GroupBox();
            this.LE_SendText_A = new System.Windows.Forms.TextBox();
            this.txt_port = new System.Windows.Forms.TextBox();
            this.txt_client = new System.Windows.Forms.RichTextBox();
            this.LB_Port_A = new System.Windows.Forms.Label();
            this.txt_ip = new System.Windows.Forms.TextBox();
            this.LB_IP_A = new System.Windows.Forms.Label();
            this.BT_Disconnect_A = new System.Windows.Forms.Button();
            this.BT_Connect_A = new System.Windows.Forms.Button();
            this.BT_SendText_A = new System.Windows.Forms.Button();
            this.GB_CS_A.SuspendLayout();
            this.SuspendLayout();
            // 
            // GB_CS_A
            // 
            this.GB_CS_A.Controls.Add(this.LE_SendText_A);
            this.GB_CS_A.Controls.Add(this.txt_port);
            this.GB_CS_A.Controls.Add(this.txt_client);
            this.GB_CS_A.Controls.Add(this.LB_Port_A);
            this.GB_CS_A.Controls.Add(this.txt_ip);
            this.GB_CS_A.Controls.Add(this.LB_IP_A);
            this.GB_CS_A.Controls.Add(this.BT_Disconnect_A);
            this.GB_CS_A.Controls.Add(this.BT_Connect_A);
            this.GB_CS_A.Controls.Add(this.BT_SendText_A);
            this.GB_CS_A.Location = new System.Drawing.Point(12, 12);
            this.GB_CS_A.Name = "GB_CS_A";
            this.GB_CS_A.Size = new System.Drawing.Size(388, 207);
            this.GB_CS_A.TabIndex = 4;
            this.GB_CS_A.TabStop = false;
            this.GB_CS_A.Text = "Cliente_A - ClientSocket";
            // 
            // LE_SendText_A
            // 
            this.LE_SendText_A.Location = new System.Drawing.Point(7, 89);
            this.LE_SendText_A.Name = "LE_SendText_A";
            this.LE_SendText_A.Size = new System.Drawing.Size(256, 20);
            this.LE_SendText_A.TabIndex = 4;
            // 
            // txt_port
            // 
            this.txt_port.Location = new System.Drawing.Point(112, 32);
            this.txt_port.Name = "txt_port";
            this.txt_port.Size = new System.Drawing.Size(100, 20);
            this.txt_port.TabIndex = 1;
            this.txt_port.Text = "1234";
            // 
            // txt_client
            // 
            this.txt_client.Location = new System.Drawing.Point(8, 116);
            this.txt_client.Name = "txt_client";
            this.txt_client.Size = new System.Drawing.Size(375, 85);
            this.txt_client.TabIndex = 6;
            this.txt_client.Text = "";
            // 
            // LB_Port_A
            // 
            this.LB_Port_A.AutoSize = true;
            this.LB_Port_A.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.LB_Port_A.Location = new System.Drawing.Point(112, 16);
            this.LB_Port_A.Name = "LB_Port_A";
            this.LB_Port_A.Size = new System.Drawing.Size(35, 13);
            this.LB_Port_A.TabIndex = 8;
            this.LB_Port_A.Text = "Porta:";
            // 
            // txt_ip
            // 
            this.txt_ip.Location = new System.Drawing.Point(6, 32);
            this.txt_ip.Name = "txt_ip";
            this.txt_ip.Size = new System.Drawing.Size(100, 20);
            this.txt_ip.TabIndex = 0;
            this.txt_ip.Text = "127.0.0.1";
            // 
            // LB_IP_A
            // 
            this.LB_IP_A.AutoSize = true;
            this.LB_IP_A.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.LB_IP_A.Location = new System.Drawing.Point(6, 16);
            this.LB_IP_A.Name = "LB_IP_A";
            this.LB_IP_A.Size = new System.Drawing.Size(19, 13);
            this.LB_IP_A.TabIndex = 7;
            this.LB_IP_A.Text = "Ip:";
            // 
            // BT_Disconnect_A
            // 
            this.BT_Disconnect_A.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.BT_Disconnect_A.Location = new System.Drawing.Point(268, 58);
            this.BT_Disconnect_A.Name = "BT_Disconnect_A";
            this.BT_Disconnect_A.Size = new System.Drawing.Size(115, 23);
            this.BT_Disconnect_A.TabIndex = 3;
            this.BT_Disconnect_A.Text = "Disconnect";
            this.BT_Disconnect_A.UseVisualStyleBackColor = true;
            // 
            // BT_Connect_A
            // 
            this.BT_Connect_A.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.BT_Connect_A.Location = new System.Drawing.Point(147, 58);
            this.BT_Connect_A.Name = "BT_Connect_A";
            this.BT_Connect_A.Size = new System.Drawing.Size(115, 23);
            this.BT_Connect_A.TabIndex = 2;
            this.BT_Connect_A.Text = "Connect";
            this.BT_Connect_A.UseVisualStyleBackColor = true;
            this.BT_Connect_A.Click += new System.EventHandler(this.BT_Connect_A_Click);
            // 
            // BT_SendText_A
            // 
            this.BT_SendText_A.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.BT_SendText_A.Location = new System.Drawing.Point(268, 87);
            this.BT_SendText_A.Name = "BT_SendText_A";
            this.BT_SendText_A.Size = new System.Drawing.Size(115, 23);
            this.BT_SendText_A.TabIndex = 5;
            this.BT_SendText_A.Text = "Send";
            this.BT_SendText_A.UseVisualStyleBackColor = true;
            this.BT_SendText_A.Click += new System.EventHandler(this.BT_SendText_A_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(433, 244);
            this.Controls.Add(this.GB_CS_A);
            this.Name = "Form1";
            this.Text = "Form1";
            this.GB_CS_A.ResumeLayout(false);
            this.GB_CS_A.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox GB_CS_A;
        private System.Windows.Forms.TextBox LE_SendText_A;
        private System.Windows.Forms.TextBox txt_port;
        private System.Windows.Forms.RichTextBox txt_client;
        private System.Windows.Forms.Label LB_Port_A;
        private System.Windows.Forms.TextBox txt_ip;
        private System.Windows.Forms.Label LB_IP_A;
        private System.Windows.Forms.Button BT_Disconnect_A;
        private System.Windows.Forms.Button BT_Connect_A;
        private System.Windows.Forms.Button BT_SendText_A;
    }
}

