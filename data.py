import urllib
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


df = pd.read_csv('WHO-COVID-19-global-data.csv')
df_india = df[df.Country == 'India']

world_date = df_india.loc[(df_india["Date_reported"] >= '2021-01-01') & (df_india["Date_reported"] <= '2021-01-31')]
x=world_date["Date_reported"]
y=world_date["New_deaths"]
z=world_date["New_cases"]
x = np.arange(len(x))
fig, ax = plt.subplots()
graph1=plt.plot(x,y,color='red', linestyle='dotted', linewidth = 1,marker='o', markerfacecolor='red', markersize=2,label="deaths")
graph2=plt.plot(x,z,color='blue', linestyle='dotted', linewidth = 1,marker='o', markerfacecolor='blue', markersize=4,label="cases")
plt.xlabel("Jan 2021 (day's)", fontname="Gabriola", fontsize=18)
plt.ylabel("New Death's And Cases's In Jan 2021", fontname="Gabriola", fontsize=18)
plt.title("India's Covid Situation In January 2021",fontname='Franklin Gothic Medium', fontsize=18,y=1.10)
ax.set_xticks(x)
fig.tight_layout()
plt.legend()
plt.grid(color = 'g', linestyle = '--', linewidth = 0.5)
plt.show()


world_date = df_india.loc[(df_india["Date_reported"] >= '2021-01-01') & (df_india["Date_reported"] <= '2021-01-31')]
x=world_date["Date_reported"]
y=world_date["New_deaths"]
z=world_date["New_cases"]
x = np.arange(len(x))
fig, ax = plt.subplots()
plt.subplot(2, 1, 1)
graph2=plt.plot(x,z,color='blue', linestyle='dotted',linewidth = 1,marker='*', markerfacecolor='blue', ms=7,label="cases")
plt.ylabel("Cases's", fontname="Gabriola", fontsize=18,color="blue")

plt.subplot(2, 1, 2)
graph1=plt.plot(x,y,color='red', linestyle='dotted',linewidth = 1,marker='o', markerfacecolor='red', ms=5,label="deaths")
plt.xlabel("Jan 2021 (day's)", fontname="Gabriola", fontsize=18,color="blue")
plt.ylabel("Death's", fontname="Gabriola", fontsize=18,color="blue")

#ax.set_xticks(x)
fig.tight_layout()
plt.legend()
plt.grid(color = 'b', linestyle = '--', linewidth = 0.5)
plt.suptitle("India's Covid Situation In January 2021",fontname='Franklin Gothic Medium', fontsize=18,color="blue",y=1.10)
plt.show()


world_date = df_india.loc[(df_india["Date_reported"] >= '2021-01-01') & (df_india["Date_reported"] <= '2021-01-31')]
x = world_date["Date_reported"]
y = world_date["New_cases"]
z = world_date["New_deaths"]
x = np.arange(len(x))
fig,ax = plt.subplots()
plt.subplot(1, 2, 1)
plt.ylabel("New Death's And Cases's In Jan 2021", fontname="Gabriola", fontsize=18)
plt.xlabel("Jan 2021 (day's)", fontname="Gabriola", fontsize=18)
plt.title("Cases's")
plt.grid(linestyle = '--', linewidth = 0.6)
plt.bar(x,y,color="green",width=0.3)
plt.subplot(1, 2, 2)
plt.title("Death's")
plt.bar(x,z,color='r',width=0.3)
plt.xlabel("Jan 2021 (day's)", fontname="Gabriola", fontsize=18)
#plt.title("India's Covid Situation In January 2021",fontname='Franklin Gothic Medium', fontsize=18)
plt.grid(linestyle = '--', linewidth = 0.6)
plt.suptitle("India's Covid Situation In January 2021",fontname='Franklin Gothic Medium', fontsize=18,y=1.05)
fig.tight_layout()
plt.show()


world_date = df_india.loc[(df_india["Date_reported"] >= '2021-01-01') & (df_india["Date_reported"] <= '2021-01-31')]
x = world_date["Date_reported"]
y = world_date["New_cases"]
z = world_date["New_deaths"]
x = np.arange(len(x))
fig,ax = plt.subplots()
plt.subplot(2, 1, 1)
plt.ylabel("Cases's", fontname="Gabriola", fontsize=18)
plt.xlabel("Jan 2021 (day's)", fontname="Gabriola", fontsize=18)
plt.grid(linestyle = '--', linewidth = 0.6)
plt.bar(x,y,color="green",width=0.3)
plt.subplot(2, 1, 2)
plt.bar(x,z,color='r',width=0.3)
plt.xlabel("Jan 2021 (day's)", fontname="Gabriola", fontsize=18)
plt.ylabel("Death's", fontname="Gabriola", fontsize=18)
#plt.title("India's Covid Situation In January 2021",fontname='Franklin Gothic Medium', fontsize=18)
plt.grid(linestyle = '--', linewidth = 0.6)
plt.suptitle("India's Covid Situation In January 2021",fontname='Franklin Gothic Medium', fontsize=18)
fig.tight_layout()
plt.show()
