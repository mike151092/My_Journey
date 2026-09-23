#Logistic regression allow us to solve classification problem
#logistic regression varies between 0 to 1, so have a cut of value at 0.5 below which it is 0 and above which is 1
#f(z) = 1/(1+(e)^-z) is the sigmoid function
#Evaluvate classification model using a confusion matrix (True positive, True negative, False positive(Type 1 error) and False negatives(type 2 error))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,classification_report

df_train = pd.read_csv('titanic_train.csv')

print(df_train.head())
print(df_train.info())
print(df_train.describe())

#sns.heatmap(df_train.isnull(),yticklabels= False, cbar=False, cmap= 'viridis')

sns.set_style('whitegrid')
#sns.countplot(x= 'Survived', data= df_train, hue = 'Sex', palette='RdBu_r')
#sns.countplot(x= 'Survived', data= df_train, hue = 'Pclass')
#sns.displot(df_train['Age'].dropna(), kde = False, bins= 30)
#sns.countplot(x='SibSp', data= df_train)
#df_train['Fare'].hist(bins=40, figsize=(10,4))
#sns.boxplot(x='Pclass',y='Age',data= df_train)

def impute_age(cols):
    Age = cols['Age']
    Pclass = cols['Pclass']

    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age
    

df_train['Age'] = df_train[['Age','Pclass']].apply(impute_age,axis=1)

#sns.heatmap(df_train.isnull(), yticklabels=False,cbar=False, cmap='viridis')
df_train.drop('Cabin', axis= 1, inplace=True)
df_train.dropna(inplace=True)

sex = pd.get_dummies(df_train['Sex'],drop_first=True).astype(int) #used to convert classification string into 0 or 1 (eg Male to 1 and female to 0)
embark = pd.get_dummies(df_train['Embarked'],drop_first= True).astype(int)

df_train_cleaned = pd.concat([df_train,sex,embark], axis=1)

print(df_train_cleaned.info())

df_train_cleaned.drop(['Sex','Embarked','Name','Ticket','PassengerId'], axis=1, inplace=True)

print(df_train_cleaned.head())

X =df_train_cleaned.drop('Survived',axis=1)
y = df_train_cleaned['Survived']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=101)

logistic_model = LogisticRegression(max_iter=500)

logistic_model.fit(X_train,y_train)


predictions = logistic_model.predict(X_test)

print(classification_report(y_test,predictions))