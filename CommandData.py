import os
import subprocess
import sys

class CommandData:
  branch: str = subprocess.run(["git", "branch", "--show-current"], capture_output=True).stdout.decode(sys.stdout.encoding).strip()
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
    return f"branch: {self.branch}"\
    + f"\ncommand: {self.command}"\
    + f"\nslot: {self.slot}"\
    + f"\ndirectory: {self.directory}"\
    + f"\nallFlag: {self.allFlag}"\
    + f"\nbranchFlag: {self.branchFlag}"\
    + f"\nhelpFlag: {self.helpFlag}"\
    + f"\nslotsFlag: {self.slotsFlag}"\
    + f"\nstackFlag: {self.stackFlag}"\
    + f"\ntopFlag: {self.topFlag}"