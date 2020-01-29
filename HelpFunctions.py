import sys

def general():
  argName = sys.argv[0]
  print(f"{argName} [--help]")
  print(f"{argName} clear [--stack] [-s slotIndex]")
  print(f"{argName} pop")
  print(f"{argName} push [-d directory]")
  print(f"{argName} save [-s slotIndex] [-d directory]")
  print(f"{argName} show [--stack [--top]] [-s slotIndex]")

  # TODO: Implement help functions for each command  