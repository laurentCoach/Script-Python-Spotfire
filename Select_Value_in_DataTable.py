#Laurent Cesaro
#Date 16/11/2016
#This script permit to recover a row in a datatable and display it in a label (Document.Properties)


from Spotfire.Dxp.Data import DataValueCursor

myStatusCursor = DataValueCursor.CreateFormatted(Document.Data.Tables["Table_Name"].Columns["Column_Name"])
markedRows = Document.Data.Markings["Marking"].GetSelection(Document.Data.Tables["Table_Name"]).AsIndexSet()

for row in Document.Data.Tables["Table_Name"].GetRows(markedRows, myStatusCursor):
	Document.Properties["Porprety_Name"] = myStatusCursor.CurrentValue