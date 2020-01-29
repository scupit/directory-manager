import sys

def general():
  argName = sys.argv[0]
  print(f"{argName} [--help]")
  print(f"{argName} clear [--all] [--stack] [--slots [-s slotIndex]]")
  print(f"{argName} pop")
  print(f"{argName} push [-d directory]")
  print(f"{argName} save [-s slotIndex] [-d directory]")
  print(f"{argName} show [--all] [--stack [--top]] [--slots [-s slotIndex]]")
  print(f"{argName} top")
  # TODO: Implement help functions for each command  