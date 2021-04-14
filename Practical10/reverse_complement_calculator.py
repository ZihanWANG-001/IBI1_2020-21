import re
def reverse_complement_calculator():
	seq=input('Please enter a DNA sequence:')#Take the input as seq
	seq0=seq.upper() #Capitalize all characters.
	seq1=re.sub(r'A','temp1',seq0)  #Convert the original 'A' into a temporary storage. In order to avoid the mixture of the original 'A' and the complement of 'T'.
	seq2=re.sub(r'G','temp2',seq1)  #Convert the original 'G' into a temporary storage. In order to avoid the mixture of the original 'G' and the complement of 'C'.
	seq3=re.sub(r'C','G',seq2)		#replace 'C' with 'G'
	seq4=re.sub(r'T','A',seq3)		#replace 'T' with 'A'
	seq5=re.sub(r'temp1','T',seq4)	#replace 'A' with 'T'
	seq6=re.sub(r'temp2','C',seq5)	#replace 'G' with 'C'
	list1=list(seq6)				#change the string to a list
	list1.reverse()					#reverse the order of the list
	return print(''.join(list1))	#join the reversed list and print it as a return.
#Call the function in this way:
reverse_complement_calculator()
#demo seq: 'AGCTTTCCGAC'
#demo reverse complement: 'GTCGGAAAGCT'


