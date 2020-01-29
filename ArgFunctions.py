from CommandData import CommandData
from History import History
from Globals import numDefaultSlots, numSlots

# TODO: If help flag is set, call the corresponding command help function

def isValidSlotIndex(slot: int) -> bool:
  return slot >= 0 and slot < numSlots

def isValidStackSlotIndex(slot: int) -> bool:
  return slot >= 0 and slot < numDefaultSlots

def clear(commandInfo: CommandData):
  with History() as data:
    if commandInfo.stackFlag:
      data.defaultSlots.clear()
    elif not commandInfo.slot is None and isValidSlotIndex(commandInfo.slot):
      data.slots[commandInfo.slot] = ""
    else:
      data.slots.clear()

def pop(commandInfo: CommandData):
  with History() as data:
    mostRecentStackSlot = data.popDefaultSlot()
    print(mostRecentStackSlot)

def push(commandInfo: CommandData):
  with History() as data:
    data.pushDefaultSlot(commandInfo.directory)
    print(commandInfo.directory, "saved to top of stack")

def save(commandInfo: CommandData):
  with History() as data:
    if commandInfo.slot is None:
      data.pushDefaultSlot(commandInfo.directory)
      print(commandInfo.directory, "saved to top of stack")
    elif isValidSlotIndex(commandInfo.slot):
      data.slots[commandInfo.slot] = commandInfo.directory
      print(commandInfo.directory, "saved to save slot", commandInfo.slot)
    else:
      print("Slot must be between 0 and", numSlots - 1)

def show(commandInfo: CommandData):
  with History() as data:
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
      print("Slot must be between 0 and", numSlots - 1)