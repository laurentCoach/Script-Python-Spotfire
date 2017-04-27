#Laurent Cesaro
#20/10/2016
#Lauch with a button Kruskal-Wallis


from System.IO import Directory
from System.Windows.Forms import MessageBox, MessageBoxButtons
from System.Windows.Forms import DialogResult
from Spotfire.Dxp.Application.Calculations.DataRelationships import *
from Spotfire.Dxp.Application.Calculations import *
from Spotfire.Dxp.Data import CalculationExecutionPromptMode

try:
	#Select the document calculation (The kruskal test must already be created)
	#If this is your first test of kruskal wallis, the number is 0
	kruskal = Document.Calculations[0]
	settings = Document.Calculations[0].CalculationSettings
	#Clear the existing X and YColumns
	settings.XColumns.Clear()
	settings.YColumns.Clear()

	#@param table: the dataTable from which we get the data
	#Select columns
	for col in Table.Columns:
	  if "ColName" in col.ToString():
		settings.YColumns.Add(col)
	  if col.ToString() == "ColName":
		settings.XColumns.Add(col)

	#Executes the calculation with the new settings (to prompt the user change never to always or remove "CalculationExecutionPromptMode.Never")
	kruskal.Execute(CalculationExecutionPromptMode.Never)

except:
	MessageBox.Show("Error")
