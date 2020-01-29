import os
from Globals import historyFileName, numDefaultSlots, numSlots
from HistoryData import HistoryData

def writeHistory(data: HistoryData):
  with open(historyFileName, 'w') as historyFile:
    historyFile.write(data.allSlotsAsString())
    historyFile.write('\n')
    historyFile.write(data.allDefaultSlotsAsString())

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
      if line[0] == 's' and len(data.slots) < numSlots:
        data.slots.append(extractPath(line))
      elif line[0] == 'd' and len(data.defaultSlots) < numDefaultSlots:
        data.defaultSlots.append(extractPath(line))
  return data