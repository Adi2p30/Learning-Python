import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np

houseframe = pd.read_csv("../Data/USA_Housing.csv")
df = pd.DataFrame(houseframe)
#print(df)
#top 5
#print(df.head())

#structure of data frame
#print(df.info())

# imp information
#print(df.describe())

#list of columns from csv
#print(df.columns)

x = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]
#print(x)

y = df["Price"]
#print(y)

#Split data into training and testing set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=101)

# print(x_train)
# print(y_train)
# print(x_test)
# print(y_test)

lm = LinearRegression()

#Fit model for training data
lm.fit(x_train,y_train)

print(lm.intercept_)

#coefficient for feature
#print(lm.coef_)

cdf = pd.DataFrame(lm.coef_,x.columns,columns=["coef"])
print(cdf)

predicts = lm.predict(x_test)
plt.scatter(y_test,predicts)
#plt.show()

# plt.hist(y_test,predicts)
# plt.show()

# sns.distplot((y_test- predicts))
# print(sns)


print("mean_absolute_error", metrics.mean_absolute_error(y_test,predicts))
print("mean_squared_error", metrics.mean_squared_error(y_test,predicts))
print("sqrt mean_squared_error", np.sqrt(metrics.mean_squared_error(y_test,predicts)))
