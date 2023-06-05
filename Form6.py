using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Реестр_буровых_на_воду
{
    public partial class Oborud : Form
    {
        public Oborud()
        {
            InitializeComponent();
        }

        private void Oborud_Load(object sender, EventArgs e)
        {
            // TODO: данная строка кода позволяет загрузить данные в таблицу "dataSetReestr.Оборудование". При необходимости она может быть перемещена или удалена.
            this.оборудованиеTableAdapter.Fill(this.dataSetReestr.Оборудование);

        }

        private void saveOborudToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.оборудованиеTableAdapter.Update(this.dataSetReestr.Оборудование);
        }

        private void closeOborudToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
