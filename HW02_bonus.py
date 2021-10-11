"""
Rider Jefferies
MATH-3430
For this homework assignment we will take our work from HW01 and use it to
prepare a python script which will implement our algoirthms as python functions. 

For Problems #0-5 from HW01, Do the following.



1) Write your answer from HW01 in a comment.

2) Below the comment write a function which implements the algorithm from your
comment. If you find that you need to change your algorithm for your python
code, you must edit your answer in the comment. 

3) Test each of your functions on at least 2 inputs. 

4) Upload your .py file to a github repo named "Math_3430_Fall_2021"

This assignment is due by 11:59pm 09/27/2021. Do NOT upload an updated version to github
after that date. 
"""


#Example:

#Problem 00

"""
-The Three Questions

Q1: What do we have?

A1: Two vectors stored as lists. Denoted by the names vector_a and vector_b. 

Q2: What do we want?

A2: Their sum stored as a list.

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and store the sums of
the corresponding components of vector_a and vector_b. 

-PsuedoCode

def add_vectors(vector_a,vector_b):

Initialize a result vector of 0's which is the same size as vector_a. Call this
vector result.

# Set each element of result to be equal to the desired sum.
for index in range(length(result)):
  result[index] = vector_a[index] + vector_b[index]

Return the desired result.
"""

def add_vectors(vector_a,vector_b):
  result = [0 for element in vector_a]
  for index in range(len(result)):
    result[index] = vector_a[index] + vector_b[index]
  return result

#End Example



#Problem 01
"""
Write an algorithm to implement scalar-vector multiplication.

Q1: What do we have?

A1: A scalar number and a vector stored as num_1 and a list Vec_1 

Q2: What do we want?

A2: The result of the scalar number multiplied through the vector stored in a list

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and store the result of the
scalar number multiplied by each element in the vector



#define the function/method/algorithm
def scalar_vector_mult(num_1,Vec_1):

# Initializing result as an empty list
result=[]


# Add an element to result for each element of Vec_1. Set that element to 0.
for element in Vec_1:
  append 0 to result


#Set each element of result to be equal to the multiplication of the scalar and the number
#at the vectors index 

for index in range(length(result)):
  result[index] = num_1 * Vec_1[index] 

# Return the desired result.
return result
"""

def scalar_vector_mult(num_1,Vec_1):

    result=[]
    result = [0 for element in Vec_1]
    
    for index in range(len(result)):
      result[index] = num_1 * Vec_1[index] 
      
    return result



#End Problem #1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Problem 02

"""
Write an algorithm to implement scalar-matrix multiplication.


Q1: What do we have?

A1: a Scalar number stored as num_1 and a matrix or a list of vectors stored as mtx_1

Q2: What do we want?

A2: the resulting matrix of the scalar multiplied throughout the matrix

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and for each index in the new list
store the product of the scalar number multiplied with the corrosponding index vector 
stored in mtx_1 using our previously defined function scalar_vector_mult()



def scalar_matrix_mult(num_1,mtx_1):

# Initializing result as an empty list
result=[]

# Add an element to result for each element of mtx_1. Set that element to 0.
for element in mtx_1:
  append 0 to result

#set each element of the result to be equal to the scalar vector multiplication of the scalar 
#with the vector stored in mtx_1 at the index

for index in range(length(result)):
  result[index] = scalar_vector_mult(num_1,mtx[index])

# Return the desired result.
return result
"""

def scalar_matrix_mult(num_1,mtx_1):

    result=[]
    
    result = [0 for element in mtx_1]
    
    for index in range(len(result)):
      result[index] = scalar_vector_mult(num_1,mtx_1[index])
    
    return result

#End Problem #2

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#Problem 03

"""
Write an algorithm to implement matrix addition.


Q1: What do we have?

A1: Two matrixs stored as lists of lists. Denoted by the names mtx_1 and mtx_2. 

Q2: What do we want?

A2: The matrix sum of the two matrix's stored as a new matrix (or list of lists).

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and for each index in the new list
store the vector addition for the index. we will go about getting the vector addition by 
using the function add_vectors(vector_a,vector_b) to add the vectors stored at each 
index of mtx_1 and mtx_2

 


def add_matrix(mtx_1,mtx_2):

# Initializing result as an empty list
result = []

# Add an element to result for each element of mtx_1. Set that element to 0.
for element in mtx_1:
  append 0 to result

# Set each element of result to be equal to the result of the vector addition of each 
# corrosponding vector at index for both matrix's

for index in range(length(result)):
  result[index] = add_vectors(mtx_1[index],mtx_2[index])

# Return the desired result.
return result
"""
def add_matrix(mtx_1,mtx_2):

    result = []
    
    result = [0 for element in mtx_1]
    
    for index in range(len(result)):
      result[index] = add_vectors(mtx_1[index],mtx_2[index])
   
    return result


#End Problem #3


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Problem 04

