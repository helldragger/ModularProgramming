# ModularProgramming
A new way to code projects, just add your generalized algorithms once in your algo database and just call them to insert them into your code! only work left is adapting the functions name and maybe tweaking the way you sort your data!

## How will this work?

Simple! You add your algorithms in the algo database, sort them how you want, and when you need to call them, you will just have to write in your file the algorithm you need, select it, and use the hotkey Ctrl + Shift + A!
This program will then search if your selection is the path to a defined algorithm, if it is, it will replace by itself your selection with a copy of it!
Tadaa! No need to reinvent the wheel twice!

## Technically?

This is a simple implementation of an AHK client and a Python server communicating through TCP the server will query
it's own database at each client query and send back the data of the algorithm if any.
