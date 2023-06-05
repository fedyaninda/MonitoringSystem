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
    public partial class DocumentDob : Form
    {
        public DocumentDob()
        {
            InitializeComponent();
           
            bmDocum = this.BindingContext[dsReestr, "Документ"];
            // Добавляем делегата  PositionChanged для события - изменение позиции в таблице Employee DataSet dsEmployee
            // bmDocum.PositionChanged += new EventHandler(BindingManagerBase_PositionChanged);
            

        }

        
        
        DataSetReestr dsReestr = new DataSetReestr();
        DataSetReestrTableAdapters.ДокументTableAdapter daДокумент = new DataSetReestrTableAdapters.ДокументTableAdapter();
        BindingManagerBase bmDocum;



        private void DocumentDob_Load(object sender, EventArgs e)
        {
            // TODO: данная строка кода позволяет загрузить данные в таблицу "dataSetReestr.Документ". При необходимости она может быть перемещена или удалена.
            this.документTableAdapter.Fill(this.dataSetReestr.Документ);

            DocumentFill();
            //dataGridViewDocument.DataSource = dsReestr;
            
            


        }

        private void DocumentFill()
        {
            daДокумент.Fill(dsReestr.Документ);
        }


        private void RemoveDoc()
        {
            string mes = "";
            bmDocum.EndCurrentEdit();
            DataSetReestr.ДокументDataTable dsDoc3 = (DataSetReestr.ДокументDataTable)dsReestr.Документ.GetChanges(DataRowState.Added);
            if (dsDoc3 != null)
                try
                {
                    daДокумент.Update(dsDoc3);
                    dsDoc3.Dispose();
                    dsReestr.Документ.AcceptChanges();
                }
                     catch (Exception x)
                {
                    string m = x.Message;
                    MessageBox.Show("Ошибка удаления записи в базе данных Реестр буровых на вод скважин" + mes, "Предупреждение");
                    dsReestr.Документ.RejectChanges();
                }
        }
                
        private void SaveDocToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.документTableAdapter.Update(this.dataSetReestr.Документ);
            //saveDoc();
            
        }

        //private void saveDoc()
        //{
        //    string mes = "";
        //    bmDocum.EndCurrentEdit();
        //    DataSetReestr.ДокументDataTable dsDoc2 = (DataSetReestr.ДокументDataTable)dsReestr.Документ.GetChanges(DataRowState.Added);
        //    if (dsDoc2 != null)
        //        try
        //        {
        //            daДокумент.Update(dsDoc2);
        //            dsDoc2.Dispose();
        //            dsReestr.Документ.AcceptChanges();
        //        }
        //        catch (Exception x)
        //        {
        //            string m = x.Message;
        //            MessageBox.Show("Ошибка вставки записи в базу данных Реестр буровых на вод скважин" + mes, "Предупреждение");
        //            dsReestr.Документ.RejectChanges();
        //        }
        //    DataSetReestr.ДокументDataTable dsDoc1 = (DataSetReestr.ДокументDataTable)dsReestr.Документ.GetChanges(DataRowState.Modified);
        //    if (dsDoc1 != null)
        //        try
        //        {
        //            daДокумент.Update(dsDoc1);
        //            dsDoc1.Dispose();
        //            dsReestr.Документ.AcceptChanges();
        //        }
        //        catch (Exception x)
        //        {
        //            string m = x.Message;
        //            MessageBox.Show("Ошибка вставки записи в базу данных Реестр буровых на вод скважин" + mes, "Предупреждение");
        //            dsReestr.Документ.RejectChanges();
        //        }
        //}

        private void closeDocToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void removeDocMenuItem1_Click(object sender, EventArgs e)
        {
            RemoveDoc();
        }

        private void dataGridViewDocument_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void UpdateMenuItem1_Click(object sender, EventArgs e)
        {

        }

        private void ActionDocToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        

        private void редактироватьТаблицуToolStripMenuItem_Click(object sender, EventArgs e)
        {
            
        }
    }
}
