import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("./Real_World_Analysis/india_state_exports_2025_26.csv")

#print(df.shape)
#print(df.info())
print(df.head())
#print(df.describe())
print(df.dtypes)
#print(df.isnull().sum())

sorted_25_26 = df.sort_values('Exports_2025_26_USD_Mn', ascending=False)

print(sorted_25_26)

df['calculated_YOY'] = ((df['Exports_2025_26_USD_Mn']-df['Exports_2024_25_USD_Mn'])/df['Exports_2024_25_USD_Mn'])*100 #calculated the diffrennce in 2024_25 and 2025_26

#print(df[["State","Exports_2024_25_USD_Mn","Exports_2025_26_USD_Mn","calculated_YOY"]])
print(df[["State","Growth_2025_26_vs_2024_25_pct","calculated_YOY"]])

print(df.loc[(df['State']=='Ladakh'), ['Exports_2024_25_USD_Mn','Exports_2025_26_USD_Mn','calculated_YOY','Growth_2025_26_vs_2024_25_pct']])

df['YOY_Difference'] = (df['calculated_YOY'] - df['Growth_2025_26_vs_2024_25_pct']) #Gives the difference between calculated data and data present in the dataset

print(df['YOY_Difference'])

print(df.sort_values(['YOY_Difference'], ascending= False))

df['Absolute_YOY_Difference'] = df['YOY_Difference'].abs() #absolute difference (chnage of sign)

print(df.sort_values("Absolute_YOY_Difference",ascending=False)[["State","calculated_YOY","Growth_2025_26_vs_2024_25_pct",
        "YOY_Difference", 'Absolute_YOY_Difference']])


print(df[df["Absolute_YOY_Difference"] > 0.1])

Sum_FY_25_26_States_Exports = df['Exports_2025_26_USD_Mn'].sum()

print(Sum_FY_25_26_States_Exports)

top_5 = df.sort_values('Exports_2025_26_USD_Mn',ascending=False).head(5)

print(top_5)

top_5_contributors = top_5['Exports_2025_26_USD_Mn'].sum()

print(top_5_contributors)

top_5_shares = (top_5_contributors/Sum_FY_25_26_States_Exports)*100



top_3 = df.sort_values('Exports_2025_26_USD_Mn',ascending=False).head(3)

top_3_contributors = top_3['Exports_2025_26_USD_Mn'].sum()

top_3_shares = (top_3_contributors/Sum_FY_25_26_States_Exports)*100

top_1_contributors = df['Exports_2025_26_USD_Mn'][0]

top_1_shares = (top_1_contributors/Sum_FY_25_26_States_Exports)*100

top_10 = df.sort_values('Exports_2025_26_USD_Mn',ascending=False).head(10)

top_10_contributors = top_10['Exports_2025_26_USD_Mn'].sum()

top_10_shares =(top_10_contributors/Sum_FY_25_26_States_Exports)*100

print(f'The contribution from the top state is {top_1_shares} %')
print(f'The contribution from the top  three state is  around {top_3_shares} %')
print(f'The contribution from the top five state is around {top_5_shares} %')
print(f'The contribution from the top ten state is around {top_10_shares} %')

df['Exports_2025_26_USD_Bn'] = (df['Exports_2025_26_USD_Mn']/1000) #vectorized operation

print(df['Exports_2025_26_USD_Bn'])

df['Export_Change_USD_Mn'] = (df['Exports_2025_26_USD_Mn']-df['Exports_2024_25_USD_Mn'])

print(df['Export_Change_USD_Mn'])

print(df.sort_values("Export_Change_USD_Mn",ascending=False)[["State","calculated_YOY","Exports_2025_26_USD_Mn",
        "Exports_2024_25_USD_Mn", 'Export_Change_USD_Mn']])

df['Export_Direction'] = np.where(df['Export_Change_USD_Mn']>0,"Increase","Decrease") #used to create an array based on the condition

print(df[["State", "Export_Change_USD_Mn", "Export_Direction"]])


print(df["Export_Direction"].value_counts())
##################################################
#                                                #
##################################################
total_state_increased_export =  (df["Export_Direction"].value_counts('Increase'))*100

print(total_state_increased_export)

increased_states = df[df['Export_Direction']=='Increase']

increased_exports = increased_states['Exports_2025_26_USD_Mn'].sum()

print(f"The export value for state that record increase in year 25 to 26 is:{increased_exports} Million Dollars")

total_export = df['Exports_2025_26_USD_Mn'].sum()

#print(Sum_FY_25_26_States_Exports )
print(f'The total export for 2025 to 26 is: {total_export} Million Dollars')

increased_export_share =(increased_exports/total_export)* 100

print(f'The share contributed by the state with increase in export for 2025 to 2026 is:{increased_export_share} %')

decreased_state = df[df['Export_Direction']=='Decrease']
decreased_exports = decreased_state['Exports_2025_26_USD_Mn'].sum()
print(f"The export value for state that record decrease in year 25 to 26 is:{decreased_exports} Million Dollars")

decreased_export_share = (decreased_exports/total_export)*100
print(f'The share contributed by the state with decrease in export for 2025 to 2026 is:{decreased_export_share} %')

total_share = increased_export_share + decreased_export_share
print(f'the value of share from both increased and decreased states is {total_share}%')

##############################################
#Visualization                               #
##############################################
top_10_states = df.sort_values('Exports_2025_26_USD_Bn',ascending=False).head(10)

print(top_10_states[['State','Exports_2025_26_USD_Bn']])


plt.figure(figsize=(20,10))
sns.barplot(data=top_10_states, x='Exports_2025_26_USD_Bn', y ='State')
plt.xlabel("Exports FY25-26 (USD Billion)",fontweight='bold')
plt.ylabel("State",fontweight='bold')
plt.title("Top 10 Indian States by Export - FY25-26",fontweight="bold")
#plt.xticks(fontweight="bold")
#plt.yticks(fontweight="bold")
for i, value in enumerate(top_10_states['Exports_2025_26_USD_Bn']):
        plt.text(value,i,f"${value:.2f}B",ha='left',va='center',fontsize=10)
plt.show()
