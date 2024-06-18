using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Data.SqlClient;
using System.Data;

namespace ClassLibrary1
{
    public class Class1
    {
        String con = "Data Source = PABLITOJUNIOR\\THEGAMMER;Initial Catalog = estudiante; Integrated Security = True";
        public void insertar(string a, string b, string c)
        {
            using (SqlConnection cn = new SqlConnection(con))
            {
                SqlCommand cmd = new SqlCommand("insert into Estudiantes(nombre, apellido, edad) values ('" + a + "','" + b + "'," + Convert.ToInt32(c) + ")", cn);
                cmd.CommandType = CommandType.Text;
                cn.Open();
                cmd.ExecuteNonQuery();
            }
        }
        public DataTable mostrar()
        {
            DataTable dt = new DataTable();
            using (SqlConnection cn = new SqlConnection(con))
            {
                SqlDataAdapter dap = new SqlDataAdapter("select * from Estudiantes", cn);
                dap.SelectCommand.CommandType = CommandType.Text;
                cn.Open();
                dap.Fill(dt);
            }
            return dt;
        }
    }
}
