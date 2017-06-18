# ModularProgramming
A new way to code projects, just add your generalized algorithms once in your algo database and just call them to insert them into your code!
Only work left is adapting the functions name and maybe tweaking the way you sort your data!

## Features

-  Once you have coded an algorithm, you won't have to recode it anymore
-  It is language-independent, just bind a some file extension to a specific language and you're done
-  Now you can even code complex algorithm by including some other algorithms in the first line of your file
-  The client and server can be on different machines, just update the server ip from the client 
side
- Can communicate any size of algorithm (make full and functional parts of programs easily now!)

### What is coming next?

-  ---Support for LARGE source codes--- *DONE*
-  Stand-alone database server to separate client query management from actual database queries
-  Configurable caching system to optimize performance and memory usage on large databases
-  Moar languages implemented (just ask if you need a specific one, it's quick to add)
-  Adding more algorithms to the database (you can contribute too!)
-  Maybe linux support if there is interest in such a feature

## What do I need in order to use it?

-  **AHK** in order to run the client on windows
-  **python 3+**


# How does it works?

## Server-side

### Starting the server

Well, there's a **start_server.py** you just need to execute in order to start the server.
That's it!

### Stopping the server

Just access to the server terminal and press **Ctrl + C** in order to terminate the server

## The Database

### How do I fill my database?

the database is the algorithms folder of this tool, it is used in the following format:

***type_of_algorithm/specific_version.language_extension***

Please make sure you type it in lower case, place your files directly in the database and you're done!
You don't even need to restart, your files are already accessible.

### How do I include another algorithm from the database in my big algorithm?

just add this on the **FIRST** line of your file:

***needs type/specific.extension***

Make sure you're referring to the right algorithm and add any other one next to the first in the same fashion to include it.

## Client-side

### Starting the client

Execute the **start_client.ahk** to start the keyboard hook and register the Shift + Space hotkey

### Using the client

Type on your favourite editor, then type your request like this:

***<type of algorithm> <specific version> <language used>***
ie: **"sort simple python"** will fetch the **sort/simple.py** algorithm in the database if it is present.

Then select your request and type **Shift + Space**, that's it!

### Exiting the client

Use the hotkey **Shift + Esc** to terminate the client!

## Any questions?

Feel free to ask some questions by contacting me at **christopher.jacquiot@gmail.com** if you ever need help or want to
use this tool for your business, I'd be glad to help you!
