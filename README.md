<center>
# Yellow
## Programming language
<img src="/Users/adrian/Desktop/Yellow/logo.png" width="300"><br/>
![Dependecies](https://img.shields.io/badge/dependecies-Python-blue.svg)<br/>
![Compilation](https://img.shields.io/badge/Compilation-don't%20need-green.svg)<br/>
![Platforms](https://img.shields.io/badge/Platforms-macOS%20%2F%20Linux-red.svg)<br/>
![Windows](https://img.shields.io/badge/Run%20on%20Windows-From%20Python%20script-yellow.svg)
</center>

## Installation
### Mac
    $ git clone https://github.com/ColdGrub1384/Yellow.git; cd Yellow; ./Build_for_Mac;
### Linux
    $ git clone https://github.com/ColdGrub1384/Yellow.git; cd Yellow; ./Build_for_Linux;
    
### Windows
Clone repository, open ```Yellow``` and remove ```#!/usr/bin/python```, then you can rename ```Yellow``` to ```Yellow.py``` and run it with Python.<br/>
NOTE: Yellow\_Shell command is not avaible for Windows, but you can use ```python [path_to_Yellow] -s``` to open it.
## Usage
### Translate to Python and create executable
    $ Yellow -t [path to yellow file] [path to new file including name]
### Shell
    $ Yellow -s
    # OR:
    $ Yellow_Shell
    
    
## Code example
    // Comment

    /* Multiline
    comment*/

    print {
        "Hello World"
    }

    if {1 == 1}:
        print{"1 == 1"}
        print{"This is a second line of code in a condition"}
    else:
        print{"1 != 1"}
        print{"This is a second line of code in a condition"}
     