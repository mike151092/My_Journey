import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression   
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error, explained_variance_score

df = pd.read_csv("Ecommerce Customers")

print(df.head())
print(df.info())
print(df.describe())

print(df.columns)

#sns.pairplot(df)
#sns.jointplot(data = df, x = 'Time on Website', y = 'Yearly Amount Spent')
#sns.jointplot(data = df, x = 'Time on App', y = 'Yearly Amount Spent')
#sns.jointplot(data=df, x = 'Time on App', y= 'Length of Membership', kind= 'hex')
#sns.lmplot(data=df, x = 'Length of Membership', y = 'Yearly Amount Spent')
#plt.show()

X = df[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]

y = df['Yearly Amount Spent']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

lm= LinearRegression()

lm.fit(X_train,y_train)

print(lm.intercept_)
print(lm.coef_)

CDF=pd.DataFrame(lm.coef_, X.columns, columns=['Coeff'])

print(CDF)

predictions = lm.predict(X_test)

#plt.scatter(y_test,predictions)
#plt.xlabel('Y Test')
#plt.ylabel('Predicted Value')
#plt.show()

print('MAE: ',mean_absolute_error(y_test,predictions) )
print('MSE: ', mean_squared_error(y_test,predictions))
print('RSME: ', root_mean_squared_error(y_test, predictions))

print(explained_variance_score(y_test,predictions))

sns.displot((y_test-predictions),kde = True) 


plt.show()