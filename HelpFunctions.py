import sys

def general():
  argName = sys.argv[0]
  print(f"{argName} pop")
  print(f"{argName} save [-s slotIndex] [-d directory]")
  print(f"{argName} show [--stack] [-s slotIndex]")
  print(f"{argName} --help")
  