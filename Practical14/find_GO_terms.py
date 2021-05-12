from xml.dom.minidom import parse
import xml.dom.minidom
import re
#The xml file should be in the same directory as this python script.
DOMTree=xml.dom.minidom.parse("go_obo.xml")
collection=DOMTree.documentElement
terms=collection.getElementsByTagName("term")

#Find the childnodes of DNA related GO terms.
dna=[]
for term in terms:
	defstr=term.getElementsByTagName("defstr")[0]#find the description element
	text=defstr.childNodes[0].data #extract the description text
	ids=term.getElementsByTagName("id")[0] #find the id element
	id_text=ids.childNodes[0].data #extract the id text
	if re.findall(r'DNA',text):   #find whether the description contains dna.
		dna.append(id_text)       #if so, add the id into a list
isa=collection.getElementsByTagName("is_a") #find the <is_a> elements
# for finding the childnodes, count how many <is_a> tag contains the id of a DNA-related GO terms.
count1=0
for i in isa:
	name=i.childNodes[0].data #extract the text of each <is_a> element
	for j in dna:
		if name==j:  #To find out whether it is the same as one of the DNA-related genes. 
			count1=count1+1 #If it is the same, it means this term is the childNode of one of the DNA-related GO terms.
print('childNodes_DNA:',count1)

#Find the childnodes of RNA related GO terms.
rna=[]
for term in terms:
	defstr=term.getElementsByTagName("defstr")[0]#find the description element
	text=defstr.childNodes[0].data #extract the description text
	ids=term.getElementsByTagName("id")[0] #find the id element
	id_text=ids.childNodes[0].data #extract the id text
	if re.findall(r'RNA',text):   #find whether the description contains rna.
		rna.append(id_text)       #if so, add the id into a list
isa=collection.getElementsByTagName("is_a") #find the <is_a> elements
# for finding the childnodes, count how many <is_a> tag contains the id of a RNA-related GO terms.
count2=0
for i in isa:
	name=i.childNodes[0].data #extract the text of each <is_a> element
	for j in rna:
		if name==j:  #To find out whether it is the same as one of the RNA-related genes. 
			count2=count2+1 #If it is the same, it means this term is the childNode of one of the RNA-related GO terms.
print('childNodes_RNA:',count2)

#Find the childNodes of protein related GO terms.
protein=[]
for term in terms:
	defstr=term.getElementsByTagName("defstr")[0]#find the description element
	text=defstr.childNodes[0].data #extract the description text
	ids=term.getElementsByTagName("id")[0] #find the id element
	id_text=ids.childNodes[0].data #extract the id text
	if re.findall(r'protein',text):   #find whether the description contains rna.
		protein.append(id_text)       #if so, add the id into a list
isa=collection.getElementsByTagName("is_a") #find the <is_a> elements
# for finding the childnodes, count how many <is_a> tag contains the id of a protein-related GO terms.
count3=0
for i in isa:
	name=i.childNodes[0].data #extract the text of each <is_a> element
	for j in protein:
		if name==j:  #To find out whether it is the same as one of the protein-related genes. 
			count3=count3+1 #If it is the same, it means this term is the childNode of one of the protein-related GO terms.
print('childNodes_protein:',count3)

#The fourth macromolecule I choose is glycoprotein.
#Find the childNodes of glycoprotein related GO terms.
glycoprotein=[]
for term in terms:
	defstr=term.getElementsByTagName("defstr")[0]#find the description element
	text=defstr.childNodes[0].data #extract the description text
	ids=term.getElementsByTagName("id")[0] #find the id element
	id_text=ids.childNodes[0].data #extract the id text
	if re.findall(r'glycoprotein',text):   #find whether the description contains glycoprotein.
		glycoprotein.append(id_text)       #if so, add the id into a list
isa=collection.getElementsByTagName("is_a") #find the <is_a> elements
# for finding the childnodes, count how many <is_a> tag contains the id of a glycoprotein-related GO terms.
count4=0
for i in isa:
	name=i.childNodes[0].data #extract the text of each <is_a> element
	for j in glycoprotein:
		if name==j:  #To find out whether it is the same as one of the glycoprotein-related genes. 
			count4=count4+1 #If it is the same, it means this term is the childNode of one of the glycoprotein-related GO terms.
print('childNodes_glycoprotein:',count4)

#Pie chart:
import matplotlib.pyplot as plt
labels='DNA','RNA','protein','glycoprotein'
size=[count1,count2,count3,count4]
plt.label=('Number of childNodes')
plt.pie(size,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.show()	
