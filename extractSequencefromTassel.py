

def main():
    infile=raw_input("filename")
    tagfile=raw_input("tag")
    outfile=raw_input("outfile")
    tags=processTagfile(tagfile)
    process(infile, outfile, tags)
    
def processTagfile(tagfile):
    infile=open(tagfile,"r")
    tags=list()
    for line in infile:
        tags.append(line.strip())
    return tags

def process(infile1, outfile1, tags):
    infile=open(infile1,"r")
    flag=0
    seqDict=dict()
    for line in infile:
        if line[0] in ">":
            tag=line.strip().split("|")[0][1::]
            if tag in tags:
                flag=1
                writetag=tag
                continue
        else:    
            if flag==1:
                seqDict[writetag]=line
                flag=0
    outfile=open(outfile1, "a")        
    for key, val in seqDict.items():
        outfile.write(">"+key+"\n"+val)
            
    infile.close()
    outfile.close()
    
main()
