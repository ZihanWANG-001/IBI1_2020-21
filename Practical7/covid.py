#import the needed packages
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing data
#change to the the directory where "full_data.csv" is stored.
os.chdir("E:") #Please change this directory to where the file is stored in your computer, or delete this line and move the file to the same directory as this script.
covid_data=pd.read_csv("full_data.csv")

#showing all the columns, and every second row between (and including) 0 and 10. 
print(covid_data.iloc[0:12:2,:])

#showing "total cases" for all rows corresponding to Afghanistan.
#create a empty list for Afghanistan
afghanistan=[]
#using a for loop to check all rows one by one whether the location is Afghanistan.
for i in range(0,7996):
	afghanistan.append(covid_data.loc[i,"location"]=="Afghanistan") #Add the Boolean values to the list
#use Booleans to find all rows of Afghanistan and show the total cases.
print(covid_data.loc[afghanistan,"total_cases"])

#same method to find new cases and date of the world. 
world=[]
for i in range(0,7996):
     world.append(covid_data.loc[i,'location']=='World')
world_new_cases=covid_data.loc[world,['date','new_cases']]
#Transfer world new cases to ndarray for computing the mean and median.
cases=np.array(world_new_cases.loc[:,'new_cases'])
#print the results and add some description.
print('mean:',np.mean(cases))
print('median:',np.median(cases))

#start a new figure: boxplot for new cases worldwide.
plt.figure()
plt.boxplot(cases,
			vert=True,
			whis=1.5,
			patch_artist=True,
			meanline=False,
			showbox=True,
			showcaps=True,
			showfliers=False,
			showmeans=True,
			notch=False
			)
#add title to the figure
plt.title("World New Cases")

#start a new figure for new cases and new deaths wrldwide.
#find the column "date" in location "World"
world_dates=world_new_cases.loc[:,'date']
world_deaths=covid_data.loc[world,'new_deaths']
plt.figure()
#plot: x-axis is the world dates, y-axis is the number. Use green pentacle for new cases and red pentacle for new deaths.
plt.plot(world_dates,cases,'gp',label=('New Cases'))
plt.plot(world_dates,world_deaths,'rp',label=('New Deaths'))
#Add the dates to x-axis. Every four date appears on the x-axis, and rotated 90 degree to prevent the labels overlap.
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
#Add title.
plt.title("New Cases and New Deaths Worldwide")
#Add x label, y label and the legend.
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()

#starting to plot the figure that contains the new cases from China and UK.
#find all the data related to China's new cases.
china=[]
for i in range(0,7996):
	china.append(covid_data.loc[i,'location']=='China')
china_new_cases=covid_data.loc[china,'new_cases']
#find all the date related to UK's new cases.
england=[]
for i in range(0,7996):
	england.append(covid_data.loc[i,'location']=='United Kingdom')
england_new_cases=covid_data.loc[england,'new_cases']
#Create a new figure	
plt.figure()
#Add the data of China and the UK to the plot. Use different colors and label the curves.
plt.plot(world_dates,china_new_cases,'b*',label=('China'))
plt.plot(world_dates,england_new_cases,'r*',label=('United Kingdom'))
#Add the dates to x-axis. Every four date appears on the x-axis, and rotated 90 degree to prevent the labels overlap.
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
#Add title to the figure
plt.title("New Cases in China and United Kingdom")
#Add labels of x and y axises.
plt.xlabel("Date")
plt.ylabel("New Cases")
#Add the figure legend (show the labels of the curve added in the "plt.plot" function.
plt.legend()

#Start to answer the question.
#find the total cases and dates of South Korea, Kenya and Colombia.
south_korea=[]
for i in range(0,7996):
	south_korea.append(covid_data.loc[i,'location']=='South Korea')
south_korea_total_cases=covid_data.loc[south_korea,'total_cases']
south_korea_dates=covid_data.loc[south_korea,'date']
kenya=[]
for i in range(0,7996):
	kenya.append(covid_data.loc[i,'location']=='Kenya')
kenya_total_cases=covid_data.loc[kenya,'total_cases']
kenya_dates=covid_data.loc[kenya,'date']
colombia=[]
for i in range(0,7996):
	colombia.append(covid_data.loc[i,'location']=='Colombia')
colombia_total_cases=covid_data.loc[colombia,'total_cases']
colombia_dates=covid_data.loc[colombia,'date']
#Start to plot a figure containing these three countries' total covid cases.
plt.figure()
#plot each curve using different colors and label them. 
plt.plot(south_korea_dates,south_korea_total_cases,'r.',label=('South Korea'))
plt.plot(kenya_dates,kenya_total_cases,'g.',label=('Kenya'))
plt.plot(colombia_dates,colombia_total_cases,'b.',label=('Colombia'))
#Add title, legend, x and y labels and dates on x-axis.
plt.title("Total Cases")
plt.legend()
plt.xticks(world_dates.iloc[0:len(world_dates):3],rotation=-90)
plt.xlabel("Date")
plt.ylabel("Total Cases")
#show all the plots.
plt.show()


