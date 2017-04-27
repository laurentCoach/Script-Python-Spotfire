#Laurent Cesaro

#-----------------------------------------------------------------#
# Scipt python to refresh a table with a button					  #
#1 - Add in script Parameters the table whch will be refresh	  #
#2 - Include a try-except to manage error						  #
#3 - Include NameScriptParametersOfTheTable.refresh				  #
#-----------------------------------------------------------------#


try:
  Table.Refresh()  
except:
  raise Exception("Error")