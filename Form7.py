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
    public partial class Index : Form
    {
        public Index()
        {
            InitializeComponent();
        }

        private void closeIndexToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void Index_Load(object sender, EventArgs e)
        {
            // TODO: данная строка кода позволяет загрузить данные в таблицу "dataSetReestr.Список_индексов". При необходимости она может быть перемещена или удалена.
            this.список_индексовTableAdapter.Fill(this.dataSetReestr.Список_индексов);

        }

        private void saveIndexToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.список_индексовTableAdapter.Update(this.dataSetReestr.Список_индексов);

        }

        private void StripButtonPictureIndex_Click(object sender, EventArgs e)
        {

          



        }
    }
}
