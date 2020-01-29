from Globals import numStackSlots, numSlots, slotPrefix, stackSlotPrefix
import HistoryParser

class HistoryData:
  slots = []
  stackSlots = []

  def allSlotsAsString(self) -> str:
    result = ""
    for i in range(0, numSlots):
      result += self.slotString(i)
      if i != numSlots - 1:
        result += '\n'
    return result

  def allStackSlotsAsString(self) -> str:
    result = ""
    for i in range(0, numStackSlots):
      result += self.stackSlotString(i)
      if i != numStackSlots - 1:
        result += '\n'
    return result

  def slotString(self, index: int) -> str:
    return f"{slotPrefix}{index}: {self.slots[index] if index < len(self.slots) else ''}"

  def stackSlotString(self, index: int) -> str:
    return f"{stackSlotPrefix}{index}: {self.stackSlots[index] if index < len(self.stackSlots) else ''}"

  def popStackSlot(self) -> str:
    if len(self.stackSlots) == 0:
      return ""
    else:
      mostRecentStackSlot = self.stackSlots[0]
      newStackSlots = []

      for i in range(1, len(self.stackSlots)):
        newStackSlots.append(self.stackSlots[i])

      self.stackSlots = newStackSlots
      return mostRecentStackSlot

  def pushStackSlot(self, directory: str):
    if len(self.stackSlots) == 0:
      self.stackSlots.append(directory)
    # This can be shortened, but is much more readable this way
    elif len(self.stackSlots) + 1 <= numStackSlots:
      self.stackSlots = [directory] + self.stackSlots
    else:
      self.stackSlots.pop()
      self.stackSlots = [directory] + self.stackSlots
