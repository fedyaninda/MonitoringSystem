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
namespace Реестр_буровых_на_воду
{
   
    public partial class UK : Form
    {
        public UK()
        {
            InitializeComponent();
            bmReestr = this.BindingContext[dsReestr, "Учетная карточка"];
            // Добавляем делегата  PositionChanged для события - изменение позиции в таблице Employee DataSet dsEmployee
            bmReestr.PositionChanged += new EventHandler(BindingManagerBase_PositionChanged);
        }

        private void BindingManagerBase_PositionChanged(object sender, EventArgs e)
        {
            int pos = ((BindingManagerBase)sender).Position;
            int sel = (int)dsReestr.Учетная_карточка[pos].Код_карточки;
            //this.comboBoxChoiceUK.Text = this.textBoxKodUK.Text[sel].ToString();
        }

        public void MenuItemEnabled(bool itemEnabled)
        {
            if (itemEnabled == true)
            {
                createToolStripMenuItem.Enabled = true;
                editToolStripMenuItem.Enabled = true;
                saveToolStripMenuItem.Enabled = false;
                undoToolStripMenuItem.Enabled = false;
                removeToolStripMenuItem.Enabled = true;
                CloseWindowToolStripMenuItem.Enabled = true;
                ExitWindowToolStripMenuItem.Enabled = true;
            }
            else
            {
                createToolStripMenuItem.Enabled = false;
                editToolStripMenuItem.Enabled = false;
                saveToolStripMenuItem.Enabled = true;
                undoToolStripMenuItem.Enabled = true;
                removeToolStripMenuItem.Enabled = true;
                CloseWindowToolStripMenuItem.Enabled = false;
                ExitWindowToolStripMenuItem.Enabled = false;

            }

        }

        public void ReadOnly(bool readOnly)

