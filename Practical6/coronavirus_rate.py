#coronavirus rates
#Record a frequency dictionary
coronavirus={'USA':29862124,'India':11285561,'Brazil':11205972,'Russia':4360823,'UK':4234924}
#import the python package matplotlib
import matplotlib.pyplot as plt
#Extract all the keywords in the dictionary so they can be used as labels in the pie chart
labels=list(coronavirus)
#Creat a list contains all the coronavirus numbers in the dictionary
#Use for-loop to add the values one by one to the empty list
numbers=[]
for i in coronavirus:
	numbers.append(coronavirus[i])	
#Use plt.pie to draw the pie chart
plt.pie(numbers,labels=labels,autopct='%1.1f%%',
	shadow=False,startangle=90)
plt.axis('equal') #Ensure the pie chart is drawn as a circle
#Show the dictionary
print(coronavirus)
#Show the pie chart
plt.show()

