x=1
y=1
i=2
print(x)
print(y)
for i in range(2,7):
	x=x+y
	print(x)
	y=y+x
	print(y)
	i=i+1
print(x+y)
#x=1,y=1
#x=2,y=1
#y=3,x=2
#x=5,y=3
#y=8,x=5

