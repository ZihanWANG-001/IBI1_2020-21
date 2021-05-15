from xml.dom.minidom import parse
import xml.dom.minidom
import re
import matplotlib.pyplot as plt
#The xml file should be in the same directory as this python script.
DOMTree=xml.dom.minidom.parse("go_obo.xml")
collection=DOMTree.documentElement
terms=collection.getElementsByTagName("term")
#Preparing things needed for counting.
#The fourth macromolecule I chose is glycoprotein.
dna=[]
rna=[]
protein=[]
glycoprotein=[]
for term in terms:
	defstr=term.getElementsByTagName("defstr")[0]#find the description element
	text=defstr.childNodes[0].data #extract the description text
	id=term.getElementsByTagName("id")[0] #find the id element
	if re.findall(r'DNA',text):   #find whether the description contains dna/rna/protein/glycoprotein.
		dna.append(id)
	if re.findall(r'RNA',text):
		rna.append(id)
	if re.findall(r'protein',text):
		protein.append(id)
	if re.findall(r'Protein',text):
		protein.append(id)
	if re.findall(r'glycoprotein',text):
		glycoprotein.append(id)	
	if re.findall(r'Glycoprotein',text):
		glycoprotein.append(id)
		
is_as=collection.getElementsByTagName("is_a")		#Collect all the <is_a> nodes
def childNode_finder(x):
	global count
	global number
	count=0
	childNodeid=[]
	for k in range(0,is_as.length):
		for i in x:
			if i.childNodes[0].data==is_as[k].childNodes[0].data:  #Extract the text and compare
				count+=1
				number+=1
				childNodeid.append(is_as[k].parentNode.childNodes[1])
	if count!=0:
		x=childNodeid
		childNode_finder(x) #recursion, use the childnodes found as the new parent nodes.
	else:                   #count=0 means there is no such id in <is_a>, so it has no child, it is the end of the node tree.
		return number
		
number=0
childNode_finder(dna)
number1=number
print('childNodes_DNA',number1)
number=0
childNode_finder(rna)
number2=number
print('childNodes_RNA',number2)
number=0
childNode_finder(protein)
number3=number
print('childNodes_protein',number3)
number=0
childNode_finder(glycoprotein)
number4=number
print('childNodes_glycoprotein',number4)

labels='DNA','RNA','protein','glycoprotein'
size=[number1,number2,number3,number4]
plt.label=('Number of childNodes')
plt.pie(size,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.show()

				
				
				
				
				
				
				