        {
            if (readOnly == true)

            {
                comboBoxRegion.Enabled = false;
                comboBoxUlus.Enabled = false;
                comboBoxNom10.Enabled = false;
                comboBoxNom5.Enabled = false;
                comboBoxNom2.Enabled = false;
                textBoxKodUK.Enabled = false;
                textBoxNomerUK.Enabled = false;
                textBoxYear.Enabled = false;
                textBoxNaz.Enabled = false;
                textBoxSost.Enabled = false;
                comboBoxInvn.Enabled = false;
                textBoxAvtors.Enabled = false;
                richTextBoxDocument.Enabled = false;
                textBoxMestoHr.Enabled = false;
                comboBoxOrg.Enabled = false;
                richTextBoxAdres.Enabled = false;
                textBoxSShGrad.Enabled = false;
                textBoxSShMin.Enabled = false;
                textBoxSShSec.Enabled = false;
                textBoxVDGrad.Enabled = false;
                textBoxVDMin.Enabled = false;
                textBoxVDSec.Enabled = false;
                textBoxNomSkv.Enabled = false;
                textBoxAbsOtm.Enabled = false;
                textBoxGlub.Enabled = false;
                textBoxYearBur.Enabled = false;
                textBoxIsp.Enabled = false;
                textBoxStoimostO.Enabled = false;
                textBoxStoimostB.Enabled = false;
                richTextBoxDopSved.Enabled = false;
                textBoxDataZap.Enabled = false;
                textBoxUKZap.Enabled = false;
                textBoxUKPro.Enabled = false;
                textBoxFioPro.Enabled = false;
                textBoxFioZap.Enabled = false;
                dataGridViewConst.Enabled = false;
                dataGridViewRazrez.Enabled = false;
                dataGridViewVG.Enabled = false;
                dataGridViewDebit.Enabled = false;
                comboBoxNomVG.Enabled = false;
                textBoxDataOtbPr.Enabled = false;
                textBoxGlubOtbOt.Enabled = false;
                textBoxGlubOtbDo.Enabled = false;
                comboBoxInfOtk.Enabled = false;
                textBoxCvet.Enabled = false;
                textBoxCvetGr.Enabled = false;
                textBoxZapah.Enabled = false;
                textBoxZapahB.Enabled = false;
                textBoxVkus.Enabled = false;
                textBoxVkusB.Enabled = false;
                textBoxProzr.Enabled = false;
                textBoxProzrSm.Enabled = false;
                textBoxOsadok.Enabled = false;
                textBoxOsadokMg.Enabled = false;
                textBoxTemp.Enabled = false;
                textBoxPlotn.Enabled = false;
                textBoxOkisl.Enabled = false;
                textBoxSuhOst.Enabled = false;
                textBoxZhObsh.Enabled = false;
                textBoxZhUst.Enabled = false;
                textBoxECl.Enabled = false;
                textBoxESO4.Enabled = false;
                textBoxEHCO3.Enabled = false;
                textBoxECa.Enabled = false;
                textBoxEMg.Enabled = false;
                textBoxENaK.Enabled = false;
                textBoxFKM.Enabled = false;
                textBoxFKHCO3.Enabled = false;
                textBoxFKSO4.Enabled = false;
                textBoxFKCl.Enabled = false;
                textBoxFKNO2.Enabled = false;
                textBoxFKF.Enabled = false;
                textBoxFKCa.Enabled = false;
                textBoxFKMg.Enabled = false;
                textBoxFKNa.Enabled = false;
                textBoxFKK.Enabled = false;
                textBoxFKNH.Enabled = false;
                textBoxFKFe.Enabled = false;
                textBoxFKNaK.Enabled = false;
                textBoxpH.Enabled = false;
                textBoxFKT.Enabled = false;
                textBoxFKD.Enabled = false;
                textBoxBaktAnaliz.Enabled = false;
                dataGridViewDopHimKom.Enabled = false;
            }
            else
            {
                comboBoxRegion.Enabled = true;
                comboBoxUlus.Enabled = true;
                comboBoxNom10.Enabled = true;
                comboBoxNom5.Enabled = true;
                comboBoxNom2.Enabled = true;
                textBoxKodUK.Enabled = true;
                textBoxNomerUK.Enabled = true;
                textBoxYear.Enabled = true;
                textBoxNaz.Enabled = true;
                textBoxSost.Enabled = true;
                comboBoxInvn.Enabled = true;
                textBoxAvtors.Enabled = true;
                richTextBoxDocument.Enabled = true;
                textBoxMestoHr.Enabled = true;
                comboBoxOrg.Enabled = true;
                richTextBoxAdres.Enabled = true;
                textBoxSShGrad.Enabled = true;
                textBoxSShMin.Enabled = true;
                textBoxSShSec.Enabled = true;
                textBoxVDGrad.Enabled = true;
                textBoxVDMin.Enabled = true;
                textBoxVDSec.Enabled = true;
                textBoxNomSkv.Enabled = true;
                textBoxAbsOtm.Enabled = true;
                textBoxGlub.Enabled = true;
                textBoxYearBur.Enabled = true;
                textBoxIsp.Enabled = true;
                textBoxStoimostO.Enabled = true;
                textBoxStoimostB.Enabled = true;
                richTextBoxDopSved.Enabled = true;
                textBoxDataZap.Enabled = true;
                textBoxUKZap.Enabled = true;
                textBoxUKPro.Enabled = true;
                textBoxFioPro.Enabled = true;
                textBoxFioZap.Enabled = true;
                dataGridViewConst.Enabled = true;
                dataGridViewRazrez.Enabled = true;
                dataGridViewVG.Enabled = true;
                dataGridViewDebit.Enabled = true;
                comboBoxNomVG.Enabled = true;
                textBoxDataOtbPr.Enabled = true;
                textBoxGlubOtbOt.Enabled = true;
                textBoxGlubOtbDo.Enabled = true;
                comboBoxInfOtk.Enabled = true;
                textBoxCvet.Enabled = true;
                textBoxCvetGr.Enabled = true;
                textBoxZapah.Enabled = true;
                textBoxZapahB.Enabled = true;
                textBoxVkus.Enabled = true;
                textBoxVkusB.Enabled = true;
                textBoxProzr.Enabled = true;
                textBoxProzrSm.Enabled = true;
                textBoxOsadok.Enabled = true;
                textBoxOsadokMg.Enabled = true;
                textBoxTemp.Enabled = true;
                textBoxPlotn.Enabled = true;
                textBoxOkisl.Enabled = true;
                textBoxSuhOst.Enabled = true;
                textBoxZhObsh.Enabled = true;
                textBoxZhUst.Enabled = true;
                textBoxECl.Enabled = true;
                textBoxESO4.Enabled = true;
                textBoxEHCO3.Enabled = true;
                textBoxECa.Enabled = true;
                textBoxEMg.Enabled = true;
                textBoxENaK.Enabled = true;
                textBoxFKM.Enabled = true;
                textBoxFKHCO3.Enabled = true;
                textBoxFKSO4.Enabled = true;
                textBoxFKCl.Enabled = true;
                textBoxFKNO2.Enabled = true;
                textBoxFKF.Enabled = true;
                textBoxFKCa.Enabled = true;
                textBoxFKMg.Enabled = true;
                textBoxFKNa.Enabled = true;
                textBoxFKK.Enabled = true;
                textBoxFKNH.Enabled = true;
                textBoxFKFe.Enabled = true;
                textBoxFKNaK.Enabled = true;
                textBoxpH.Enabled = true;
                textBoxFKT.Enabled = true;
                textBoxFKD.Enabled = true;
                textBoxBaktAnaliz.Enabled = true;
                dataGridViewDopHimKom.Enabled = true;
            }
        }


