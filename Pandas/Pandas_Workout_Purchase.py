import numpy as np
import pandas as pd

df = pd.read_csv("Ecommerce Purchases")

#print(df)
#print(df.head())
#print(df.info())

#average purchase price

#print(df['Purchase Price'].mean())

#Highest and lowest purchase price

#print(df['Purchase Price'].max())
#print(df['Purchase Price'].min())

#How many people have English 'en' as their Language of choice on the website?

#print(df[df['Language']=='en'].count())

#How many people have the job title of "Lawyer" ?
#print(df[df['Job']=='Lawyer'].info())

#How many people made the purchase during the AM and how many people made the purchase during PM

#print(df['AM or PM'].value_counts())

#What are the 5 most common Job Titles?

#print(df['Job'].value_counts().head(5))

#Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? **

#print(df[df['Lot']=='90 WT']['Purchase Price'])

#What is the email of the person with the following Credit Card Number: 4926535242672853

#print(df[df['Credit Card']==4926535242672853]['Email'])

#How many people have American Express as their Credit Card Provider *and* made a purchase above $95

#print(df[(df['CC Provider']=='American Express') & (df['Purchase Price']>95)].count())

#How many people have a credit card that expires in 2025

#print(df[df['CC Exp Date'].apply(lambda expiry: expiry[3:]=='25')].count()['CC Exp Date'])

#What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)

print(df['Email'].apply(lambda email: email.split('@')[1]).value_counts().head(5))