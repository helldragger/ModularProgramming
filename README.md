# ModularProgramming
A new way to code projects, just add your generalized algorithms once in your algo database and just call them to insert them into your code! only work left is adapting the functions name and maybe tweaking the way you sort your data!

## Features

-  Once you have coded an algorithm, you won't have to recode it anymore
-  It is language-independent, just bind a some file extension to a specific language and you're done
-  Now you can even code complex algorithm by including some other algorithms in the first line of your file
-  The client and server can be on different machines, just update the server ip from the client 
side

### What is coming next?

-  Support for LARGE source codes (currently limited to 4 Ko per request)
-  Moar languages implemented (just ask if you need a specific one, it's quick to add)
-  Adding more algorithms to the database (you can contribute too!)

## What do I need in order to use it?

-  AHK in order to run the client on windows
-  ironAHK in order to run the client on linux (untested yet)
-  python 3+


## How does it works?

### Starting the server

Well, there's a start_server.py you just need to execute in order to start the server.
That's it!

### Stopping the server

Just access to the server terminal and press Ctrl + C in order to terminate the server

### Starting the client

Execute the start_client.ahk to start the keyboard hook and register the Shift + Space hotkey

### Using the client

Type on your favourite editor, then type your request like this:

<type of algorithm> <specific version> <language used>
ie: sorting simple python

Then select your request and type Shift + Space, that's it!

### Exiting the client

Use the hotkey Shift + Esc to terminate the client!

## How do I fill my database?

the database is the algorithms folder of this tool, it is used in the following format:

TYPE_OF_ALGORITHM/SPECIFIC_VERSION.LANGUAGE_EXTENSION

Please make sure you type it in upper case.


## Some questions?

Feel free to ask some questions by contacting me at christopher.jacquiot@gmail.com if you ever need help or want to
use this tool for your business, I'd be glad to help you!
