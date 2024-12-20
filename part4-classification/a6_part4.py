import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Accesses the data, replaces gender values, and creates x and y variables
# Male = 0, Female = 1
data = pd.read_csv("part4-classification/suv_data.csv")
print(data)

# Gender column is transformed into numerical values: 0 for Male, 1 for Female
data['Gender'].replace(['Male','Female'],[0,1], inplace=True)
print(data)

# Define the feature variables (Age, EstimatedSalary, Gender) and the target variable (Purchased)
x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values

# Step 1: Standardizes the x values using StandardScaler
scaler = StandardScaler().fit(x)
x = scaler.transform(x)

# Step 2: Splits the data into a training and testing set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Step 3: Creates the logistic regression model and fits the data
model = linear_model.LogisticRegression().fit(x_train, y_train)

# Step 4: Prints the accuracy of the model
print("Accuracy:", model.score(x_test, y_test))
print("*************")
print("Testing Results:")
print("")

# Step 5: Prints out the actual and predicted values for the test data
print("Actual and Predicted Results:")
for index in range(len(x_test)):
    x_sample = x_test[index]
    x_sample = x_sample.reshape(1, -1)  # Reshape for prediction
    y_pred = int(model.predict(x_sample))

    # Convert numerical predictions back to meaningful labels
    if y_pred == 0:
        y_pred = "No Purchase"
    else:
        y_pred = "Purchased"
    
    actual = y_test[index]
    if actual == 0:
        actual = "No Purchase"
    else:
        actual = "Purchased"
    
    print(f"Predicted: {y_pred} | Actual: {actual}")
    print("")