import os
from pathlib import Path
import sys

# For easy access and changing
historyFileBaseName = "directory_history.txt"

# Used
historyFileName = str(Path(os.path.dirname(os.path.realpath(sys.argv[0]))) / historyFileBaseName)
numSlots = 10
numStackSlots = 10

defaultSlotPrefix = "default slot"
slotPrefix = "slot"
stackSlotPrefix = "stack"