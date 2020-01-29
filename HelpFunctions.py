import sys

def general():
  argName = sys.argv[0]
  print(f"{argName} save [-s slotNumber] [-d directory]")
  print(f"{argName} load [-s slotNumber] [-d directory]")
  print(f"{argName} history [-s historyIndex]")
  print(f"{argName} slots [-s slotNumber]")
  print(f"{argName} --help")
  