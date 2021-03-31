#Method 1:
import re
seq='ATGCGACTACGATCGAGGGCC'
#Split the sequence into many three-letter-code.
#The regex means A or G or C or T repeat three times.
#"()" will let the three-letter-code returns as part of the resulting list.
code=re.split(r'([AGCT]{3})',seq)
#Spilting the sequence in this way will return many empty string ''. The code below aims to delete them.
for i in code:
	if i=='':
		code.remove(i)
	else:
		continue
#Find out: for every item of the list, whether it can match these codons. 
for i in range(0,len(code)):
	if re.search(r'TT[TC]{1}',code[i]):
		code[i]='F'
	elif re.search(r'TT[AG]{1}',code[i]):
		code[i]='L'
	elif re.search(r'CT[AGCT]{1}',code[i]):
		code[i]='L'
	elif re.search(r'AT[TC]{1}',code[i]):
		code[i]='I'
	elif re.search(r'ATA',code[i]):
		code[i]='J'
	elif re.search(r'GT[ATCG]{1}',code[i]):
		code[i]='V'
	elif re.search(r'TC[AGCT]{1}',code[i]):
		code[i]='S'
	elif re.search(r'CC[AGCT]{1}',code[i]):
		code[i]='P'
	elif re.search(r'AC[AGCT]{1}',code[i]):
		code[i]='T'
	elif re.search(r'GC[AGCT]{1}',code[i]):
		code[i]='A'
	elif re.search(r'TA[CT]{1}',code[i]):
		code[i]='Y'
	elif re.search(r'TAA',code[i]):
		code[i]='O'
	elif re.search(r'TAG',code[i]):
		code[i]='U'
	elif re.search(r'CA[TC]{1}',code[i]):
		code[i]='H'
	elif re.search(r'CAA',code[i]):
		code[i]='Q'
	elif re.search(r'CAG',code[i]):
		code[i]='Z'
	elif re.search(r'AAT',code[i]):
		code[i]='N'
	elif re.search(r'AAC',code[i]):
		code[i]='B'
	elif re.search(r'AA[AG]{1}',code[i]):
		code[i]='K'
	elif re.search(r'GA[CT]{1}',code[i]):
		code[i]='D'
	elif re.search(r'GA[AG]{1}',code[i]):
		code[i]='E'
	elif re.search(r'TG[CT]{1}',code[i]):
		code[i]='C'
	elif re.search(r'CG[AGCT]{1}',code[i]):
		code[i]='R'
	elif re.search(r'AG[CT]{1}',code[i]):
		code[i]='S'
	elif re.search(r'AG[AG]{1}',code[i]):
		code[i]='R'
	elif re.search(r'GG[AGCT]{1}',code[i]):
		code[i]='G'
	else:
		code[i]='M'
#Create a string that contains the results. 
#Join the items one by one in list "code"
amino=''
for i in range(0,len(code)):
	amino=amino+code[i]
print(amino)


#Method 2
#Create a dictionary. The keys are codons, values are the corresponding amino acids.
dictionary={'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
 'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
 'ATT':'I','ATC':'I','ATA':'J','ATG':'M',
 'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
 'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
 'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
 'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
 'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
 'TAT':'Y','TAC':'Y','TAA':'Y','TAG':'U',
 'CAT':'H','CAC':'H','CAA':'Q','CAG':'Z',
 'AAT':'N','AAC':'B','AAA':'K','AAG':'K',
 'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
 'TGT':'C','TGC':'C','TGA':'X','TGG':'W',
 'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
 'AGT':'S','AGC':'S','AGA':'A','AGG':'R',
 'GGT':'G','GGC':'G','GGA':'G','GGG':'G'}
seq='ATGCGACTACGATCGAGGGCC'
#Split the sequence into many three-letter-code.
#The regex means A or G or C or T repeat three times.
#"()" will let the three-letter-code returns as part of the resulting list.
code=re.split(r'([AGCT]{3})',seq)
#Spilting the sequence in this way will return many empty string ''. The code below aims to delete them.
for i in code:
	if i=='':
		code.remove(i)
	else:
		continue
aa_sequence=''
#table[i] means to find the value in the dictionary that has the key "i". In this way we can find what amino acid is for codon i.
for i in code:
	aa_sequence=aa_sequence+dictionary[i]
print(aa_sequence)
print('The amino acid sequence is: '+aa_sequence)
	
