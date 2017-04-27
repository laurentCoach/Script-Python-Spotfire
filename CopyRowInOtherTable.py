from Spotfire.Dxp.Data import AddRowsSettings
from Spotfire.Dxp.Data.Import import DataTableDataSource

#Source Data Table

sourceDataTable= Document.Data.Tables["NEW_CONTROL_LIMIT"]

#Mark rows on the source

dataSelection=Document.ActiveMarkingSelectionReference
dataSource=DataTableDataSource(Document.Data.Tables["NEW_CONTROL_LIMIT"],dataSelection)

#Copy rows to new data table
destinationDataTable=Document.Data.Tables["USER_CONTROL_LIMIT"]
rowsettings=AddRowsSettings(destinationDataTable,dataSource)
destinationDataTable.AddRows(dataSource,rowsettings)
