from pathlib import Path
from CommandData import CommandData

def isFlag(arg: str) -> bool:
  return arg[0] == '-'

def nextArgExists(index: int, args: list) -> bool:
  return index < len(args) - 1

def parseArgs(args):
  numArgs = len(args)
  output = CommandData()

  if numArgs > 1:
    output.command = args[1]

  shouldSkipNextArg = False

  for i in range(2, numArgs):
    if (shouldSkipNextArg):
      shouldSkipNextArg = False
      continue
    
    if args[i] == "-s":
      output.slot = int(args[i + 1])
      shouldSkipNextArg = True
    elif args[i] == "-b":
      output.branchFlag = True
      # Giving a branch to -b is optional
      if nextArgExists(i, args) and not isFlag(args[i + 1]):
        output.branch = args[i + 1]
        shouldSkipNextArg = True
    elif args[i] == "-d":
      output.directory = str(Path(args[i + 1]).resolve())
      shouldSkipNextArg = True
    elif args[i] == "--all":
      output.allFlag = True
    elif args[i] == "--help":
      output.helpFlag = True
    elif args[i] == "--slots":
      output.slotsFlag = True
    elif args[i] == "--stack":
      output.stackFlag = True
    elif args[i] == "--top":
      output.topFlag = True
    else:
      raise ValueError(f"Invalid argument {args[i]} given.")

  return output