#Laurent Cesaro

#Import library
from Spotfire.Dxp.Data import RowSelection, IndexSet

selection   = IndexSet(dt.RowCount,True)
for r in selection:
   selection[r] = (r<=100)

 #delete rows based on selection (rows from indexset marked as true)
dt.RemoveRows(RowSelection(selection)) 