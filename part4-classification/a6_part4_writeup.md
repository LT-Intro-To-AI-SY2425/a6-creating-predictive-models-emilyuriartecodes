# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?

The model is less accurate because the the scales are very different and the model may give less importance to the EstimatedSalary feature (with much larger values), while ignoring the Age feature to some extent, leading to lower performance. Standardization ensures all features contribute equally to the learning process, improving the model's performance.

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.

If the accuracy score is above 80%, the model is likely performing well for the given use case, such as predicting SUV purchases based on age, estimated salary, and gender. However, if the accuracy is below 70%, the model may require improvement, which could involve gathering more data, exploring additional features, or tuning the model. 

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?

Errors were projected near the middle age range of the data set.

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.

No she would not.