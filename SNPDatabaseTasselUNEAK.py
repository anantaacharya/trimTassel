#written by ananta acharya
#ananta@uga.edu

#please credit if you use this tool

import time
from itertools import izip, imap
import operator
import commontools
def main():

    opt=raw_input("what do you want to do? \n 1. Make database from Tassel Fasta \n 2. Merge new fasta to database\n\n 3. Search against Database\n")
    if opt=="1":
        firstFasta=raw_input("*.fas.txt")
        name=raw_input("Name of this fasta TP, used in database properties")
        database=raw_input("Database name and location to make")
        makedatabase(firstFasta, database, name)
    elif opt=="2":
        print "not implemented at this time"
##        database=raw_input("Where is the database")
##        newFasta=raw_input("Which file  Merge")
##        
##        mergedatabase(database, newFasta)
    elif opt=="3":
        
        database=raw_input("Where is the database")
        newFasta=raw_input("Which file to serch against and Merge")
        OutFile=raw_input("where to erite results?")
        searchdatabasedirect(database, newFasta, OutFile)
        
    else:
        print "Not valid option"
        


def extractFasta(infile):
    """Make dictionary of Tagpairs names and seqs"""
    
    inf=open(infile,"r")
    count=0
    eachline=1
    SNPdict=dict()

    for line in inf:
        count+=1
        
        if eachline==1:
            TP=line.strip().split("|")[0][1::]
            eachline=2
            
        elif eachline==2:
                        
            seq=line.strip()


            SNPdict[TP]=seq
            eachline=1    
    inf.close()
    return SNPdict            
   
def swapdict(dd):
    """Swaps keys and values of dict"""
    d2=dict((value.strip(), key.strip()) for key, value in dd.iteritems())
    return d2      
        
def makedatabase(firstFasta, database, name):
    
    SNPdict=extractFasta(firstFasta)
            
    with open(database,"a") as databaseout:
        for key in sorted(SNPdict.iterkeys()):
            databaseout.write(key+"\t"+SNPdict[key]+"\t"+name)
            databaseout.write("\n")
    print str(len(SNPdict))+" SNPs are added to "+database     

def mergedatabase(database, newFasta):
    pass  


def searchdatabasedirect(database, newFasta, outFasta):
    matchdict=dict()
    matchdict2=dict()
    SNPdict=dict()
    SNPdictNew=dict()
    start=time.time()
    databasein=open(database,"r")
    for line in databasein:
        linelist=line.strip().split("\t")
        SNPdict[linelist[1].strip()]=linelist[0]
        
    databasein.close()
    
    
    
    newSNPdict=swapdict(extractFasta(newFasta))
    
    
    
    same=set.intersection(set(newSNPdict.keys()),set(SNPdict.keys()))
    
    print str(len(newSNPdict))+"items searched\n"
    print str(len(same))+"items found\n"
    print str(len(newSNPdict)-len(same))+"items not found\n"
    for item in same:
        matchdict[SNPdict[item]]=(newSNPdict[item],item)
                  
    with open(outFasta,"a") as outFastaout:
        for key in sorted(matchdict.iterkeys()):
            outFastaout.write(key+"\t"+matchdict[key][0]+"\t"+matchdict[key][1])
            outFastaout.write("\n")
  
    print str(len(matchdict))+" SNPs are matched to "+database
    print "matched SNPs written in"+outFasta
   
  

    
        

main()
