#Laurent Cesaro

#This script permit to recover a row in a datatable and display it in a label (Document.Properties)

#Inport library
from Spotfire.Dxp.Data import DataValueCursor

#Create cursor on table
myStatusCursor = DataValueCursor.CreateFormatted(Document.Data.Tables["Table_Name"].Columns["Column_Name"])
#Select marked row
markedRows = Document.Data.Markings["Marking"].GetSelection(Document.Data.Tables["Table_Name"]).AsIndexSet()

#Add in your Document.Properties the table value
for row in Document.Data.Tables["Table_Name"].GetRows(markedRows, myStatusCursor):
	Document.Properties["Porprety_Name"] = myStatusCursor.CurrentValue
