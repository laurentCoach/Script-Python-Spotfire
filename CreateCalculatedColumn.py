#Laurent Cesaro
#Date 17/03/2017
#Create a calculated column

from Spotfire.Dxp.Data import CalculatedColumn
cols = Document.Data.Tables["MyTable"].Columns
cols.AddCalculatedColumn("ThisIsACalculatedColumn", "Expression")