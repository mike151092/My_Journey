import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("./Data_Capstone_Project/911.csv")

print(df.shape)
print(df.info())
print(df.isnull().sum())
#print(df['zip'].isnull())


#Top 5 zip codes for 911 calls
print(df['zip'].value_counts().head(5))

#Top 5 townships
print(df['twp'].value_counts().head(5))

#Unique Title codes
print(df['title'].nunique())

#Create a Reason column from the data set
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])

print(df['Reason'])

#Common Reason for the 911 calls
print(df['Reason'].value_counts())

#Create countplot using seaborn of 911 calls by Reason

#sns.countplot(x='Reason',data=df,palette='viridis')

#plt.show()

#data type of the objct in timeStamp
print(df['timeStamp'].dtype)

#Convert the time stamp from str to 
print(df['timeStamp'][0])
from datetime import datetime
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

print(df['timeStamp'].dtype)

#Create new column hour Month and day of week
print(df['timeStamp'][0].hour)

df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)

print(df['Hour'])

df['Month'] =df['timeStamp'].apply(lambda time: time.month)

print(df['Month'])

df['Day of Week'] =df['timeStamp'].apply(lambda time: time.dayofweek)

print(df['Day of Week'])

#map day of week from the dictionary and display the weeks
dmap= {0:'Monday',1:'Tuesday',2:'Wednesday', 3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
df['Day of Week'] = df['Day of Week'].map(dmap)

print(df['Day of Week'])

#Create a count plot for the day of week and colour it based on the Reason column

#sns.countplot(x='Day of Week',data=df,hue='Reason')
#plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0)

#plt.show()

#Create a count plot for the Month and colour it based on the Reason column
sns.countplot(x='Month',data=df,hue='Reason')
plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0)

plt.show()