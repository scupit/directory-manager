from pathlib import Path
from CommandData import CommandData

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
    elif args[i] == "-d":
      output.directory = str(Path(args[i + 1]).resolve())
      shouldSkipNextArg = True
    elif args[i] == "--help":
      output.helpFlag = True
    elif args[i] == "--stack":
      output.stackFlag = True
    elif args[i] == "--top":
      output.topFlag = True
    else:
      raise ValueError(f"Invalid argument {args[i]} given.")

  return output