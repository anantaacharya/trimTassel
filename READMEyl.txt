Author: Ananta Raj Acharya
ananta@uga.edu

The included codes are complimentary to TASSEL UNEAK pipeline to keep TP nomenclature consistent between studies.
The included codes only work with fasta sequences.
Look at processTASSEL for filtering tools.
This is interactive rather than command line. For command line, look at a different branch.

Use pipeline:
It starts with HapMap.fas.txt.

1. splittasselfasta.py
	To extract consensus sequence with SNP for each TagPair
2. SNPDatabaseTasselUNEAK.py
	It serves as two functions: 
	a. makes a database from existing SNP tagpair consensus sequence (from 1 above)
	b. search the database (from 2a) with another set of Fasta consensus. (from 1 above)
	
3.  extractSequencefromTassel.py
	If you use some filters and want to use those tags only, save tags in each line (TP..), use the list to search against consensus (from 1 above).
	You can use this output to search against database
	
 
	