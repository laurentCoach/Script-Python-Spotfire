#Laurent Cesaro
#Date 17/03/2017
#Create a calculated column

#Import librarie
from Spotfire.Dxp.Data import CalculatedColumn

#Select your table
cols = Document.Data.Tables["MyTable"].Columns

#Define column name and expression
cols.AddCalculatedColumn("ThisIsACalculatedColumn", "Expression")
