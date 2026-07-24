# Day 06: Statistical Reductions

NumPy provides highly optimized functions to compute descriptive statistics. Understanding how to perform reductions globally or across specific dimensional axes is vital for aggregating and summarizing matrix data.

## Concepts Covered

### 1. Global vs. Axis-Targeted Reductions
* **Global Reductions**: Calling statistical functions directly on an array without specifying an axis flattens the dimensions and evaluates the entire dataset as a single pool of numbers.
* **The Axis Parameter**: Passing an axis parameter collapses that specific dimension. For a 2D matrix, `axis=0` operates downward across rows to evaluate columns, while `axis=1` operates horizontally across columns to evaluate rows.

### 2. Basic Descriptive Statistics
* `np.sum()`: Calculates the total arithmetic addition of elements.
* `np.mean()`: Computes the arithmetic average of elements.
* `np.median()`: Locates the middle value of a sorted distribution, preventing skew from outliers.

### 3. Measures of Dispersion
* `np.std()`: Computes the standard deviation, measuring the spread of data around the mean.
* `np.var()`: Evaluates the variance, representing the average squared deviations from the mean.

