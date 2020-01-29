import os

class CommandData:
  command: str = "--help"
  slot = None
  directory: str = os.getcwd()

  helpFlag: bool = False
  stackFlag: bool = False

  def slotString(self):
    return "(Default Slot)" if self.slot is None else self.slot

  def __str__(self):
    return f"command: {self.command}\nslot: {self.slotString()}\ndirectory: {self.directory}\nhelpFlag: {self.helpFlag}"
