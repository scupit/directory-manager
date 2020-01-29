import sys
from ArgParser import parseArgs
import ArgFunctions
import HelpFunctions

if len(sys.argv) > 1:
  try:
    commandData = parseArgs(sys.argv)
    print(str(commandData))
  
    # if commandData.command == '--help':
    #   HelpFunctions.general()
    # elif commandData.command == "load":
    #   ArgFunctions.load(commandData)
    # elif commandData.command == "save":
    #   ArgFunctions.save(commandData)
    # elif commandData.command == "history":
    #   ArgFunctions.history(commandData)
    # elif commandData.command == "slots":
    #   ArgFunctions.slots(commandData)
    # else:
    #   print("Invalid command, see --help for a command list")

  except ValueError as error:
    print(str(error))

else:
  HelpFunctions.general()
