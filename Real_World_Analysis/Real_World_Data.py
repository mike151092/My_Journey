import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import folium
import matplotlib.patheffects as pe
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

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
total_export_25_26 =df['Exports_2025_26_USD_Bn'].sum()
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
'''top_10_states = df.sort_values('Exports_2025_26_USD_Bn',ascending=False).head(10)

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
plt.show()'''

##############################################
#Choroplet Plotting                          #
##############################################

df['Exports_2024_25_USD_Bn'] = (df['Exports_2024_25_USD_Mn']/1000)
print(df['Exports_2024_25_USD_Bn'])

total_export_24_25 =df['Exports_2024_25_USD_Bn'].sum()
print(f'Total FY24-25 exports: {total_export_24_25:.3f} Billion USD')
print(f'Total FY25-26 exports: {total_export_25_26:.3f} Billion USD')

#State share for each year
df['State_share_pct_24_25'] = (df['Exports_2024_25_USD_Bn']/total_export_24_25) * 100
print(df['State_share_pct_24_25'])

df['State_share_pct_25_26'] = (df['Exports_2025_26_USD_Bn']/total_export_25_26) * 100
print(df['State_share_pct_25_26'])

print(df[['State','State_share_pct_24_25','State_share_pct_25_26']])

df['State_share_change_pct_points'] = (df['State_share_pct_25_26']-df['State_share_pct_24_25'])

print(df.sort_values('State_share_change_pct_points',ascending=False))

india_map= gpd.read_file("./Real_World_Analysis/LGD_States.geojson")

print(india_map.shape)
print(india_map.columns)
print(india_map["STNAME"].tolist())
print(df["State"].tolist())

df['State_Join'] = df['State'].str.strip().str.title()

print(df['State_Join'])

india_map['State_Join'] = (india_map['STNAME'].str.strip().str.title())

print(sorted(set(df['State_Join'])-set(india_map["State_Join"])))
print(sorted(set(india_map["State_Join"])-set(df['State_Join'])))

state_mapping = {"Andaman & Nicobar": "Andaman And Nicobar Islands",
    "Dadra,Nagar Haveli,Daman & Diu": "Dadra & Nagar Haveli And Daman & Diu",
    "Jammu & Kashmir": "Jammu And Kashmir"}

india_map['State_Join'] = india_map['State_Join'].replace(state_mapping)

print(sorted(set(df['State_Join'])-set(india_map["State_Join"])))
print(sorted(set(india_map["State_Join"])-set(df['State_Join'])))

#Merging data

india_export_map = india_map.merge(df,on="State_Join",how='left')


print(india_export_map[['STNAME','State','Exports_2024_25_USD_Bn','Exports_2025_26_USD_Bn',
                        'State_share_pct_24_25','State_share_pct_25_26']].head())

print(india_export_map.shape)
print(india_export_map["State"].nunique())
print(india_export_map.geometry.isna().sum())

#############################################
# USED for Plots                            #
#############################################

label_offsets = {"West Bengal": (0.2, -1.2),"Assam": (2.0, 0.3),"Madhya Pradesh": (-0.5, -0.5),
                 'Andhra Pradesh': (0.0,-0.8),'Gujarat':(0.0,0.25),'Kerala':(0.0,-0.75),
                 "Dadra & Nagar Haveli and Daman & Diu": (1.8, -0.5)}

small_states = ["Andaman And Nicobar Islands","Chandigarh","Sikkim",
                "Tripura","Nagaland","Mizoram","Manipur","Meghalaya","Puducherry",
                'Delhi', 'Goa']
def add_callout(state, x_offset, y_offset):

    row = india_export_map[india_export_map["State"] == state].iloc[0]
    point = row.geometry.representative_point()

    ax.annotate(f"{state}\n"f"{row['State_share_pct_25_26']:.2f}%",xy=(point.x, point.y),
        xytext=(x_offset, y_offset),textcoords="offset points",fontsize=6.5,ha="center",va="center",
        arrowprops=dict(arrowstyle="-",linewidth=0.8))

