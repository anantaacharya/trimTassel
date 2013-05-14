#written by ananta acharya
#ananta@uga.edu

#please credit if you use this tool

#this takes the HapMap.fas.txt from UNEAK pipeline and writes a fasta file either just query or merging the query and hit with SNP position

import os
import commontools #this is another code written by me look for commontools.py

def main():
    infile=raw_input("fas.txt")
    while not commontools.OKtoRead(infile):
        infile=raw_input("fas.txt")
        
    outfile=raw_input("out")
    while not commontools.OKtoWrite(outfile):
        outfile=raw_input("out")
    method=raw_input("1: get trimmed fasta query seq only\n 2: get trimmed fasta with SNP ")
    while method not in ["1","2"]:
        method=raw_input("1: get trimmed fasta query seq only\n 2: get trimmed fasta with SNP ")
    if method=="1":
        
        print "processing"
        split(infile, outfile)
        print "finished"
    elif method=="2":
        
        print "processing"
        SNPposIUPAC(infile, outfile)
        print "finished"

def split(infile, outfile):
    """Gets the trimmed Query sequence """
    inf=open(infile,"r")
    count=0
    bufferw=""
    for line in inf:
        count+=1
        if (count-1)%4==0:
            pair=line[1:-1].strip().split("_")
            TP=pair[0]
            lenn=int(pair[2])
            bufferw+=">"+TP+"\n"
        elif (count-2)%4==0:
            
            bufferw+=line[1:lenn]+"\n"

            
    outf=open(outfile,"a")
    outf.write(bufferw)
    inf.close()
    outf.close()
    
def SNPposIUPAC(infile, outfile):
    """Gets the trimmed aligned sequence with SNP"""
    inf=open(infile,"r")
    eachline=1
    bufferw=""
    for line in inf:
        
        if eachline==1:
            pair=line[1:-1].strip().split("_")
            TP=pair[0]
            lenn=int(pair[2])
            
            eachline=2
        elif eachline==2:
            query=line[0:lenn]
            eachline=3
        elif eachline==3:
            eachline=4
            
        elif eachline==4:
            hit=line[0:lenn]
            #print query, hit
            pos=SNPandpos(query,hit)
            #print pos
            if pos:
                #modify string to accomodate position of string
                bufferw+=">"+TP+"|"+str(pos[0])+"\n"+query[0:pos[0]]+pos[1]+query[pos[0]+1::]+"\n"

            eachline=1
    outf=open(outfile,"a")
    outf.write(bufferw)
    inf.close()
    outf.close()

def SNPandpos(str1, str2):
    
    if len(str1)<>len(str2):
        return False
    for i in range(len(str1)):
        
        if str1[i]<>str2[i]:
            mismatch=i,commontools.IUPAC(str1[i], str2[i]) #position of SNP
            return mismatch

main()
