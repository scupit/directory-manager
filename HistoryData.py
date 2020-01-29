import HistoryParser

class HistoryData:
  slots = []
  defaultSlots = []

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
