#Some simple math
a=110602  #My birthday
b=190784  #Rob's birthday
c=100321  #Today's date
#Calculate the absolute difference between my birthday and today's date. 
#Check which is bigger. The big value minus the small value.
if a>=c:
	d=a-c
	print('d=',d) #print out the results.
else:
	d=c-a
	print('d=',d) #print out the results.
#Calculate the absolute difference between my value and Rob's value.
#Check which is bigger. The big value minus the small value.
if b>=a:
	e=b-a
	print('e=',e)#print out the results.
else:
	e=a-b
	print('e=',e)
#Compare d to e
if d>e:
	print('d is bigger than e')
elif d<e:
	print('d is smaller than e')
else:
	print('d is equal to e')
#Booleans
x=True       #Set the Boolean value to x and y.
y=False
z=(x and not y)or(y and not x)#Define z to make z true if x and y are one of them true and one of them false. 
print(z)    #Print the result of z. It is true if either x or y (but not both) are true. It is false if x and y are both true or both false.
w=x!=y      #Let w be true if x and y are not the same(That should be either 'x=True,y=False' or 'x=False,y=True'). 
print(w)    #Therefore, by definition,z and w have the same Boolean value. Print out w.
print(z==w) #To test if z and w are always the same. And print out the result.