"""
Write an algorithm to implement matrix-vector multiplication using the linear
combination of columns method. You must use the algorithms from Problem #0 and
Problem #1.  


Q1: What do we have?

A1: a matrix stored as mtx_1 and a vector stored as vec_1

Q2: What do we want?

A2: the result of matrix-vector multiplication stored as a new vector

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and for each index in the new list,
store the vector-scalar multiplication into a temp vector, where the vector is each vector 
stored in mtx_1 and the scalar is each element of vec_1 and then vector-vector addition 
to add each result of scalar-vector multiplication into a single vector(list)

 


def matrix_vector_mult(mtx_1,vec_1):

# Initializing result as an empty list
result = []

# Initialize a temp list to helo the result of scalar vector mult
temp = []

# Add an element to temp for each element of vec_1. Set that element to 0.
for element in vec_1:
  append 0 to temp


# Add an element to result for each element of mtx_1. Set that element to 0.
for element in mtx_1:
  append 0 to result

#set the result to be the total vector addition for each scalar vector multiplication 
#
for index in range(length(temp)):
  
  temp = scalar_vector_mult(vec_1[index],mtx_1[index])
  result = add_vectors(result,temp)


# Return the desired result.
return result
"""

def matrix_vector_mult(mtx_1,vec_1):

    
    result = []
    
    temp = []
    
    temp = [0 for element in vec_1]
    
    result = [0 for element in mtx_1]
    
    for index in range(len(temp)):
      
      temp = scalar_vector_mult(vec_1[index],mtx_1[index])
      result = add_vectors(result,temp)
    
    return result

#End Problem #4


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Problem 05

"""
Write an algorithm to implement matrix-matrix multiplication using your
algorithm from Problem #4.  


Q1: What do we have?

A1: two matrix stored in mtx_1 and mtx_2

Q2: What do we want?

A2: the result of matrix-matrix multiplication stored as a new matrix(list of lists)

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and for each index in 
the new list store the matrix-vector multiplication vector, where the matrix 
is each mtx_1 and the vector is each element of mtx_2 

 


def matrix_matrix_mult(mtx_1,mtx_2):

# Initializing result as an empty list
result = []


# Add an element to result for each element of mtx_1. Set that element to 0.
for element in mtx_1:
  append 0 to result

#set each element in result to be the vector returned by matrix vector multiplication for each vector in matrix 2
for index in range(length(result)):
  
  result[index] = matrix_vector_mult(mtx_1,mtx_2[index])


# Return the desired result.
return result
"""

def matrix_matrix_mult(mtx_1,mtx_2):

    result = []    
    
    result = [0 for element in mtx_1]
    
    for index in range(len(result)):
      result[index] = matrix_vector_mult(mtx_1,mtx_2[index])
    
    return result


#End Problem #5

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Test Inputs

test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]
test_vector_03 = [5, 3, 1]
test_const_01 = 2
test_const_02 = 3
test_identity_mtx = [[1, 0, 0],[0, 1, 0],[0, 0, 1]]
test_matrix_01 = [test_vector_01, test_vector_02, test_vector_03]

# add_vectors(test_vector_01,test_vector_02) should output [4,3,6]
#problem 0
print('Test Output for add_vectors: ' + str(add_vectors(test_vector_01,test_vector_02)))
print('Should have been [4,3,6]')
print(" ")
print('Test Output for add_vectors: ' + str(add_vectors(test_vector_02,test_vector_03)))
print('Should have been [8,4,3]')
print(" ")
print("~~~~~~~~~~~~~~~")

#problem 1
print("Test Output for scalar_vector_mult: " + str(scalar_vector_mult(test_const_01, test_vector_01)))
print("Should have been [2,4,8]")
print(" ")
print("Test Output for scalar_vector_mult: " + str(scalar_vector_mult(test_const_02, test_vector_02)))
print("Should have been [9,3,6]")
print(" ")
print("~~~~~~~~~~~~~~~")

#problem 2
print("Test Output for scalar_matrix_mult " + str(scalar_matrix_mult(test_const_01,test_identity_mtx)))
print("Should have been [[2,0,0],[0,2,0],[0,0,2]]")
print(" ")
print("Test Output for scalar_matrix_mult " + str(scalar_matrix_mult(test_const_01,test_matrix_01)))
print("Should have been [[2,4,8],[6,2,4],[10,6,2]]")
print(" ")
print("~~~~~~~~~~~~~~~")

#Problem 3
print("Test Output for add_matrix: " + str(add_matrix(test_matrix_01,test_identity_mtx)))
print("Should have been [[2,2,4],[3,2,2],[5,3,2]]")
print(" ")
print("Test Output for add_matrix: " + str(add_matrix(test_matrix_01,test_matrix_01)))
print("Should have been [[2,4,8],[6,2,4],[10,6,2]]")
print(" ")
print("~~~~~~~~~~~~~~~")

#problem 4
print("Test Output for matrix_vector_mult: " + str(matrix_vector_mult(test_matrix_01,test_vector_01)))
print("Should have been [27, 16, 12]")
print(" ")
print("Test Output for matrix_vector_mult: " + str(matrix_vector_mult(test_matrix_01,test_vector_02)))
print("Should have been [16,13,16]")
print(" ")
print("~~~~~~~~~~~~~~~")

#problem 5
print("Test Output for matrix_matrix_mult: " + str(matrix_matrix_mult(test_matrix_01, test_identity_mtx)))
print("Should have been [[1,2,4],[3,1,2],[5,3,1]]")
print(" ")
print("Test Output for matrix_matrix_mult: " + str(matrix_matrix_mult(test_matrix_01, test_matrix_01)))
print("Should have been [[27,16,12],[16,13,16],[19,16,27]]")
print("~~~~~~~~~~~~~~~")
