import HistoryParser

class HistoryData:
  slots = []
  defaultSlots = []

  def slotString(self, index: int) -> str:
    return f"s{index}:{self.slots[index] if index < len(self.slots) else ""}"

  def defaultSlotString(self, index: int) -> str:
    return f"d{index}:{self.defaultSlots[index] if index < len(self.defaultSlots) else ""}"
