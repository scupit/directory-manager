from CommandData import CommandData
from History import History
from Globals import numStackSlots, numSlots

# TODO: If help flag is set, call the corresponding command help function

def isValidSlotIndex(slot: int) -> bool:
  return slot >= 0 and slot < numSlots

def isValidStackSlotIndex(slot: int) -> bool:
  return slot >= 0 and slot < numStackSlots

def clear(commandInfo: CommandData):
  with History() as data:
    if commandInfo.allFlag:
      data.stackSlots.clear()
      data.slots.clear()
      print("Cleared slots and stack")
    elif commandInfo.stackFlag:
      data.stackSlots.clear()
      print("Cleared stack")
    elif not commandInfo.slot is None and isValidSlotIndex(commandInfo.slot):
      data.slots[commandInfo.slot] = ""
      print("Cleared slot", commandInfo.slot)
    else:
      data.slots.clear()
      print("Cleared all slots")

def pop(commandInfo: CommandData):
  with History() as data:
    mostRecentStackSlot = data.popStackSlot()
    print(mostRecentStackSlot)

def push(commandInfo: CommandData):
  with History() as data:
    data.pushStackSlot(commandInfo.directory)
    print(commandInfo.directory, "saved to top of stack")

def save(commandInfo: CommandData):
  with History() as data:
    if commandInfo.slot is None:
      data.pushStackSlot(commandInfo.directory)
      print(commandInfo.directory, "saved to top of stack")
    elif isValidSlotIndex(commandInfo.slot):
      data.slots[commandInfo.slot] = commandInfo.directory
      print(commandInfo.directory, "saved to save slot", commandInfo.slot)
    else:
      print("Slot must be between 0 and", numSlots - 1)

def show(commandInfo: CommandData):
  with History() as data:
    if commandInfo.allFlag:
      print("---Slots---")
      print(data.allSlotsAsString())
      print("\n\n---Stack---")
      print(data.allStackSlotsAsString())
    elif commandInfo.stackFlag:
      if commandInfo.topFlag:
        print(data.stackSlots[0])
      elif not commandInfo.slot is None and isValidStackSlotIndex(commandInfo.slot):
        print(data.stackSlots[commandInfo.slot])
      else:
        print(data.allStackSlotsAsString())
    elif commandInfo.slot is None:
      print(data.allSlotsAsString())
    elif isValidSlotIndex(commandInfo.slot):
      print(data.slots[commandInfo.slot])
    else:
      print("Slot must be between 0 and", numSlots - 1)