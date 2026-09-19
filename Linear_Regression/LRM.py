import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression   
from sklearn.metrics import mean_absolute_error, mean_squared_error


df = pd.read_csv("USA_Housing.csv")

print(df.head())
print(df.info())

#sns.pairplot(df)
#sns.displot(df['Price'],kde=True)

#plt.show()

print(df.columns)

X= df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]

y = df['Price']

X_train,X_test,y_train,y_test =train_test_split(X,y, test_size=0.4, random_state=101)

lm = LinearRegression()

lm.fit(X_train,y_train)

print(lm.intercept_)

print(lm.coef_)

CDF=pd.DataFrame(lm.coef_, X.columns, columns=['Coeff'])

print(CDF)

predictions = lm.predict(X_test)

print(predictions)

#plt.scatter(y_test,predictions)
sns.displot((y_test-predictions),kde = True) 

#plt.show()

print(mean_absolute_error(y_test,predictions))
print(mean_squared_error(y_test,predictions))