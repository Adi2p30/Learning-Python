import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model
import seaborn as sns
from sklearn import metrics
train = pd.read_csv('data/titanic_train.csv')
test = pd.read_csv('data/titanic_test.csv')
df = pd.DataFrame(train)
df1 = pd.DataFrame(test)
df1.insert(11,'Survived',0)
print(df.head())
#print(train)
print(df.columns)
# sns.set_style('whitegrid')
# (sns.countplot(x = 'Survived',hue='Embarked',data=train))
# plt.show()

sex = pd.get_dummies(df["Sex"],drop_first=True)
df = pd.concat([sex,df],axis=1)

sex1 = pd.get_dummies(df1["Sex"],drop_first=True)
print(sex1)
df1 = pd.concat([sex1,df1],axis=1)


def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]

    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age

df['Age'] = df[['Age','Pclass']].apply(impute_age,axis=1)
df.drop('Cabin',axis=1,inplace=True)

df1['Age'] = df1[['Age','Pclass']].apply(impute_age,axis=1)
df1.drop('Cabin',axis=1,inplace=True)

x_train = df[['Pclass', 'male', 'Age','Fare']]
y_train = df["Survived"]

x_test = df1[['Pclass', 'male', 'Age','Fare']]
y_test = df1["Survived"]

print("x_test.isnull")
print(x_test.isnull)
lm = sklearn.linear_model.LinearRegression()
lm.fit(x_train,y_train)




predicts =  lm.predict(x_test.head())
print(predicts)
# sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')