#############################################
#Plot 1                                     #
#############################################
'''
fig, ax =plt.subplots(figsize=(14,10))

india_export_map.plot(column="State_share_pct_25_26",ax=ax,legend=True,cmap="managua",
                      linewidth=0.5,edgecolor='white')




for idx, row in india_export_map.iterrows():

    if row['State'] not in small_states:
        point = row.geometry.representative_point()
        dx, dy = label_offsets.get(row["State"],(0, 0))
        ax.text(point.x + dx,point.y + dy,f"{row['State']}\n{row['State_share_pct_25_26']:.2f}%",
                fontsize=6.5,ha="center",va="center")



add_callout("Sikkim", 10, 22)
add_callout("Tripura", 0, -30)
add_callout("Nagaland", 35, 5)
add_callout("Manipur", 35, -15)
add_callout("Mizoram", 35, -15)
add_callout("Meghalaya", -10, -20)
add_callout('Goa',-15,0)
add_callout('Delhi',20,0)
add_callout('Chandigarh',80,20)
add_callout('Puducherry',20,5)

ax.set_title('India State Export Share FY25-26',fontsize=22,fontweight='bold',pad=20)
ax.axis('off')
plt.show()'''
#############################################
# END of Plot 1                             #           
#############################################
india_export_map['Share_Change_pct_points'] = (india_export_map['State_share_pct_25_26']
                                               -india_export_map['State_share_pct_24_25'])

share_change = india_export_map[['State','State_share_pct_24_25',
                                 'State_share_pct_25_26',
                                 'Share_Change_pct_points']].sort_values('Share_Change_pct_points',ascending=False)

print(share_change)
print(share_change.head(5))
print(share_change.tail(5))
print(share_change.sort_values("Share_Change_pct_points",ascending=True).head(5))

max_change = india_export_map['Share_Change_pct_points'].abs().max()
print(max_change)

#############################################
#PLOT2                                      #
#############################################
'''
fig, ax =plt.subplots(figsize=(14,10))

india_export_map.plot(column="Share_Change_pct_points",ax=ax,legend=True,cmap="coolwarm",
                      linewidth=0.5,edgecolor='white',vmin = -max_change,vmax= max_change)


def format_change(x):
    if abs(x) < 0.005:
        return "0.00"
    elif x > 0:
        return f"+{x:.2f}"
    else:
        return f"{x:.2f}"

for idx, row in india_export_map.iterrows():
    if row['State'] not in small_states:
        point = row.geometry.representative_point()
        dx, dy = label_offsets.get(row["State"],(0, 0))
        ax.text(point.x + dx,point.y + dy,f"{row['State']}\n{format_change(row['Share_Change_pct_points'])}%",
        fontsize=8,ha="center",va="center")
add_callout("Sikkim", 10, 22)
add_callout("Tripura", 0, -30)
add_callout("Nagaland", 35, 5)
add_callout("Manipur", 35, -15)
add_callout("Mizoram", 35, -15)
add_callout("Meghalaya", -10, -20)
add_callout('Goa',-15,0)
add_callout('Delhi',20,0)
add_callout('Chandigarh',80,20)
add_callout('Puducherry',20,5)

ax.set_title('Change in State Export Share:  FY24-25 to FY25-26',fontsize=18,fontweight='bold',pad=20)
ax.axis('off')
plt.show()'''
#############################################
#END of PLOT2                               #
#############################################
summary = india_export_map[['State',"Exports_2024_25_USD_Bn",
                            "Exports_2025_26_USD_Bn",'State_share_pct_24_25',
                            'State_share_pct_25_26','Share_Change_pct_points']].copy()

summary['Export_Change_USD_Bn']= (summary['Exports_2025_26_USD_Bn']-summary['Exports_2024_25_USD_Bn'])

print(summary.sort_values('Export_Change_USD_Bn',ascending=False))
