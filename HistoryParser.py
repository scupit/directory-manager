import os
from Globals import historyFileName, numDefaultSlots, numSlots
from HistoryData import HistoryData

def writeSlots(historyFile, data: HistoryData):
  for i in range(0, numSlots):
    historyFile.write(data.slotString(i) + '\n')

def writeDefaultSlots(historyFile, data: HistoryData):
  for i in range(0, numSlots):
    historyFile.write(data.defaultSlotString(i) + '\n')

def writeHistory(data: HistoryData):
  with open(historyFileName, 'w') as historyFile:
    writeSlots(historyFile, data)
    writeDefaultSlots(historyFile, data)

def createEmptyHistory():
  writeHistory(HistoryData())

def extractPath(fullSlot: str) -> str:
  colonIndex = fullSlot.find(':')
  return "" if colonIndex == -1 or colonIndex == len(fullSlot) -1 else line[colonIndex + 1:]

def getHistory() -> HistoryData:
  if not os.path.exists(historyFileName):
    createEmptyHistory()

  data = HistoryData()

  with open(historyFileName, 'r') as historyFile:
    line = ""
    while not historyFile.closed:
      line = historyFile.readline()

      if line[0] == 's' and len(data.slots) < numSlots:
        data.slots.append(extractPath(line))
      elif line[0] == 'd' and len(data.defaultSlots) < numDefaultSlots:
        data.defaultSlots.append(extractPath(line))
  return data