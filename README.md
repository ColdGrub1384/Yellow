# Yellow
## Programming language
<img src="https://raw.githubusercontent.com/ColdGrub1384/Yellow/master/logo.png" width="300"></img><br/>
![Dependecies](https://img.shields.io/badge/Dependecies-Python-blue.svg)<br/>
![Compilation](https://img.shields.io/badge/Compilation-don't%20need-green.svg)<br/>
![Platforms](https://img.shields.io/badge/Platforms-macOS%20%2F%20Linux-red.svg)<br/>
![Windows](https://img.shields.io/badge/Run%20on%20Windows-From%20Python%20script-yellow.svg)

## Installation
### Mac
    $ git clone https://github.com/ColdGrub1384/Yellow.git; Yellow/Build_for_Mac;
### Linux
    $ git clone https://github.com/ColdGrub1384/Yellow.git; Yellow/Build_for_Linux;
    
### Windows
Yellow is not coded for Windows, but if you modify scripts for Windows, you can run them as Python script:<br/>
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

    console {
        "Hello World from Yellow "+_version
    }
    \\n
    name = keyboard{
        "What's your name? "
    }

    log{
        "Question asked!"
    }

    Logclose{}

    from sys import platform
    if {platform == "linux" or platform == "linux2" or platform == "darwin"}:
        ${"clear"}
    else:
        ${"cls"}

    if {name == "Adrian"}:
        console.okGreen {
            "We have the same name!"
        }
    else:
        if {name == "Windows"}:
            console.failed {
                "Fuck you"
            }
        
        else:
            console.okBlue {
                "My name is Adrian"
            }
 
    console{_LOG}

    LOGFILE = open{
        _LOG,"r"
    }

    console {
        "LOG:\n"+LOGFILE.read{}
    }
    
    \\n
    \\n
    print{"1 != 1"}
    print{"This is a second line of code in a condition"}
     