        private void DisplayForm(bool mode)

        {
            MenuItemEnabled(mode);
            ReadOnly(mode);
        }

        public void ReestrFill()
        {
            daСписок_районов.Fill(dsReestr.Список_районов);
            daДокумент.Fill(dsReestr.Документ);
            daПредприятие.Fill(dsReestr.Предприятие);
            daОборудование.Fill(dsReestr.Оборудование);
            daСписок_индексов.Fill(dsReestr.Список_индексов);
            daУчетная_карточка.Fill(dsReestr.Учетная_карточка);
            daКонструкция_скважины.Fill(dsReestr.Конструкция_скважины);
            daГеологический_разрез.Fill(dsReestr.Геологический_разрез);
            daВодоносный_горизонт.Fill(dsReestr.Водоносный_горизонт);
            daДебит.Fill(dsReestr.Дебит);
            daХимический_анализ.Fill(dsReestr.Химический_анализ);
            daФизические_свойства.Fill(dsReestr.Физические_свойства);
            daДополнительные_химические_элементы.Fill(dsReestr.Дополнительные_химические_элементы);
            daФормула_Курлова.Fill(dsReestr.Формула_Курлова);
        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void groupBox1_Enter_1(object sender, EventArgs e)
        {

        }

        private void ChoiceUK()
        {
            dsReestr.Учетная_карточка.Columns.Add("FullName", typeof(string), "Номенклатура_топографической_карты_1к1000+'-'+[1к500т]+'-'+Номер_карточки");

        }
        private void AddChoiceUK()
        {
            comboBoxChoiceUK.DataSource = dsReestr;
            comboBoxChoiceUK.DisplayMember = "Учетная карточка.FullName";
        }

        private void UK_Load(object sender, EventArgs e)
        {
            // TODO: данная строка кода позволяет загрузить данные в таблицу "dataSetReestr.Список_индексов". При необходимости она может быть перемещена или удалена.
            this.список_индексовTableAdapter.Fill(this.dataSetReestr.Список_индексов);


            // TODO: данная строка кода позволяет загрузить данные в таблицу "dataSetReestr.Документ". При необходимости она может быть перемещена или удалена.
            this.документTableAdapter.Fill(this.dataSetReestr.Документ);
            // TODO: данная строка кода позволяет загрузить данные в таблицу "dataSetReestr.Список_районов". При необходимости она может быть перемещена или удалена.
            this.список_районовTableAdapter.Fill(this.dataSetReestr.Список_районов);
            // TODO: данная строка кода позволяет загрузить данные в таблицу "dataSetReestr.Учетная_карточка". При необходимости она может быть перемещена или удалена.
            this.учетная_карточкаTableAdapter.Fill(this.dataSetReestr.Учетная_карточка);
            
            DisplayForm(true);
            ReestrFill();
            ChoiceUK();
            AddChoiceUK();
            OsnSved();
            Document_UK();
            Org();

            dataGridViewVG.DataSource = dsReestr;
            dataGridViewVG.DataMember = "Учетная карточка.Код_карточки";
            dataGridViewVG.DataBindings.Add("Text", dsReestr, "Учетная карточка.Код_карточки");
            //ColumnNVG.DataGridView.DataSource = dsReestr.Водоносный_горизонт;
            //ColumnNVG.DataGridView.DataBindings.Add("Text", dsReestr, "Учетная карточка.Код_карточки");

        }

        private void OsnSved ()
        {
            textBoxKodUK.DataBindings.Add("Text", dsReestr, "Учетная карточка.Код_карточки");
            textBoxSost.DataBindings.Add("Text", dsReestr, "Учетная карточка.Состояние");
            textBoxNaz.DataBindings.Add("Text", dsReestr, "Учетная карточка.Назначение");
            textBoxNomerUK.DataBindings.Add("Text", dsReestr, "Учетная карточка.Номер_карточки");
            comboBoxNom10.DataBindings.Add("Text", dsReestr, "Учетная карточка.Номенклатура_топографической_карты_1к1000");
            comboBoxNom5.DataBindings.Add("Text", dsReestr, "Учетная карточка.1к500т");
            comboBoxNom2.DataBindings.Add("Text", dsReestr, "Учетная карточка.1к200т");
            comboBoxUlus.DataSource = dsReestr.Список_районов;
            comboBoxUlus.DisplayMember = "Район";
            comboBoxUlus.Text = "Район";
            comboBoxUlus.DataBindings.Add("Text", dsReestr, "Учетная карточка.Район");
            comboBoxRegion.DataBindings.Add("Text", dsReestr, "Список районов.Регион");
            textBoxYear.DataBindings.Add("Text", dsReestr, "Учетная карточка.Год_заполнения");
            richTextBoxAdres.DataBindings.Add("Text", dsReestr, "Учетная карточка.Адрес");
            textBoxNomSkv.DataBindings.Add("Text", dsReestr, "Учетная карточка.Номер_скважины_при_бурении");
            textBoxSShGrad.DataBindings.Add("Text", dsReestr, "Учетная карточка.СШГ");
            textBoxSShMin.DataBindings.Add("Text", dsReestr, "Учетная карточка.СШМ");
            textBoxSShSec.DataBindings.Add("Text", dsReestr, "Учетная карточка.СШС");
            textBoxVDGrad.DataBindings.Add("Text", dsReestr, "Учетная карточка.ВДГ");
            textBoxVDMin.DataBindings.Add("Text", dsReestr, "Учетная карточка.ВДМ");
            textBoxVDSec.DataBindings.Add("Text", dsReestr, "Учетная карточка.ВДС");
            textBoxAbsOtm.DataBindings.Add("Text", dsReestr, "Учетная карточка.Абсолютная_отметка_устья");
            textBoxYearBur.DataBindings.Add("Text", dsReestr, "Учетная карточка.Год_бурения");
            textBoxGlub.DataBindings.Add("Text", dsReestr, "Учетная карточка.Глубина");
            textBoxStoimostO.DataBindings.Add("Text", dsReestr, "Учетная карточка.Стоимость_общая");
            textBoxStoimostB.DataBindings.Add("Text", dsReestr, "Учетная карточка.В_т_ч_бурения");
            richTextBoxDopSved.DataBindings.Add("Text", dsReestr, "Учетная карточка.Доп_сведения");
            textBoxDataZap.DataBindings.Add("Text", dsReestr, "Учетная карточка.Дата_заполнения");
            textBoxFioZap.DataBindings.Add("Text", dsReestr, "Учетная карточка.ФИО_заполняющего");
            textBoxFioPro.DataBindings.Add("Text", dsReestr, "Учетная карточка.ФИО_проверяющего");
            textBoxUKPro.DataBindings.Add("Text", dsReestr, "Учетная карточка.Должность_проверяющего");
            textBoxUKZap.DataBindings.Add("Text", dsReestr, "Учетная карточка.Должность_заполняющего");
            textBoxIsp.DataBindings.Add("Text", dsReestr, "Учетная карточка.Использование");
        }


        


        private void Document_UK()
        {
            comboBoxInvn.DataSource = dsReestr;
            comboBoxInvn.DisplayMember = "Документ.Инвентарный_номер";
            comboBoxInvn.ValueMember = "Документ.Код_документа";
            comboBoxInvn.DataBindings.Add("SelectedValue", dsReestr, "Учетная карточка.Код_документа");
            textBoxAvtors.DataBindings.Add("Text", dsReestr, "Документ.Автор");
            richTextBoxDocument.DataBindings.Add("Text", dsReestr, "Документ.Название_документа");
            textBoxMestoHr.DataBindings.Add("Text", dsReestr, "Документ.Место_хранения");
            


        }



            private void Org()
        {
            comboBoxOrg.DataSource = dsReestr.Предприятие;
            comboBoxOrg.DisplayMember = "Краткое_наименование";
            comboBoxOrg.ValueMember = "Код_предприятия";
            comboBoxOrg.DataBindings.Add("SelectedValue", dsReestr, "Учетная карточка.Код_предприятия");

        }

        private void Const()
        {

        }

        private void labelDocument_Click(object sender, EventArgs e)
        {

        }

        private void textBoxSShGrad_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBoxSost_TextChanged(object sender, EventArgs e)
        {

        }

        private void labelSost_Click(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void dataGridViewConst_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void label1_Click_1(object sender, EventArgs e)
        {

        }

        public void Turn()
        {
            this.WindowState = FormWindowState.Minimized;
        }

        private void createToolStripMenuItem_Click(object sender, EventArgs e)
        {
            DisplayForm(false);
            Create();
            //Save();
        }

        private void actionToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void editToolStripMenuItem_Click(object sender, EventArgs e)
        {
            DisplayForm(false);
        }

        private void saveToolStripMenuItem_Click(object sender, EventArgs e)
        {
            DisplayForm(true);
            Save();

        }
        
        private void Create ()
        {
            DataRow rowUK = dsReestr.Учетная_карточка.NewУчетная_карточкаRow();
            rowUK["Район"] = "н/д";
            rowUK["Код_документа"] = 1;
            rowUK["Код_предприятия"] = 1;
            dsReestr.Учетная_карточка.Rows.Add(rowUK);
            int pos = dsReestr.Учетная_карточка.Rows.Count  - 1;
            BindingContext[dsReestr, "Учетная карточка.Код_карточки"].Position = pos;
            textBoxNomerUK.Focus();
         

            
        }

        private void Save ()
        {
            string mes = "";
            bmReestr.EndCurrentEdit();
            DataSetReestr.Учетная_карточкаDataTable ds2 = (DataSetReestr.Учетная_карточкаDataTable)dsReestr.Учетная_карточка.GetChanges(DataRowState.Added);
            if (ds2 != null)
                try
                {
                    daУчетная_карточка.Update(ds2);
                    ds2.Dispose();
                    dsReestr.AcceptChanges();
                }

                catch (Exception x)
                {
                    string m = x.Message;
                    MessageBox.Show("Ошибка вставки записи в базу данных Реестр буровых на вод скважин" + mes, "Предупреждение");
                    dsReestr.Учетная_карточка.RejectChanges();
                }
            DataSetReestr.Учетная_карточкаDataTable ds1 = (DataSetReestr.Учетная_карточкаDataTable)dsReestr.Учетная_карточка.GetChanges(DataRowState.Modified);
            if (ds1!=null)
                try
                {
                    daУчетная_карточка.Update(ds1);
                    ds1.Dispose();
                    dsReestr.Учетная_карточка.AcceptChanges();
                }
                catch(Exception X)
                {
                    string m = X.Message;
                    MessageBox.Show("Ошибка обновления базы данных Реестр буровых на вод скважин" + mes, "Предупреждение");
                    dsReestr.Учетная_карточка.RejectChanges();

                }
            DataSetReestr.ДокументDataTable ds3 = (DataSetReestr.ДокументDataTable)dsReestr.Документ.GetChanges(DataRowState.Modified);
            if (ds3 != null)
                try
                {
                    daДокумент.Update(ds3);
                    ds3.Dispose();
                    dsReestr.AcceptChanges();
                }
                catch (Exception X)
                {
                    string m = X.Message;
                    MessageBox.Show("Ошибка обновления базы данных Реестр буровых на вод скважин" + mes, "Предупреждение");
                    dsReestr.Учетная_карточка.RejectChanges();

                }


        }

        private void undoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            DisplayForm(true);
            Undo();
        }

        private void Undo()
        {
            bmReestr.EndCurrentEdit();
            dsReestr.Учетная_карточка.RejectChanges();
            dsReestr.Документ.RejectChanges();
            dsReestr.Предприятие.RejectChanges();
        }

        private void свернутьОкноToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Turn();
        }

