#Create two lists
gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
#Perform numerical operations on dnarry
import numpy as np
l=np.array(gene_lengths)
c=np.array(exon_counts)
#Sort
average_exon_length=sorted(l/c)
#Show the sorted list
print(average_exon_length)
#Draw the boxplot
import matplotlib.pyplot as plt
plt.boxplot(average_exon_length,#Use the data in "average_exon_length"
			notch=False,
			vert=True,
			whis=1.5,
			patch_artist=True,
			meanline=False,
			showcaps=True,
			showbox=True,
			showfliers=True,
			#customize the color
			boxprops=dict(facecolor='turquoise', color='black'),
            capprops=dict(color='black'),
            whiskerprops=dict(color='black'),
            flierprops=dict(color='yellow', markeredgecolor='orange'),
            medianprops=dict(color='mediumvioletred')
			)
plt.show() #Show the boxplot. Otherwise we cannot see it.
			
			
