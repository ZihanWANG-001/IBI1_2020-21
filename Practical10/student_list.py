class Student(object):
	def __init__(self,first_name,last_name):
		self.name=first_name+' '+last_name #Link the first name and the last name
	def add_programme(self,programme):
		info=self.name+' '+programme       #Link the name and the programme
		return print(info)
print('Examples:')
a=Student('Hua','Li')
a.add_programme('BMS')
b=Student('Mike','Brown')
b.add_programme('BMI')
first_name=input('first_name:')
last_name=input('last_name:')
progremme=input('programme:')
c=Student(first_name,last_name)
c.add_programme(progremme)
		
