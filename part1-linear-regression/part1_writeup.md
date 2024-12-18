# Part 1 - Linear Regression Writeup

After completing `a6_part1.py` answer the following questions

## Questions to answer

1. What is the r squared value?  What does this say about this linear regression model?

The r-squared value is 0.63. This value means that the deviation that the line of best fit has from the actual data point. This value is measured from a scale of 0-1; with 1 meaning that all the data points are located on the line of best fit and 0 meaning thta it is extremly far from the actual data points (AKA not a good line of best fit). The r-squared value being 0.63 shows that te line of best fit doesnt align with the data points too much, this is due to the lack of more information.

2. According to your model, what is the predicted systolic blood pressure for a person who is 42 years old?

137

3. How accurate do you think this model's predictions are?  Do you think this model is accurate enough to reliably predict someone's blood pressure based on their age?  Why or why not?  And if not, what could improve the model?

I dont think they're too accurate considering the average blood pressure for a 43 year old in 122 (in real life). The real relationship between blood pressure and age depends on many helath factors than go beyond just age. Not to mention that this model shows a linear relationship which largly generalizes the data. Adding more factors like weight, gender, and lifestyle can make this model more accurate when it comes to predicting blood pressure.