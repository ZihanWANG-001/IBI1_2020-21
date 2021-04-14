def grade():
	#Take the four input.
	name=input('Student_name:')
	code=float(input('Grade for the code portfolio:'))
	poster=float(input('Grade for the poster presentation:'))
	exam=float(input('Grade for the final exam:'))
	#Calculate the grade
	grade=0.4*code+0.3*poster+0.3*exam
	#print the result
	return print('Student name:',name,'\nFinal grade:',grade)
#Call the function
grade()
