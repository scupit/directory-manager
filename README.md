# Directory storage
A simple python CLI for storing and managing directory names and branches. Storage spaces include a
default slot, 10 slots, and a stack with 10 spaces.

## Why is this useful?
It allows you to store and manage directory names for later using several different methods.
This of it as a directory clipboard. You have one default space for quick use and swapping.
Then you also have 10 spaces which you assign and pull from individially. Finally you have
a directory stack.

## Possible Uses
* Wrap this functionality in a *load* script and easily `cd` between projects
* For memory, remember where your last few projects are
* For large projects, use this to remember some of the branches you are working on

# How to Run
`python main.py --help` will list how to use this script

## TODO
- [X] Make a version of this project for git branches. That would be great. (Done, with the same project)
- [ ] Maybe let this store any entered string, like a clipboard