from CommandData import CommandData
import HistoryParser
from Globals import numDefaultSlots, numSlots

# TODO: If help flag is set, call the corresponding command help function

def slotIsValidIndex(slot: int) -> bool:
  return slot >= 0 and slot < numSlots

def pop(commandInfo: CommandData):
  data = HistoryParser.getHistory()
  mostRecentStackSlot = data.popDefaultSlot()
  print(mostRecentStackSlot)
  HistoryParser.writeHistory(data)

def save(commandInfo: CommandData):
  data = HistoryParser.getHistory()

  if commandInfo.slot is None:
    data.pushDefaultSlot(commandInfo.directory)
    print(commandInfo.directory, "saved to top of stack")
  elif slotIsValidIndex(commandInfo.slot):
    data.slots[commandInfo.slot] = commandInfo.directory
    print(commandInfo.directory, "saved to save slot", commandInfo.slot)
  else:
    print("Slot must be between 0 and", numSlots)
  
  HistoryParser.writeHistory(data)
    
def show(commandInfo: CommandData):
  data = HistoryParser.getHistory()

  if commandInfo.stackFlag:
    if commandInfo.topFlag:
      print(data.defaultSlots[0])
    else:
      print(data.allDefaultSlotsAsString)
  elif commandInfo.slot is None:
    print(data.allSlotsAsString)
  elif slotIsValidIndex(commandInfo.slot):
    print(data.slots[commandInfo.slot])
  else:
    print("Slot must be between 0 and", numSlots)