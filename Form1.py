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
    public partial class GlMenu : Form
    {
        public GlMenu()
        {
            InitializeComponent();
        }

        private void Exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void buttonUK_Click(object sender, EventArgs e)
        {
            UK UK = new UK();
            UK.Show();
        }

        private void ButtonDocumentation_Click(object sender, EventArgs e)
        {
            DocumentDob documentDob = new DocumentDob();

            documentDob.ShowDialog();
        }

        private void ButtonObject_Click(object sender, EventArgs e)
        {
            ReestrObj reestrObj = new ReestrObj();
            reestrObj.ShowDialog();
        }

        private void buttonYear_Click(object sender, EventArgs e)
        {
            ReestrYear reestrYear = new ReestrYear();
            reestrYear.ShowDialog();
        }
    }
}
