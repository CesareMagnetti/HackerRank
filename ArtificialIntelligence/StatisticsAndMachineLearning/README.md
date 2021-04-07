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