        private void закрытьОкноToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        DataSetReestr dsReestr = new DataSetReestr();
        DataSetReestrTableAdapters.Учетная_карточкаTableAdapter daУчетная_карточка = new DataSetReestrTableAdapters.Учетная_карточкаTableAdapter();
        DataSetReestrTableAdapters.Водоносный_горизонтTableAdapter daВодоносный_горизонт = new DataSetReestrTableAdapters.Водоносный_горизонтTableAdapter();
        DataSetReestrTableAdapters.Геологический_разрезTableAdapter daГеологический_разрез = new DataSetReestrTableAdapters.Геологический_разрезTableAdapter();
        DataSetReestrTableAdapters.ДебитTableAdapter daДебит = new DataSetReestrTableAdapters.ДебитTableAdapter();
        DataSetReestrTableAdapters.ДокументTableAdapter daДокумент = new DataSetReestrTableAdapters.ДокументTableAdapter();
        DataSetReestrTableAdapters.Дополнительные_химические_элементыTableAdapter daДополнительные_химические_элементы = new DataSetReestrTableAdapters.Дополнительные_химические_элементыTableAdapter();
        DataSetReestrTableAdapters.Конструкция_скважиныTableAdapter daКонструкция_скважины = new DataSetReestrTableAdapters.Конструкция_скважиныTableAdapter();
        DataSetReestrTableAdapters.ОборудованиеTableAdapter daОборудование = new DataSetReestrTableAdapters.ОборудованиеTableAdapter();
        DataSetReestrTableAdapters.ПредприятиеTableAdapter daПредприятие = new DataSetReestrTableAdapters.ПредприятиеTableAdapter();
        DataSetReestrTableAdapters.Список_индексовTableAdapter daСписок_индексов = new DataSetReestrTableAdapters.Список_индексовTableAdapter();
        DataSetReestrTableAdapters.Список_районовTableAdapter daСписок_районов = new DataSetReestrTableAdapters.Список_районовTableAdapter();
        DataSetReestrTableAdapters.Физические_свойстваTableAdapter daФизические_свойства = new DataSetReestrTableAdapters.Физические_свойстваTableAdapter();
        DataSetReestrTableAdapters.Формула_КурловаTableAdapter daФормула_Курлова = new DataSetReestrTableAdapters.Формула_КурловаTableAdapter();
        DataSetReestrTableAdapters.Химический_анализTableAdapter daХимический_анализ = new DataSetReestrTableAdapters.Химический_анализTableAdapter();
        BindingManagerBase bmReestr;

        private void comboNom10_SelectedIndexChanged(object sender, EventArgs e)
        {
            
        }

        private void comboBoxNom5_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void comboBoxChoiceUK_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void menuStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

        }

       

        private void buttonOrg_Click(object sender, EventArgs e)
        {
            OrgDob OrgDob = new OrgDob();

            OrgDob.ShowDialog();

        }

        private void UpdateStripMenuItem1_Click(object sender, EventArgs e)
        {
            
        }

        private void ButtonDocumentation_Click(object sender, EventArgs e)
        {
            DocumentDob documentDob = new DocumentDob();

            documentDob.ShowDialog();
        }

        private void labelZapah_Click(object sender, EventArgs e)
        {

        }

        private void tabPageCharWater_Click(object sender, EventArgs e)
        {

        }

        private void textBoxECa_TextChanged(object sender, EventArgs e)
        {

        }

        private void labelFKSO4_Click(object sender, EventArgs e)
        {

        }

        private void buttonOborud_Click(object sender, EventArgs e)
        {
            Oborud oborud = new Oborud();
            oborud.ShowDialog();
        }

        private void buttonSIndex_Click(object sender, EventArgs e)
        {
            Index index = new Index();
            index.ShowDialog();
        }
    }
}
