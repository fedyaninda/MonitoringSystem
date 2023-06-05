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
    public partial class OrgDob : Form
    {
        public OrgDob()
        {
            InitializeComponent();
        }

        private void closeOrgToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void OrgDob_Load(object sender, EventArgs e)
        {
            // TODO: данная строка кода позволяет загрузить данные в таблицу "dataSetReestr.Предприятие". При необходимости она может быть перемещена или удалена.
            this.предприятиеTableAdapter.Fill(this.dataSetReestr.Предприятие);

        }

        private void saveOrgToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.предприятиеTableAdapter.Update(this.dataSetReestr.Предприятие);
        }
    }
}
