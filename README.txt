Author: Ananta Raj Acharya
ananta@uga.edu

This is utility for TASSEL UNEAK pipeline 
This is for fasta sequences
Look at processTASSEL for filtering tools
This is interactive not command line
for command line look at different branch

use pipeline.
It starts with HapMap.fas.txt

1. splittasselfasta.py
	To extrach consensus sequence with SNP for each TagPair
2. SNPDatabaseTasselUNEAK.py
	it serves as two function, 
	a. makes a database from existing SNP tagpair consensus sequence (from 1 above)
	b. Search the database (from 2a) with another set of Fasta consensus. (from 1 above)
	
3.  extractSequencefromTassel.py
	If you use some filters and want to use those tags only. save tags in each line (TP..). use the list to search against consensus (from 1 above)
	you can use this output to search against database
	
 
	