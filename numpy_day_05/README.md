# Broadcasting and Rules.

## 📡 Broadcasting in Numpy Array.

## What is Broadcasting?

A broadcasting is a powerful mechanism that allows us to perform arithmetic operations on two or more arrays with different shapes and dimensions.This concept that used to perform broadcasting operations incredibly fast by two compatible arrays.
This mechanism is very important in machine learning for complex matrix operations, not all arrays are broadcastable we want to make some changes to our shapes and perform rules to be compatible by stretching smaller array virtually as same size of larger array.

## Rules to perform before performing operations.

Rule 1: Check always shape of two arrays before operations.

Rule 2: Observe the shape by `right-to-left`.

Rule 3: Check size of trailing and leading dimensions.The size of two array must match from column side and row side

Rule 4: Or either one of size must be one.

Rule 5: Then perform broadcasting operations.

## Example:
For suppose we have a two arrays with shape of (2,4) and (3,4) which are non compatible.

``A = np.arange(8).reshape(2,4)``
``B = np.arange(12).reshape(3,4)``


print(A - B) ## Here raises an error ``ValueError: Cannot broadcast arrays with shape (2,4) and (3,4).``

## Solution:

Since we have same size in column side but not satisfies row side rule.In that case we are using ``np.newaxis``.

``A = np.arange(8).reshape(2,4)[:, np.newaxis]``
``B = np.arange(12).reshape(3,4)[np.newaxis, :]``


## Strategies to Prevent Broadcasting.

* Use transpose function ```(.transpose() or .T)``` to inverse the arrays elements.
* Use ```np.newaxis``` to increase the dimension of an smaller array by row side ```[np.newaxis, :]``` and column side ```[:, np.newaxis]```
* Use ```reshape()``` method to manipulate arrays into compatible arrays.
