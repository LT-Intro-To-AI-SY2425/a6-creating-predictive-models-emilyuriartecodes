import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("part2-training-testing-data/blood_pressure_data.csv")

x = data["Age"].values.reshape(-1, 1)  # Reshape x to be a 2D array
y = data["Blood Pressure"].values

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(xtrain, ytrain)

coef = round(model.coef_[0], 2)
bias = round(model.intercept_, 2)

r_squared = round(model.score(xtrain, ytrain), 2)

print(f"Linear Equation: y = {coef} * Age + {bias}")
print(f"R-squared: {r_squared}")

'''
**********TEST THE MODEL**********
'''

xtest = xtest.reshape(-1, 1)

ypred = model.predict(xtest)

ypred_rounded = np.round(ypred, 2)

print("\nTesting Linear Model with Testing Data:")
for i in range(len(xtest)):
    print(f"Age: {xtest[i][0]} -> Predicted Blood Pressure: {ypred_rounded[i]}")

'''
**********CREATE A VISUAL OF THE RESULTS**********
'''
plt.figure(figsize=(8, 6))
plt.scatter(xtrain, ytrain, color='blue', label='Training Data')
plt.plot(xtrain, model.predict(xtrain), color='red', label=f"Regression Line: y = {coef} * Age + {bias}")
plt.scatter(xtest, ytest, color='green', label='Testing Data')
plt.title("Linear Regression: Blood Pressure vs Age")
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.legend()
plt.grid(True)
plt.show()