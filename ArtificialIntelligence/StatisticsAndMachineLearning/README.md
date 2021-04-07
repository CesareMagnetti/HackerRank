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
1. **X** &isin; R<sup>NxF</sup>  = [**x**<sub>0</sub>, ... , **x**<sub>N</sub>] with **x**<sub>n</sub> = [1, x<sub>n</sub><sup>1</sup>, ..., x<sub>n</sub><sup>F-1</sup>] &isin; R<sup>F</sup>. The 1 takes care of the bias basis.
2. **y** &isin; R<sup>N</sup>
- A linear model can be expressed mathematically as h<sub>**&theta;**</sub>(**X**) = **X&theta;**, where **&theta;** &isin; R<sup>F</sup>.
-  We formulate the problem objective as **&theta;**<sup>*</sup> = argmin 0.5&sum;<sub>n=1</sub><sup>N</sup>(**&theta;**<sup>T</sup>x<sub>n</sub> - y<sub>n</sub>)<sup>2</sup> = 0.5(**X&theta;** - **y**)<sup>T</sup>(**X&theta;** - **y**)
- We then take derivatives w.r.t **&theta;**  and set to zero to find the minimum: **X**<sup>T</sup>(**X&theta;** - **y**) = 0
- Re-arrange to get optimal **&theta;**<sup>*</sup> = (**X**<sup>T</sup>**X**)<sup>-1</sup>**X**<sup>T</sup>**y**
- To make predictions then we simply evaluate h<sub>**&theta;**</sub>() at test points **X**<sub>test</sub> as **y**<sub>test</sub> = **X**<sub>test</sub>**&theta;**<sup>*</sup>

Therefore everything we need to do to build a linear regression model with linear basis functions id to extract the input data, arrange it to the above matrix form and apply the normal equation to estimate optimal parameters through maximum likelyhood estimation. Note that this is prone to overfitting and more advanced routines such as Maximum a Posteriori or Bayesian Linear Regression/Gaussian Processes are usually more situable.

**example input**
The input of the exercise consisted in the train and test datasets, for the training data the rightmost column was the house price. The first line of input (2 7) represents the number of features F (2) and the number of training points N (7). For the test set we have 4 test points.

2 7
0.18 0.89 109.85
1.0 0.26 155.72
0.92 0.11 137.66
0.07 0.37 76.17
0.85 0.16 139.75
0.99 0.41 162.6
0.87 0.47 151.77
4
0.49 0.18
0.57 0.83
0.56 0.64
0.76 0.18

**example output**
105.22
142.68
132.94
129.71

Simply copy and paste the example input after calling ```python MultipleLinearRegression_PredictingHousePricing.py```
