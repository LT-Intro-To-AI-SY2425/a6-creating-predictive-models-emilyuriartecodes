# Part 2 - Training and Testing Data Writeup

After completing `a6_part2.py` answer the following questions

## Questions to answer

1. What makes this model more effective than the model you created in the previous lesson?

This model utilizes the train-split data technique in which is seperates the data bases and allows you to train the model on one subset of the data and test it on the other. This provides a more reliable way of evaluating the model’s performance.

2. What does the R squared coefficient tell you about the model?

The r-squared value tells us that the model is more accurate in its predictions that the first model in part.1 since its r-squared value is 0.85 and it's closer to 1.

3. Would you say that your model is accurate? What evidence supports your conclusion? Consider the meaning of the predicted and actual values in the context of the chart below from the American Heart Association’s website on understanding blood pressure.

I think this model is accurate becuase, not only is it's r-quared value closer to 1, but also, compared to the data given to us by the American Heart Association, its average for the blood pressure by age is closer to the predictions given to us by the graph. For example, the normal blood pressure (120) matches up with the ages that the AHA would normally classify as people who would have them (younge people).