#Method one: using a dictionary
import os
import re
os.chdir('E:') #Please change this directory to where the file is stored in your computer, or delete this line and move the file to the same directory as this script.
f=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')	
#Create a dictionary to store the information.
dic={}
#Create an empty string to be used in the loop to add the DNA sequence.
gene=''
for line in f:
	if line.startswith('>'):#Find the description lines.
		key=line
		gene=''#If the gene is changed (this means a line that satisfied the condition in "if"), then this string should be cleared. 
		       #To prevent the sequence of different genes being added together.
	else:
		gene=gene+str(re.sub(r'\n','',line))#Delete \n at the end of the sequence. Make the sequence of the same gene together, being one line.
		dic[key]=gene  #Match the sequence and the description using the "key:item" pattern in the dictionary.
#Start to write the file.
f2=open('unknown_function.fa','w')
for key in dic.keys():  #Iterate all the keys in the dictionary.
	if re.search(r'unknown function',key): #Find the unknown function.
		x=str(re.findall(r'>(\S+)_{1}',key)).strip("'[]") #Extract the name and strip [' and '] of the name.
		line1=x+'   '+str(len(dic[key]))+'\n'      #Join the name and the length and add \n at the end.
		line2=dic[key]+'\n'                         #The sequence.
		f2.write(line1)                             #write.
		f2.write(line2)
f2.close()
f2=open('unknown_function.fa','r')
print(f2.read())
f2.close()



#Method two
import os
import re
os.chdir('E:') #Please change this directory to where the file is stored in your computer, or delete this line and move the file to the same directory as this script.
f=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')		
f2=open('temp.fa','w')
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
f2=open('temp.fa','r')
function=[]
gene=[]
#Separate gene sequence and description. Store them  in separete lists.
for line in f2:
	if line.startswith('>'):
		function.append(line)
	elif line.startswith('\n'):
		del(line)
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
	length.append(len(gene[i])-1)#Because there is a '\n' at the end of the line, we need to substrate 1 to get the real length.
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

