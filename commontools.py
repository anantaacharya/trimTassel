#written by ananta acharya,
#ananta@uga.edu
#has some common utilities like file I/O and other Sequence related
#commontools.py
#may change time to time

import os
def OKtoRead(inputfile):
    """Checks whether the input file is readable"""
    if not os.path.exists(inputfile):
        print "File does not Exist"
        return False
    elif not os.path.isfile(inputfile):
        print "Is not a file"
        return False
   
    return True
    
def OKtoWrite(outputfile):
    """Checks whether the input file is writable"""
    if not os.path.exists(os.path.dirname(outputfile)):
        print "Path Does Not Exist"
        return False
    elif os.path.isdir(outputfile):
        print "Is not a file but folder"
        return False
    elif os.path.exists(outputfile):
        print "File already exists, Can not Overwite or Merge"
        return False
    else:
        return True

def IUPAC(n1,n2):

    listt=[n1.upper(),n2.upper()]

    if "A" in listt and "T" in listt:
        return "W"
    elif "A" in listt and "C" in listt:
        return "M"
    elif "A" in listt and "G" in listt:
        return "R"
    elif "C" in listt and "T" in listt:
        return "Y"
    elif "C" in listt and "G" in listt:
        return "S"
    elif "G" in listt and "T" in listt:
        return "K"
    else:
        return "N"
    


