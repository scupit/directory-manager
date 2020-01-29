from CommandData import CommandData
import HistoryParser

def pop(commandInfo: CommandData):
  data = HistoryParser.getHistory()
  mostRecentStackSlot = data.popDefaultSlot()
  HistoryParser.writeHistory(data)
  print(mostRecentStackSlot)