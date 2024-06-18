using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace WindowsFormsApp4
{
    public partial class Form1 : Form
    {
        ClassLibrary1.Class1 cl = new ClassLibrary1.Class1();
        public Form1()
        {
            InitializeComponent();
        }
        private void button1_Click(object sender, EventArgs e)
        {

            cl.insertar(textBox2.Text, textBox3.Text, textBox4.Text);

        }

        private void button2_Click(object sender, EventArgs e)
        {
            DataTable dt2 = new DataTable();
            dt2 = cl.mostrar();
            dataGridView1.DataSource = dt2;
        }

       

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
