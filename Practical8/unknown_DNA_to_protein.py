import re
import os
os.chdir('E:')
f=open('unknown_function.fa','r')
#Separate the sequence and the name.
#Store the name in list "name".
#Store the DNA sequence in list "DNA".
DNA=[]
name=[]
for line in f:
	if re.search(r'^[AGCT]',line):
		DNA.append(line)
	else:
		newline=re.findall(r'(^\S+)\s+',line)
		name.append(newline)
f.close()
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
#Find the protein sequence and store in a list.
amino_str=''
amino=[]
for i in DNA:
	seq=str(i)
	valid=len(seq)-len(seq)%3   #make sure the length can be devided by three.
	for j in range(0,valid,3):  #extract three letter in the sequence as the codon and match the amino acid.
		key=seq[j:j+3]
		amino_str=amino_str+dictionary[key]
	amino.append(amino_str)
	amino_str=''                #make the amino acids that come from the same gene be together as a string and stored in another list.
#Calculate the length of protein sequence.
protein_length=[]
for i in amino:
	protein_length.append(len(i))
#Let the user input a file name.
#If it is a fasta file (.fa), then continue to write these information in the file.
	#To write the file:
	#Open the file in write mode.
	#Each item in the previous lists should be a line in the file.
	#Convert the list ltem into string.
	#Add something. e.g."Name:","Protein Length:","Protein Sequence:".
	#Add \n at the end of each line.
	#Write these lines into the file.
	#Close the file.
	#Open the file in read mode.
	#Read the file to check whether there's anything goes wrong.
#If the file doesn't end with ".fa", then print out a notification.
file_name=input('Enter a file name:')
if file_name.endswith('.fa'):
	f2=open(file_name,'w')
	for i in range(0,len(name)):
		newname=str(name[i]).strip("'[]")
		line1='Name: '+newname+'\n'
		line2='Protein Length: '+str(protein_length[i])+'\n'
		line3='Protein Sequence: '+str(amino[i])+'\n'
		f2.write(line1)
		f2.write(line2)
		f2.write(line3)
	f2.close()
	f2=open(file_name,'r')
	print(f2.read())
else:
	print('Please enter the name of a fasta file!')

	
