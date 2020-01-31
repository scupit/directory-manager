import subprocess

class CommandData:
  branch: str = subprocess.run(["git", "branch", "--show-current"], capture_output=True).stdout
  command: str = "--help"
  slot = None
  directory: str = os.getcwd()

  allFlag: bool = False
  branchFlag: bool = False
  helpFlag: bool = False
  slotsFlag: bool = False
  stackFlag: bool = False
  topFlag: bool = False

  def __str__(self):
    return f"command: {self.command}"\
    + f"\nslot: {self.slot}"\
    + f"\ndirectory: {self.directory}"\
    + f"\nallFlag: {self.allFlag}"\
    + f"\nslotsFlag: {self.slotsFlag}"\
    + f"\nstackFlag: {self.stackFlag}"\
    + f"\ntopFlag: {self.topFlag}"