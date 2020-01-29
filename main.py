import sys
from ArgParser import parseArgs
import ArgFunctions
import HelpFunctions

if len(sys.argv) > 1:
  try:
    commandData = parseArgs(sys.argv)
  
    if commandData.command == '--help':
      HelpFunctions.general()
    elif commandData.command == "clear":
      ArgFunctions.clear(commandData)
    elif commandData.command == "pop":
      ArgFunctions.pop(commandData)
    elif commandData.command == "push":
      ArgFunctions.push(commandData)
    elif commandData.command == "save":
      ArgFunctions.save(commandData)
    elif commandData.command == "show":
      ArgFunctions.show(commandData)
    else:
      print("Invalid command, see --help for a command list")

  except ValueError as error:
    print(str(error))

else:
  HelpFunctions.general()
