import os
import re
os.chdir('E:')
f=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')		
f2=open('edited.fa','w')
#Delete unwanted \n, that is, the \n at the end of the gene sequence.
#To avoid mixing of sequence and description (because the \n of the last line of a gene's sequence has been deleted), add \n at the beginning of the description. 
for line in f:
	if line.startswith('>'):
		line1=re.sub(r'>','\n>',line)
		f2.write(line1)
	else:
		line2=re.sub(r'\n','',line)
		f2.write(line2)
f.close()
f2.close()
f2=open('edited.fa','r')
function=[]
gene=[]
#Separate gene sequence and description. Store them  in separete lists.
for line in f2:
	if line.startswith('>'):
		function.append(line)
	else:
		gene.append(line)
f2.close()
#Find the index of gene of unknown function
unknown_index=[]
count=-1
for item in function:
	count+=1
	if re.search(r'unknown function',item):
		unknown_index.append(count)
	else:
		continue
#Store the length of unknown function in list "length"
length=[]
for i in unknown_index:
	length.append(len(gene[i]))
name=[]
#Store the name of unknown function in list "name"
for i in unknown_index:
	name.append(re.findall(r'>([A-Z0-9a-z\-]+)',function[i]))
#Store the sequence of unknown function in list "unknown_gene"
unknown_gene=[]
for i in unknown_index:
	unknown_gene.append(gene[i])
#Store the information of the unknown genes in a new file
f3=open('unknown_function.fa','w')
for i in range(0,len(unknown_index)):
	n=str(name[i])
#Strip the name. For example: ['YJR134C_mRNA'] should be YJR134C_mRNA.
	n2=n.strip("'[]")
#Join the name and the length. Make them appear in one line. Add \n at the end of the line.
#Make the sequence another line.
#Write the two lines into the new file.
#Close the file.
	l=str(length[i])+'\n'
	f3line1='  '.join([n2,l])
	f3line2=str(unknown_gene[i])
	f3.write(f3line1)
	f3.write(f3line2)
f3.close()
#Display the first 3 gene of unknown function.
f3=open('unknown_function.fa','r')
c=0
while c<=5:
	c+=1
	print(f3.readline())
f3.close()
