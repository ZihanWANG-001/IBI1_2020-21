#Create the first two values
x=1
y=1
print(x) #Print the first two values
print(y)
#Create a loop 
#Find the repeat time, that is the range of i
for i in range(0,11): #A total of 13 values,remain 11. Need 11 rounds. So the range of i is (0,11).
	x=x+y      #Let an be the nth of the fibonacci squence. x=a3=a1+a2=1+1=2
	y=x-y      #Reset y to the previous x value. So that the addition can move on. y=x-1=2-1=a2
	i=i+1      
	print(x)   #print a3
	           #Next,x=a4=a3+a2
	           #y=x-y=a4-a2=a3
	           #Next,x=a5=x+y=a4+a3
	           #y=x-y=a5-a3=a4
	           #Next,x=a6=a4+a5
	           #..............


