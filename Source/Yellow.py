#!/usr/bin/python

import sys
import py_compile
import os
import os.path
from os.path import expanduser

version = "1.1"
path = os.path.dirname(os.path.realpath(__file__))
shell = False

# Check for arguments
if (len(sys.argv) == 1):
    sys.exit ("\nUSAGE: [OPTION] [ARGUMENT]\n\nOPTIONS:\n\n-t: [file to translate] [file to create] Translate file and create executable\n-r: [file to run] Translate file and run it\n-s: Run Yellow Shell\n-v: Return version\n")
    
if (sys.argv[1] == "-v"):
    print version
    exit()
    
print "\nWelcome to Yellow programming language by ColdGrub1384"

# Open file
file = ""
if(sys.argv[1] != "-s"):
    file = sys.argv[2]
    file = open(file,"r").read()
else:
    file = file
    
if(sys.argv[1] != "-s"):
    print("Translating file...\n\n")
    
code = file.split("\n")

currentLine = 0

global translated
translated = ""

while (currentLine < len(code)):

    # Setup files
    home = expanduser("~")
    if (not os.path.exists(home+"/Library/Yellow/")):
        os.mkdir(home+"/Library/Yellow/")

    # Shell
    if(sys.argv[1] == "-s"):
        code = ["",""]
        currentLine = 0
        code[currentLine] = raw_input("-> ")

    if (True):
    
                 
        # Translate

        if(sys.argv[1] == "-s"):
            colors = open(path+"/PYClasses/Colors.py","r")
            code[currentLine] = colors.read()+"\n\n"+code[currentLine]
    
        withoutSpace = code[currentLine].replace(" ","");
        if (withoutSpace.startswith("//")):
            code[currentLine] = ""
    
        # Comments
        code[currentLine] = code[currentLine].replace("/*","'''")
        code[currentLine] = code[currentLine].replace("*/","'''")
    
        # Syntax
    
        code[currentLine] = code[currentLine]+"\n"
    
        if (code[currentLine].endswith("{") and code[currentLine+1].startswith("    ")):
            code[currentLine+1] = code[currentLine+1].replace("    ","")
    
        if (code[currentLine].endswith("}") or code[currentLine].endswith("{")):
            if (code[currentLine+1].startswith("else")):
                print ""
            else:
                if (code[currentLine+1].startswith("    ")):
                    code[currentLine] = code[currentLine]+"; "+code[currentLine+1]
                    code[currentLine+1] = ""
                else:
                    code[currentLine] = code[currentLine]+code[currentLine+1]
                    code[currentLine+1] = ""
        
                if (currentLine+2 < len(code)):
                    if (code[currentLine+2].startswith("}")):
                        code[currentLine] = code[currentLine]+code[currentLine+2]                 
                        code[currentLine+2] = ""
                    
        code[currentLine] = code[currentLine].replace("{","(")
        code[currentLine] = code[currentLine].replace("}",")")
    
        # Functions / Variables
        code[currentLine] = code[currentLine].replace("console","print")
        code[currentLine] = code[currentLine].replace("keyboard","raw_input") 
        code[currentLine] = code[currentLine].replace("_version","\""+version+"\"")
        code[currentLine] = code[currentLine].replace(repr("\\n").replace("'",""),"print \"\\n\"")
        code[currentLine] = code[currentLine].replace("\print","print")
        code[currentLine] = code[currentLine].replace("$","import os; os.system")
    
        if (sys.argv[1] != "-s"):
            code[currentLine] = code[currentLine].replace("log","from os.path import expanduser;logfile = open(expanduser(\"~\")+\"/Library/Yellow/"+os.path.basename(sys.argv[2])+"-log.txt"+"\",\"w+\"); logfile.write")

            code[currentLine] = code[currentLine].replace("_LOG","\""+home+"/Library/Yellow/"+os.path.basename(sys.argv[2])+"-log.txt"+"\"")
    
        code[currentLine] = code[currentLine].replace("Logclose","logfile.close")

        ## Colors
        code[currentLine] = code[currentLine].replace("print.header","header")
        code[currentLine] = code[currentLine].replace("print.okBlue","okBlue")          
        code[currentLine] = code[currentLine].replace("print.okGreen","okGreen")
        code[currentLine] = code[currentLine].replace("print.warning","warning")
        code[currentLine] = code[currentLine].replace("print.failed","failed")          
        code[currentLine] = code[currentLine].replace("print.bold","bold")
        code[currentLine] = code[currentLine].replace("print.underline","underline")
    
        # Encodage
        code[currentLine] = code[currentLine].replace("\{","{")
        code[currentLine] = code[currentLine].replace("\}","}")
    
        if(sys.argv[1] == "-s"):
             exec code[currentLine]
        translated = translated+"\n"+code[currentLine]
        currentLine = currentLine+1
            
                    

# Check for arguments
if (shell == False):
    for option in sys.argv:
        if(option == "-t"):
            script = open(sys.argv[3],"w+")
            colors = open(path+"/PYClasses/Colors.py","r")
            script.write("#!/usr/bin/python\n"+colors.read()+"\n"+translated)
            os.chmod(sys.argv[3], 0o777)

        if(option == "-r"):
            colors = open(path+"/PYClasses/Colors.py","r")
            translated = colors.read()+"\n\n"+translated
            exec translated
                        
                
