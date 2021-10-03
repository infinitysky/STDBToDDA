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
    public partial class MainView : Form
    {
        public MainView()
        {
            InitializeComponent();
        }

        private void exitButton_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void restartButton_Click(object sender, EventArgs e)
        {
            Application.Restart();
        }

        private void dbSetting_Click(object sender, EventArgs e)
        {
            DBConfig form = new DBConfig();
            form.Show();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();
        }





        /* Main Founctions
         */
        private void loadDBConfigrationFile()
        {

        }

        private void createEmptyDBConfigrationFile()
        {

        }


    }
}
