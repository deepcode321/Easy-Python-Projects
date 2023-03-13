#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv('https://github.com/deepcode321/datasets/raw/master/titanic.csv')
print("HI")
import matplotlib.pyplot as plt

plt.hist(df['Age'].dropna(), bins=20)
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()
survival_counts = df.groupby(['Survived', 'Pclass'])['PassengerId'].count().unstack()

survival_counts.plot(kind='bar', stacked=True)
plt.xlabel('Survival Status')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.legend(title='Passenger Class', loc='upper left')
plt.show()
colors = {'male': 'blue', 'female': 'red'}
plt.scatter(df['Age'], df['Fare'], c=df['Sex'].map(colors), alpha=0.5, s=100, edgecolors='none')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Age vs. Fare (colored by sex)')
plt.show()



# In[ ]:




