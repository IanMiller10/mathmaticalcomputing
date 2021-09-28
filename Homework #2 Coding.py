# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Wed Sep 22 21:36:12 2021)---
import turtle
from turtle import *
forward(100)
right(90)
forward(100)

## ---(Mon Sep 27 20:02:20 2021)---
#Scalar Vector Multiplication
#We will multiply a vector named a_1 by a scalar named b
#We will store our result in a vector named my_result
import numpy as np
import math
a_1 = [1,2,3,4]
b=2
my_array = np.array(a_1)
a_2 = my_array * b
print (a_2)
a_1 = [5,6,7,8]
b=3
my_array = np.array(a_1)
a_2 = my_array * b
print (a_2)
a_1 = [9,10,11,12]
b=4
my_array = np.array(a_1)
a_2 = my_array * b
print (a_2)
end
END
#Scalar Matrix Multiplication
#We will multiply a matrix named a_1 by scalar b
#We will store the result in a matrix named a_2
import numpy as np
import math
a_1 = np.array([[1,2],[3,4]])
b=3
a_2 = b*a_1
print(a_2)
a_1 = np.array([[5,6],[7,8]])
b=4
a_2 = b*a_1
print(a_2)
a_1 = np.array([[9,10],[11,12]])
b=5
a_2 = b*a_1
print(a_2)
#Matrix Addition
#We will add two matrices names matrix_1 and matrix_2
#We will store the result in a matrix named matrix_result
import numpy as np
import math
matrix_1 = ([[1,2,3],[2,3,4]])
matrix_2 = ([[3,4,5],[5,6,7]])
matrix_result = np.add(matrix_1,matrix_2)
print(matrix_result)
matrix_1 = ([[8,9,10],[10,11,12]])
matrix_2 = ([[10,11,12],[12,13,14]])
matrix_result = np.add(matrix_1,matrix_2)
print(matrix_result)
matrix_1 = ([[15,16,17],[17,18,19]])
matrix_2 = ([[17,18,19],[19,20,21]])
matrix_result = np.add(matrix_1,matrix_2)
print(matrix_result)
#Matrix Vector Multiplication using the Linear Combination of Columns
#We will multiply a matrix named matrix_1 with a vector named vector_1
#We will transpose vector_1 to use the Linear Combination of Columns
#We will store the result in an array called result_array
import numpy as np
import math
matrix_1 = ([[1,2,3],[2,3,4],[3,4,5]])
vector_1 = [1,3,5]
vector_1trans = np.transpose(vector_1)
result_array = np.linalg.solve(matrix_1,vector_1trans)
print(result array)
print(result_array)
matrix_1 = ([[6,7,8],[7,8,9],[9,10,11]])
vector_1 = [7,9,11]
vector_1trans = np.transpose(vector_1)
result_array = np.linalg.solve(matrix_1,vector_1trans)
print(result_array)
#Matrix Matrix Multiplication
#We will multiply two matrices named matrix_1 and matrix_2
#We will store the result in a matrix named matrix_result
import numpy as np
import math
matrix_1 = np.array([[1,2],[3,4]])
matrix_2 = np.array([[5,6,7],[8,9,10]])
matrix_result = matrix_1.dot(matrix_2)
print(matrix_result)
matrix_1 = np.array([[5,6],[7,8]])
matrix_2 = np.array([[9,10,11],[12,13,14]])
matrix_result = matrix_1.dot(matrix_2)
print(matrix_result)