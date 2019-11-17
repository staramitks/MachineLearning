# Load libraries
import pandas as pd
from sklearn import linear_model
import numpy as np
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report, mean_squared_error

# Load dataset
print("loading dataset")

names = ['Area', 'Rooms', 'Cost']
dataset = pd.read_csv("C:/Amit/ML-Data/HouseData.csv", names=names)
# shape
print("Data Set shape is ", dataset.shape)
# head
print("Data Set head is ", dataset.head(20))
# descriptions
print("Description", dataset.describe())

# train, test = train_test_split(dataset, test_size=0.2)

dataset.hist()
plt.show()
# # scatter plot matrix
scatter_matrix(dataset)
plt.show()
areaList = dataset[['Area', 'Rooms']]
#
# # areaList = areaList.reshape(len(areaList),1)
# print ("updated list is ", areaList)
costList = dataset['Cost']
#
# print("Area is ", areaList)
#
# print ("Cost list ", costList)
#
area_train_x_data = areaList[1:81]
area_test_x_data = areaList[81:]
cost_train_y_data = costList[1:81]
cost_test_y_data = costList[81:]
model=linear_model.LinearRegression()
model.fit(area_train_x_data, cost_train_y_data)
cost_prediction = model.predict(area_test_x_data)

print("RMSE is", mean_squared_error(cost_test_y_data, cost_prediction))

print ("weight is ", model.coef_)
print("intercept is ", model.intercept_)
print ("Predicted Value ", model.predict(np.array([[5674, 1]])))

