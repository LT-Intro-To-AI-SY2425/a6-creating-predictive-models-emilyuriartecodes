import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")

x = data["Age"].values
y = data["Blood Pressure"].values

x = x.reshape(-1, 1)

model = LinearRegression().fit(x, y)

coef = round(float(model.coef_[0]), 2)
intercept = round(float(model.intercept_), 2)
r_squared = round(model.score(x, y), 2)

print(f"Linear Equation: y = {coef} * x + {intercept}")
print(f"R-squared: {r_squared}")

age_to_predict = 43
predicted_blood_pressure = model.predict(np.array([[age_to_predict]]))
print(f"Predicted blood pressure for a 43-year-old: {round(predicted_blood_pressure[0], 2)}")

plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, model.predict(x), color='red', label='Line of Best Fit')
plt.xlabel('Age')
plt.ylabel('Blood Pressure')
plt.title('Blood Pressure vs Age')
plt.legend()
plt.show()

# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 


# Print out the linear equation and r squared value

# Predict the the blood pressure of someone who is 43 years old.
# Print out the prediction

# Create the model in matplotlib and include the line of best fit