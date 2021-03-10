#r rate

#Define n as the original number of infected individuals.
n=84
#Define the r rate
r=1.2
#Define a value to represent how many rounds are there.
i=0
#Check the infection round.
#While the number of infection round is lower than 5, start another round of infection.
#After the new round of infection: the total number of infected indeviduals is n*(1+r).
#The number of rounds should increase by 1.
#Check the infection round.
#Now if the round is 5, end the infection.
#Print out the total number of infected indeviduals after 5 generations.
while i<5:
	n=n*(1+r)
	i=i+1
print('The total number of individuals infected after 5 generations is ',n,' when the r rate is ',r)
