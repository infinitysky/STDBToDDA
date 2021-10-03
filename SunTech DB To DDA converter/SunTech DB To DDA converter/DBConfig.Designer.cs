
namespace SunTech_DB_To_DDA_converter
{
    partial class DBConfig
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
            this.BDConfigCloseButton = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.label4 = new System.Windows.Forms.Label();
            this.dbConnectionPasswordInputBox = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.dbConnectionUserNameInputBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.dbNameInputBox = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.dbSourceInputBox = new System.Windows.Forms.TextBox();
            this.dbConfigSaveButton = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // BDConfigCloseButton
            // 
            this.BDConfigCloseButton.Location = new System.Drawing.Point(322, 343);
            this.BDConfigCloseButton.Name = "BDConfigCloseButton";
            this.BDConfigCloseButton.Size = new System.Drawing.Size(75, 23);
            this.BDConfigCloseButton.TabIndex = 0;
            this.BDConfigCloseButton.Text = "Close";
            this.BDConfigCloseButton.UseVisualStyleBackColor = true;
            this.BDConfigCloseButton.Click += new System.EventHandler(this.BDConfigCloseButton_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.label4);
            this.groupBox1.Controls.Add(this.dbConnectionPasswordInputBox);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.dbConnectionUserNameInputBox);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.dbNameInputBox);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.dbSourceInputBox);
            this.groupBox1.Location = new System.Drawing.Point(30, 30);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(367, 270);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Database Settings";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(27, 201);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(53, 13);
            this.label4.TabIndex = 7;
            this.label4.Text = "Password";
            // 
            // dbConnectionPasswordInputBox
            // 
            this.dbConnectionPasswordInputBox.Location = new System.Drawing.Point(182, 198);
            this.dbConnectionPasswordInputBox.Name = "dbConnectionPasswordInputBox";
            this.dbConnectionPasswordInputBox.Size = new System.Drawing.Size(140, 20);
            this.dbConnectionPasswordInputBox.TabIndex = 6;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(27, 147);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(60, 13);
            this.label3.TabIndex = 5;
            this.label3.Text = "User Name";
            // 
            // dbConnectionUserNameInputBox
            // 
            this.dbConnectionUserNameInputBox.Location = new System.Drawing.Point(182, 144);
            this.dbConnectionUserNameInputBox.Name = "dbConnectionUserNameInputBox";
            this.dbConnectionUserNameInputBox.Size = new System.Drawing.Size(140, 20);
            this.dbConnectionUserNameInputBox.TabIndex = 4;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(27, 96);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(84, 13);
            this.label2.TabIndex = 3;
            this.label2.Text = "Database Name";
            // 
            // dbNameInputBox
            // 
            this.dbNameInputBox.Location = new System.Drawing.Point(182, 93);
            this.dbNameInputBox.Name = "dbNameInputBox";
            this.dbNameInputBox.Size = new System.Drawing.Size(140, 20);
            this.dbNameInputBox.TabIndex = 2;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(27, 49);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(90, 13);
            this.label1.TabIndex = 1;
            this.label1.Text = "Database Source";
            // 
            // dbSourceInputBox
            // 
            this.dbSourceInputBox.Location = new System.Drawing.Point(182, 46);
            this.dbSourceInputBox.Name = "dbSourceInputBox";
            this.dbSourceInputBox.Size = new System.Drawing.Size(140, 20);
            this.dbSourceInputBox.TabIndex = 0;
            // 
            // dbConfigSaveButton
            // 
            this.dbConfigSaveButton.Location = new System.Drawing.Point(30, 343);
            this.dbConfigSaveButton.Name = "dbConfigSaveButton";
            this.dbConfigSaveButton.Size = new System.Drawing.Size(75, 23);
            this.dbConfigSaveButton.TabIndex = 2;
            this.dbConfigSaveButton.Text = "Save";
            this.dbConfigSaveButton.UseVisualStyleBackColor = true;
            this.dbConfigSaveButton.Click += new System.EventHandler(this.dbConfigSaveButton_Click);
            // 
            // DBConfig
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(436, 409);
            this.Controls.Add(this.dbConfigSaveButton);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.BDConfigCloseButton);
            this.Name = "DBConfig";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Database Configuration";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button BDConfigCloseButton;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox dbConnectionPasswordInputBox;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox dbConnectionUserNameInputBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox dbNameInputBox;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox dbSourceInputBox;
        private System.Windows.Forms.Button dbConfigSaveButton;
    }
}