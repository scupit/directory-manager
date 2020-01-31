from CommandData import CommandData
from History import History
from Globals import numStackSlots, numSlots

# TODO: If help flag is set, call the corresponding command help function

def isValidSlotIndex(slot: int) -> bool:
  return slot >= 0 and slot < numSlots

def isValidStackSlotIndex(slot: int) -> bool:
  return slot >= 0 and slot < numStackSlots

def printTop(data):
  print(data.stackSlots[0])

def clear(commandInfo: CommandData):
  with History() as data:
    if commandInfo.allFlag:
      data.clearDefaultSlot()
      data.stackSlots.clear()
      data.slots.clear()
      print("Cleared slots, default space, and stack")
    else:
      if (commandInfo.slotsFlag):
        if commandInfo.slot is None:
          data.slots.clear()
          print("Cleared all slots")
        elif isValidSlotIndex(commandInfo.slot):
          data.clearSlot(commandInfo.slot)
          print("Cleared slot", commandInfo.slot)
        else:
          print("Slot must be between 0 and", numSlots - 1)
      elif commandInfo.stackFlag:
        data.stackSlots.clear()
        print("Cleared stack")
      else:
        data.clearDefaultSlot()
        print("Cleared default space")

def pop(commandInfo: CommandData):
  with History() as data:
    mostRecentStackSlot = data.popStackSlot()
    print(mostRecentStackSlot)

def push(commandInfo: CommandData):
  with History() as data:
    if commandInfo.branchFlag:
      data.pushStackSlot(commandInfo.branch)
      print("Branch", commandInfo.branch, "saved to top of stack")
    else:
      data.pushStackSlot(commandInfo.directory)
      print("Directory", commandInfo.directory, "saved to top of stack")

def save(commandInfo: CommandData):
  with History() as data:
    if commandInfo.slot is None:
      if commandInfo.branchFlag:
        data.defaultSlot = commandInfo.branch
        print("Branch", commandInfo.branch, "saved to the default space")
      else:
        data.defaultSlot = commandInfo.directory
        print("Directory", commandInfo.directory, "saved to the default space")
    elif isValidSlotIndex(commandInfo.slot):
      if commandInfo.branchFlag:
        data.slots[commandInfo.slot] = commandInfo.branch
        print("Branch", commandInfo.branch, "saved to save slot", commandInfo.slot)
      else:
        data.slots[commandInfo.slot] = commandInfo.directory
        print("Directory", commandInfo.directory, "saved to save slot", commandInfo.slot)
    else:
      print("Slot must be between 0 and", numSlots - 1)

def show(commandInfo: CommandData):
  with History() as data:
    if commandInfo.allFlag:
      print("---Default Slot---")
      print(data.defaultSlotString())
      print("\n\n---Slots---")
      print(data.allSlotsAsString())
      print("\n\n---Stack---")
      print(data.allStackSlotsAsString())
    else:
      if commandInfo.stackFlag:
        if commandInfo.topFlag:
          printTop(data)
        elif not commandInfo.slot is None and isValidStackSlotIndex(commandInfo.slot):
          print(data.stackSlots[commandInfo.slot])
        else:
          print(data.allStackSlotsAsString())
      elif commandInfo.slotsFlag:
        if commandInfo.slot is None:
          print(data.allSlotsAsString())
        else:
          if isValidSlotIndex(commandInfo.slot):
            print(data.slots[commandInfo.slot])
          else:
            print("Slot must be between 0 and", numSlots - 1)
      else:
        print(data.defaultSlot)

def top(commandInfo: CommandData):
  with History() as data:
    printTop(data)