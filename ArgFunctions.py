from CommandData import CommandData
import HistoryParser
from Globals import numDefaultSlots, numSlots

# TODO: If help flag is set, call the corresponding command help function

def isValidSlotIndex(slot: int) -> bool:
  return slot >= 0 and slot < numSlots

def isValidStackSlotIndex(slot: int) -> bool:
  return slot >= 0 and slot < numDefaultSlots

def pop(commandInfo: CommandData):
  data = HistoryParser.getHistory()
  mostRecentStackSlot = data.popDefaultSlot()
  print(mostRecentStackSlot)
  HistoryParser.writeHistory(data)

def push(commandInfo: CommandData):
  data = HistoryParser.getHistory()
  data.pushDefaultSlot(commandInfo.directory)
  print(commandInfo.directory, "saved to top of stack")
  HistoryParser.writeHistory(data)

def save(commandInfo: CommandData):
  data = HistoryParser.getHistory()

  if commandInfo.slot is None:
    data.pushDefaultSlot(commandInfo.directory)
    print(commandInfo.directory, "saved to top of stack")
  elif isValidSlotIndex(commandInfo.slot):
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
    elif not commandInfo.slot is None and isValidStackSlotIndex(commandInfo.slot):
      print(data.defaultSlots[commandInfo.slot])
    else:
      print(data.allDefaultSlotsAsString())
  elif commandInfo.slot is None:
    print(data.allSlotsAsString())
  elif isValidSlotIndex(commandInfo.slot):
    print(data.slots[commandInfo.slot])
  else:
    print("Slot must be between 0 and", numSlots)