# Statistics and Machine Learning Questions from AI collection of HackerRank

## requirements

Popular Python libraries (i.e. numpy etc.) are used, you can make sure to download all required libraries by:

```python
pip install -r requirements.txt
```

```requirements.txt``` is located at the root of the repo.

## Predicting House Prices

This problem was a simple Linear Regression implementation, it was fitted through maximum likelyhood assuming gaussian iid datapoints (i.e. minimimizing the MSE between the ground truth and the model predictions).

**brief explanation:**<br>
- We have the following datapoints: 
1. X &isin; R<sup>NxF</sup>  = [x<sub>0</sub>, ... , x<sub>N</sub>] with x<sub>n</sub> &isin; R<sup>F</sup>
2. y &isin; R<sup>N</sup>
- A linear model can be expressed mathematically as h<sub>&theta;</sub>(X) = X&theta;, where &theta; &isin; R<sup>F</sup>.
-  We formulate the problem objective as &theta;<sup>*</sup> = argmin MSE
