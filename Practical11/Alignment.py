import os
import re
import pandas as pd
#os.chdir('E:') For the marker's convience, I moved the file to the same directory as the python script.
#Read three files and store the sequence in a string
f1=open('SOD2_human.fa')
human=''
for line in f1:
	if not line.startswith('>'):
		human=human+str(re.sub(r'\n','',line))
f1.close()

f2=open('SOD2_mouse.fa')
mouse=''
for line in f2:
	if not line.startswith('>'):
		mouse=mouse+str(re.sub(r'\n','',line))
f2.close()

random=''
f3=open('RandomSeq.fa')
for line in f3:
	if not line.startswith('>'):
		random=random+str(re.sub(r'\n','',line))
f3.close()

#Write the BLOSUM62 matrix into a list of lists.
#The title of colum and row
column=['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X','*']
row=['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X','*']
blosum=[
[4,-1,-2,-2,0,-1,-1,0,-2,-1,-1,-1,-1,-2,-1,1,0,-3,-2,0,-2,-1,0,-4],
[-1,5,0,-2,-3,1,0,-2,0,-3,-2,2,-1,-3,-2,-1,-1,-3,-2,-3,-1,0,-1,-4],
[-2,0,6,1,-3,0,0,0,1,-3,-3,0,-2,-3,-2,1,0,-4,-2,-3,3,0,-1,-4], 
[-2,-2,1,6,-3,0,2,-1,-1,-3,-4,-1,-3,-3,-1,0,-1,-4,-3,-3,4,1,-1,-4], 
[0,-3,-3,-3,9,-3,-4,-3,-3,-1,-1,-3,-1,-2,-3,-1,-1,-2,-2,-1,-3,-3,-2,-4], 
[-1,1,0,0,-3,5,2,-2,0,-3,-2,1,0,-3,-1,0,-1,-2,-1,-2,0,3,-1,-4], 
[-1,0,0,2,-4,2,5,-2,0,-3,-3,1,-2,-3,-1,0,-1,-3,-2,-2,1,4,-1,-4], 
[0,-2,0,-1,-3,-2,-2,6,-2,-4,-4,-2,-3,-3,-2,0,-2,-2,-3,-3,-1,-2,-1,-4], 
[-2,0,1,-1,-3,0,0,-2,8,-3,-3,-1,-2,-1,-2,-1,-2,-2,2,-3,0,0,-1,-4],
[-1,-3,-3,-3,-1,-3,-3,-4,-3,4,2,-3,1,0,-3,-2,-1,-3,-1,3,-3,-3,-1,-4], 
[-1,-2,-3,-4,-1,-2,-3,-4,-3,2,4,-2,2,0,-3,-2,-1,-2,-1,1,-4,-3,-1,-4], 
[-1,2,0,-1,-3,1,1,-2,-1,-3,-2,5,-1,-3,-1,0,-1,-3,-2,-2,0,1,-1,-4], 
[-1,-1,-2,-3,-1,0,-2,-3,-2,1,2,-1,5,0,-2,-1,-1,-1,-1,1,-3,-1,-1,-4], 
[-2,-3,-3,-3,-2,-3,-3,-3,-1,0,0,-3,0,6,-4,-2,-2,1,3,-1,-3,-3,-1,-4], 
[-1,-2,-2,-1,-3,-1,-1,-2,-2,-3,-3,-1,-2,-4,7,-1,-1,-4,-3,-2,-2,-1,-2,-4], 
[1,-1,1,0,-1,0,0,0,-1,-2,-2,0,-1,-2,-1,4,1,-3,-2,-2,0,0,0,-4], 
[0,-1,0,-1,-1,-1,-1,-2,-2,-1,-1,-1,-1,-2,-1,1,5,-2,-2,0,-1,-1,0,-4], 
[-3,-3,-4,-4,-2,-2,-3,-2,-2,-3,-2,-3,-1,1,-4,-3,-2,11,2,-3,-4,-3,-2,-4],
[-2,-2,-2,-3,-2,-1,-2,-3,2,-1,-1,-2,-1,3,-3,-2,-2,2,7,-1,-3,-2,-1,-4],
[0,-3,-3,-3,-1,-2,-2,-3,-3,3,1,-2,1,-1,-2,-2,0,-3,-1,4,-3,-2,-1,-4],
[-2,-1,3,4,-3,0,1,-1,0,-3,-4,0,-3,-3,-2,0,-1,-4,-3,-3,4,1,-1,-4],
[-1,0,0,1,-3,3,4,-2,0,-3,-3,1,-1,-3,-1,0,-1,-3,-2,-2,1,4,-1,-4],
[0,-1,-1,-1,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,0,0,-2,-1,-1,-1,-1,-1,-4],
[-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,1]
]
#human vs mouse
score_hm=0
for a in range(0,len(human)):
	for i in range(0,len(row)):
		if human[a]==row[i]:
			list1=blosum[i]
			for j in range(0,len(column)):
				if mouse[a]==column[j]:
					score_hm=score_hm+list1[j]

number1=0
for h in range(len(human)):
	if human[h]==mouse[h]:
		number1+=1
print('Human vs Mouse')
print('BLOSUM62 score:',score_hm)
print('The percentage of identical amino acids:',(number1/len(human))*100,'%\n')

	

#human vs random
score_hr=0
for a in range(0,len(human)):
	for i in range(0,len(row)):
		if human[a]==row[i]:
			list1=blosum[i]
			for j in range(0,len(column)):
				if random[a]==column[j]:
					score_hr=score_hr+list1[j]

number2=0
for h in range(len(human)):
	if human[h]==random[h]:
		number2+=1
print('Human vs Random')
print('BLOSUM62 score:',score_hr)
print('The percentage of identical amino acids:',(number2/len(human))*100,'%\n')

#mouse vs random
score_mr=0
for a in range(0,len(mouse)):
	for i in range(0,len(row)):
		if mouse[a]==row[i]:
			list1=blosum[i]
			for j in range(0,len(column)):
				if random[a]==column[j]:
					score_mr=score_mr+list1[j]

number3=0
for m in range(len(mouse)):
	if mouse[m]==random[m]:
		number3+=1
print('Mouse vs Random')
print('BLOSUM62 score:',score_mr)
print('The percentage of identical amino acids:',(number3/len(mouse))*100,'%')



	
		
		
