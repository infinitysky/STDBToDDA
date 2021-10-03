using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SunTech_DB_To_DDA_converter
{
    public partial class DBConfig : Form
    {
        public DBConfig()
        {
            InitializeComponent();
        }


        private void BDConfigCloseButton_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void dbConfigSaveButton_Click(object sender, EventArgs e)
        {
            Application.Restart();
        }
    }
}
