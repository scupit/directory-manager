import HistoryParser

class History():
  def __enter__(self):
    self.dataItem = HistoryParser.getHistory()
    return self.dataItem

  def __exit__(self, type, value, traceBack):
    HistoryParser.writeHistory(self.dataItem)
