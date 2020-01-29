from CommandData import CommandData
import HistoryParser
from Globals import numDefaultSlots, numSlots

def pop(commandInfo: CommandData):
  data = HistoryParser.getHistory()
  mostRecentStackSlot = data.popDefaultSlot()
  HistoryParser.writeHistory(data)
  print(mostRecentStackSlot)

def save(commandInfo: CommandData):
  data = HistoryParser.getHistory()

  if commandInfo.slot is None:
    data.pushDefaultSlot(commandInfo.directory)
    print(commandInfo.directory, "saved to top of stack")
  elif commandInfo.slot >= 0 and commandInfo.slot < numSlots:
    data.slots[commandInfo.slot] = commandInfo.directory
    print(commandInfo.directory, "saved to save slot", commandInfo.slot)
  else:
    print("Slot must be between 0 and", numSlots)

    