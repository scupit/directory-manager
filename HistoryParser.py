import os
from Globals import historyFileName, numStackSlots, numSlots, slotPrefix, stackSlotPrefix
from HistoryData import HistoryData

def writeHistory(data: HistoryData):
  with open(historyFileName, 'w') as historyFile:
    historyFile.write(data.allSlotsAsString())
    historyFile.write('\n')
    historyFile.write(data.allStackSlotsAsString())

def createEmptyHistory():
  writeHistory(HistoryData())

def extractPath(fullSlot: str) -> str:
  colonIndex = fullSlot.find(':')
  return "" if colonIndex == -1 or colonIndex == len(fullSlot) -1 else fullSlot[colonIndex + 1:].strip()

def getHistory(data = HistoryData()) -> HistoryData:
  if not os.path.exists(historyFileName):
    createEmptyHistory()

  with open(historyFileName, 'r') as historyFile:
    for line in historyFile:
      line = line.strip()

      if line.find(slotPrefix) == 0 and len(data.slots) < numSlots:
        data.slots.append(extractPath(line))
      elif line.find(stackSlotPrefix) == 0 and len(data.stackSlots) < numStackSlots:
        data.stackSlots.append(extractPath(line))
  return data