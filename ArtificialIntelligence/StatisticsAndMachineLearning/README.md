# Statistics and Machine Learning Questions from AI collection of HackerRank

## requirements

Popular Python libraries (i.e. numpy etc.) are used, you can make sure to download all required libraries by:

```python
pip install -r requirements.txt
```

```requirements.txt``` is located at the root of the repo.

## Correlation

No real explanation needed, just evaluating the correlation coefficient in python.

## Predicting House Prices

This problem was a simple Linear Regression implementation, it was fitted through maximum likelyhood assuming gaussian iid datapoints (i.e. minimimizing the MSE between the ground truth and the model predictions). Only requires ```NumPy```

**brief explanation:**<br>
- We have the following datapoints: 
1. **X** &isin; R<sup>NxF</sup>  = [**x**<sub>0</sub>, ... , **x**<sub>N</sub>] with **x**<sub>n</sub> = [1, x<sub>n</sub><sup>1</sup>, ..., x<sub>n</sub><sup>F</sup>] &isin; R<sup>F</sup>. The 1 takes care of the bias basis.
2. **y** &isin; R<sup>N</sup>
- A linear model can be expressed mathematically as h<sub>**&theta;**</sub>(**X**) = **X&theta;**, where **&theta;** &isin; R<sup>F</sup>.
-  We formulate the problem objective as **&theta;**<sup>*</sup> = argmin 0.5&sum;<sub>n=1</sub><sup>N</sup>(**&theta;**<sup>T</sup>x<sub>n</sub> - y<sub>n</sub>)<sup>2</sup> = 0.5(**X&theta;** - **y**)<sup>T</sup>(**X&theta;** - **y**)
- We then take derivatives w.r.t **&theta;**  and set to zero to find the minimum: **X**<sup>T</sup>(**X&theta;** - **y**) = 0
- Re-arrange to get optimal **&theta;**<sup>*</sup> = (**X**<sup>T</sup>**X**)<sup>-1</sup>**X**<sup>T</sup>**y**
- To make predictions then we simply evaluate h<sub>**&theta;**</sub>() at test points **X**<sub>test</sub> as **y**<sub>test</sub> = **X**<sub>test</sub>**&theta;**<sup>*</sup>

Therefore everything we need to do to build a linear regression model with linear basis functions id to extract the input data, arrange it to the above matrix form and apply the normal equation to estimate optimal parameters through maximum likelyhood estimation. Note that this is prone to overfitting and more advanced routines such as Maximum a Posteriori or Bayesian Linear Regression/Gaussian Processes are usually more situable.

**example input**<br>
The input of the exercise consisted in the train and test datasets, for the training data the rightmost column was the house price. The first line of input (2 7) represents the number of features F (2) and the number of training points N (7). For the test set we have 4 test points.<br>
Simply copy and paste the example input after calling ```python MultipleLinearRegression_PredictingHousePricing.py```

2 7<br>
0.18 0.89 109.85<br>
1.0 0.26 155.72<br>
0.92 0.11 137.66<br>
0.07 0.37 76.17<br>
0.85 0.16 139.75<br>
0.99 0.41 162.6<br>
0.87 0.47 151.77<br>
4<br>
0.49 0.18<br>
0.57 0.83<br>
0.56 0.64<br>
0.76 0.18<br>

**example output**<br>
105.22<br>
142.68<br>
132.94<br>
129.71<br>

## Polynomial Regression: Office Prices
This problem builds up on the above linear regression by introducing basis functions, polynomials in this case. Again, it was fitted through maximum likelyhood assuming gaussian iid datapoints (i.e. minimimizing the MSE between the ground truth and the model predictions). Only requires ```NumPy```

**brief explanation:**<br>
- We have the following datapoints: 
1. **X** &isin; R<sup>NxF</sup>  = [**x**<sub>1</sub>, ... , **x**<sub>N</sub>] with **x**<sub>n</sub> = [x<sub>n</sub><sup>1</sup>, ..., x<sub>n</sub><sup>F</sup>] &isin; R<sup>F</sup>.
2. **y** &isin; R<sup>N</sup>
- Build the basis function matrix **&Phi;** = [&phi;(**x**<sub>1</sub>)<sup>T</sup>, ... , &phi;(**x**<sub>N</sub>)<sup>T</sup>] &isin; R<sup>NxD</sup>, where the basis functions &phi;(**x**<sub>i</sub>)<sup>T</sup> = [1, x<sub>i</sub><sup>1</sup>, ... , x<sub>i</sub><sup>F</sup>, x<sub>i</sub><sup>1</sup>x<sub>i</sub><sup>2</sup>, ... &prod;<sub>j</sub>x<sub>i</sub><sup>j</sup>] &isin; R<sup>D</sup> are really a design choice. In this case they were p<sup>th</sup> order polynomials but really it could be any sensible function (i.e. gaussian RBF basis are a common choice due to their local properties).
- The model can again be expressed as a linear combination of weights and basis functions as h<sub>**&theta;**</sub>(**X**) = **&Phi; &theta;**, where **&theta;** &isin; R<sup>D</sup>.
-  We formulate the problem objective as **&theta;**<sup>*</sup> = argmin 0.5&sum;<sub>n=1</sub><sup>N</sup>(**&theta;**<sup>T</sup> &phi;(**x**<sub>n</sub>)<sup>T</sup> - y<sub>n</sub>)<sup>2</sup> = 0.5(**&Phi; &theta;** - **y**)<sup>T</sup>(**&Phi; &theta;** - **y**)
- We then take derivatives w.r.t **&theta;**  and set to zero to find the minimum: **&Phi;**<sup>T</sup>(**X&theta;** - **y**) = 0
- Re-arrange to get optimal **&theta;**<sup>*</sup> = (**&Phi;**<sup>T</sup>**&Phi;**)<sup>-1</sup>**&Phi;**<sup>T</sup>**y**
- To make predictions then we simply evaluate h<sub>**&theta;**</sub>() at test points **X**<sub>test</sub> as **y**<sub>test</sub> = **&Phi;**<sub>test</sub>**&theta;**<sup>*</sup>

As you can see the problem formulation is still linear and the only difference compared to the previous linear regression is that we now have a basis matrix **&Phi;** &isin; R<sup>NxD</sup> instead of simply having the data **X** &isin; R<sup>NxF</sup>. You can fit it to the same data as the previous exercise and see the change in outcome.
