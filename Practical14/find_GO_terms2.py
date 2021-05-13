from xml.dom.minidom import parse
import xml.dom.minidom
import re
#The xml file should be in the same directory as this python script.
DOMTree=xml.dom.minidom.parse("go_obo.xml")
collection=DOMTree.documentElement
terms=collection.getElementsByTagName("term")
isa=collection.getElementsByTagName("is_a") #find the <is_a> elements
isa_id=[]
for i in isa:
	name=i.childNodes[0].data #extract the text of each <is_a> element
	isa_id.append(name)
#Preparing things needed for counting.
#The fourth macromolecule I chose is glycoprotein.
dna=[]
count1=0
rna=[]
count2=0
protein=[]
count3=0
glycoprotein=[]
count4=0
for term in terms:
	defstr=term.getElementsByTagName("defstr")[0]#find the description element
	text=defstr.childNodes[0].data #extract the description text
	ids=term.getElementsByTagName("id")[0] #find the id element
	id_text=ids.childNodes[0].data #extract the id text
	if re.findall(r'DNA',text):   #find whether the description contains dna/rna/protein/glycoprotein.
		dna.append(id_text)
	if re.findall(r'RNA',text):
		rna.append(id_text)
	if re.findall(r'protein',text):
		protein.append(id_text)
	if re.findall(r'glycoprotein',text):
		glycoprotein.append(id_text)

#for finding the childnodes, count how many <is_a> tag contains the id of a DNA/RNA/protein/glycoprotein-related GO terms. 
for i in isa_id:
	for a in dna:
		if a==i: #If it is the same, it means this term ("i") is the childNode of one of the DNA-related GO terms ("a").
			count1+=1
	for b in rna:
		if b==i:
			count2+=1
	for c in protein:
		if c==i:
			count3+=1
	for d in glycoprotein:
		if d==i:
			count4+=1
print('childNodes_DNA:',count1)
print('childNodes_RNA:',count2)
print('childNodes_protein:',count3)
print('childNodes_glycoprotein:',count4)
#Pie chart:
#import necessary package
#add the information to the pie chart.
import matplotlib.pyplot as plt
labels='DNA','RNA','protein','glycoprotein'
size=[count1,count2,count3,count4]
plt.label=('Number of childNodes')
plt.pie(size,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.show()
