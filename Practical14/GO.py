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

#Establish a dictionary. The key is the parent node and the corresponding value is the childnode of the key.
#Store each id as one entry of the dictionary.
#For each key create an empty list to store its childnodes.
parent_child={} 
for term in terms:
	id=term.getElementsByTagName('id')[0].childNodes[0].data
	parent_child[id]=[]
#<is_a> is the parent nodes, they need to be stored in the key.
for term in terms:
	id1=term.getElementsByTagName('id')[0].childNodes[0].data #Get the child of the <is_a> and store it in the list of the <is_a> key.
	is_as=term.getElementsByTagName('is_a')#An id can have more than one <is_a>. Use a loop to add them all into the list.
	for is_a in is_as:
		parent_child[is_a.childNodes[0].data].append(id1)
#Now we have the dictionary that stored all one-layer relationship of parent-child.
#There are some entry with an empty list. This means this GO:xxxx in the key has no childnode.
#define the function to find all levels of childnodes of a given finder.

#define a function to search for the given keyword.
#The "finder" is either "DNA" or "RNA" or other keywords.
#Search this "finder" in each <defstr>
#If it is in the <defstr>, then find the <id> of this <defstr>. This is the parent node.
#Search in the dictionary's key for this parent node.
#If its list is not empty, this means it has childnode(s)
#Make its list be the new "finder",find their childnodes.
def search(finder):
	for term in terms:
		defstr=term.getElementsByTagName('defstr')[0].childNodes[0].data
		if finder in defstr:
			id2=term.getElementsByTagName('id')[0].childNodes[0].data
			if parent_child[id2]!=[]:                 #The function will stop when there is no more childnodes for a given id-----reached the tip of the tree.
				new_parent_list=parent_child[id2]
				a=childNode_counter(new_parent_list)  #Call another function to repeatedly use the parent_child relationship built by the dictionary to find all the childnodes and store them in a list.
	print('childNode number of',finder,':',a)         #a is the returned result of the other function, which is the length of the list which stores the childnodes.
	global b                                          #because we need to store each "a" value to draw the pie chart, a global b is needed to make it accessible outside the function.
	b=a
	return a
				
children=[]		#Creat an empty list to store the childnodes.
#Define another function to repeadly count the childnodes of previous nodes.		
def childNode_counter(new_parent_list):
	for j in range(0,len(new_parent_list)):#for each_previous_child in new_parent_list. 
		if new_parent_list[j] not in children: #new_parent_list[j] is the previous child
			children.append(new_parent_list[j]) #add the childnodes into the list
			childNode_counter(parent_child[new_parent_list[j]]) #parent_child[new_parent_list[j]] is the child of the new parent (previous child)
	return len(children)
#Call the functions to search for DNA's childnodes
search('DNA')
a1=b
#Call the functions to search for RNA's childnodes, and protein's and glycoprotein's
#Remember to clear the childnode list each time.
children=[]
search('RNA')
a2=b
children=[]
search('protein')
a3=b
children=[]
search('glycoprotein')
a4=b

#Draw the pie chart
labels='DNA','RNA','protein','glycoprotein'
size=[a1,a2,a3,a4]
plt.label=('Number of childNodes')
plt.pie(size,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.show()

				
				
				
				
				
				
				
