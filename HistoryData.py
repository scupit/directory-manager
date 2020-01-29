from Globals import numDefaultSlots, numSlots
import HistoryParser

class HistoryData:
  slots = []
  defaultSlots = []

  def allSlotsAsString(self) -> str:
    result = ""
    for i in range(0, numSlots):
      result += data.slotString(i)
      if i != numSlots - 1:
        result += '\n'
    return result

  def allDefaultSlotsAsString(self) -> str:
    result = ""
    for i in range(0, numDefaultSlots):
      result += self.defaultSlotString(i)
      if i != numDefaultSlots - 1:
        result += '\n'
    return result

  def slotString(self, index: int) -> str:
    return f"s{index}:{self.slots[index] if index < len(self.slots) else ''}"

  def defaultSlotString(self, index: int) -> str:
    return f"d{index}:{self.defaultSlots[index] if index < len(self.defaultSlots) else ''}"

  def popDefaultSlot(self) -> str:
    if len(self.defaultSlots) == 0:
      return ""
    else:
      mostRecentStackSlot = self.defaultSlots[0]
      newStackSlots = []

      for i in range(1, len(self.defaultSlots)):
        newStackSlots.append[self.defaultSlots[i]]

      self.defaultSlots = newStackSlots
      return mostRecentStackSlot

  def pushDefaultSlot(self, directory: str):
    if len(self.defaultSlots) == 0:
      self.defaultSlots.append(directory)
    # This can be shortened, but is much more readable this way
    elif len(self.defaultSlots) + 1 <= numDefaultSlots:
      self.defaultSlots = [directory] + self.defaultSlots
    else:
      self.defaultSlots.pop()
      self.defaultSlots = [directory] + self.defaultSlots
