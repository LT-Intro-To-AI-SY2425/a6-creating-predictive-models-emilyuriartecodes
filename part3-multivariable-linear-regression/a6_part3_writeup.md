# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?

0.86, yhis means that the model is relativley accurate in relation to the data.

2. Is your model accurate? Why or why not?

Yes becuse the r-squard is closer to 1.

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?

10yrs old / 89k miles : $10,305.90
20yrs old / 150k miles : $2,699.59


4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?

Linear regression models arent as equipped to outliers or values that fall outside the range of the data used to train the model. If there are no examples of cars in the dataset with extremly high values then the model cant really predict as accurate according to typical market values. 
