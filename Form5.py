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
    public partial class ReestrObj : Form
    {
        public ReestrObj()
        {
            InitializeComponent();
        }

        private void ReestrObj_Load(object sender, EventArgs e)
        {
            ReadOnlyAdm(false);
            ReadOnlyNomencl(false);
        }

        private void ReadOnlyAdm(bool readOnlyAdm)
        {
           if (readOnlyAdm == true)
            {
                comboBoxOtchetAdm.Enabled = true;
                buttonOtchetAdm.Enabled = true;
            }
           else
            {
                comboBoxOtchetAdm.Enabled = false;
                buttonOtchetAdm.Enabled = false;

            }
        }

        private void ReadOnlyNomencl (bool readOnlyNomencl)
        {
            if (readOnlyNomencl == true)
            {
                comboBoxOtchetNomencl.Enabled = true;
                buttonOtchNomencl.Enabled = true;
            }
            else
            {
                comboBoxOtchetNomencl.Enabled = false;
                buttonOtchNomencl.Enabled = false;
            }
        }

        private void radioButtonOtchetAdm_CheckedChanged(object sender, EventArgs e)
        {
            ReadOnlyAdm(true);
            ReadOnlyNomencl(false);
        }

        private void radioButtonOtchetNomencl_CheckedChanged(object sender, EventArgs e)
        {
            ReadOnlyNomencl(true);
            ReadOnlyAdm(false);
        }
    }
}
