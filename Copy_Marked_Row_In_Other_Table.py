#Laurent Cesaro

#Import Libraries
from Spotfire.Dxp.Data import AddRowsSettings
from Spotfire.Dxp.Data.Import import DataTableDataSource

#Source Data Table
sourceDataTable= Document.Data.Tables["Table1"]

#Mark rows on the source
dataSelection=Document.ActiveMarkingSelectionReference
dataSource=DataTableDataSource(Document.Data.Tables["Table1"],dataSelection)

#Copy rows to new data table
destinationDataTable=Document.Data.Tables["Table2"]
rowsettings=AddRowsSettings(destinationDataTable,dataSource)
destinationDataTable.AddRows(dataSource,rowsettings)
