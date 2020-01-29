import os

class CommandData:
  command: str = "--help"
  slot = None
  directory: str = os.getcwd()

  allFlag: bool = False
  helpFlag: bool = False
  stackFlag: bool = False
  topFlag: bool = False

  def slotString(self):
    return "(Stack Slot)" if self.slot is None else self.slot

  def __str__(self):
    return f"command: {self.command}\nslot: {self.slotString()}\ndirectory: {self.directory}\nhelpFlag: {self.helpFlag}"
