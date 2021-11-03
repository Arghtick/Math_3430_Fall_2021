# -*- coding: utf-8 -*-
"""
Name: Rider Jefferies

This homework is due on 10/15/2021 by 11:59pm. 


For this assignment you will be writing a python script to be named LA.py. In
this script you will need to write 6 functions. Every function must 

1) Have a doc string.

2) Have type annotations

3) Be tested using unit testing. 

Once you have finished writing LA.py you will upload it to the same github repo
you used for HW02. The functions you need to write are 

#0 A function which takes as it's arguments two vectors stored as
lists and returns their sum, also stored as a list.


#1 A function which takes as it's arguments a vector stored as a list and a
scalar, and returns the scalar vector multiplication stored as a list.


#2 A function which takes as it's arguments a matrix, stored as a list of lists
where each component list represents a column of the matrix(you cannot represent
the matrix as a list of rows!) and a scalar and returns their product, also
stored as a list of lists where each component list represents a column. You
must use the function from problem #1. Failure to use this function will result
in an earned grade of 0.

#3 A function which takes as it's arguments two matrices stored as lists of
lists where each component list represents a column vector, and returns their
sum stored in the same manner. You must use the function in problem #0 in your
method here. Failure to use the function from problem #0 will reuslt in an
earned grade of 0.

#4 A function which takes as it's argument a matrix (stored as a list of lists,
each component list representing a column vector), and a vector stored as a
list, and returns the matrix-vector product. This function must compute the
matrix-vector product by calculating the neccessary linear combination of the
input matrices columns. All other methods of matrix-vector multiplication are
strictly forbidden and their use will result in a grade of 0. For this function
you must use the functions written for problem #0 and problem #1. Failure to use
these functions will result in an earned grade of 0.

#5 A function which takes as it's arguments two matrices, each stored as a list
of lists where each component list represents a column vector, and returns their
product stored in the same manner. To earn any credit on this problem you must
use the function from problem #4 to implement the matrix-vector method of
matrix-matrix multiplication. Use of any other method will result in an earned
grade of 0.
"""


# Begin Example
# Problem #0

def add_vectors(vector_a: list, vector_b: list) -> list:
    """Adds the two input vectors.

    Creates a result vector stored as a list of 0's the same length as the input 
    then overwrites each element of the result vector with the corresponding
    element of the sum of the input vectors. Achieves this using a for loop over
    the indices of result. 

    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector, the same length as vector_a, stored as a list.

    Returns:
       The sum of the input vectors stored as a list. 
    """ 
    result: list = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result

# End Example
# Note that you must add unit tests for problem 0!!!!!

# Problem #1

def scalar_vector_mult(num_1: float,Vec_1: list) -> list:
    
    """multiplies the input scalar and input vector
    
    Creates an empty list of the size equal to the input list vector, then 
    takes the product of the input scalar number multiplied by each element 
    in the input vector and stores it in each element in the result list.
    uses a for loop to index through list. 
    
    Args:
        num_1: A scalar number as a float.
        Vec_1: A vector stored as a list of floats.
        
    Returns:
        The product of the input scalar and vector stored as a list
    """

    result: list = [0 for element in Vec_1]
    
    for index in range(len(result)):
        result[index] = num_1 * Vec_1[index]
      
    return result

#End Problem #1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Problem 02



def scalar_matrix_mult(num_1: float,mtx_1: list):
    
    """Multiplies input scalar times input matrix
    
    Creates an empty list of the size equal to the input list matrix, then 
    takes the product of the input scalar number multiplied by each element 
    in the input matrix and stores it in each element in the result list.
    uses a for loop and the scalar vector multiplication function to multiply 
    each index in input list.
    
    Args:
        num_1: A scalar number as a float.
        mtx_1: A matrix stored as a list of lists of floats.
        
    Returns:
        The product of input scalar and matrix stored as a list of lists of floats
    """
    
    result: list = [0 for element in mtx_1]
    
    for index in range(len(result)):
      result[index] = scalar_vector_mult(num_1,mtx_1[index])
    
    return result

#End Problem #2

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#Problem 03


def add_matrix(mtx_1: list,mtx_2: list):
    
    """
    Implements matrix + matrix addition.
    
    Create an empty list of the appropriate size equal to the input matrix
    for each index in the new list stores the vector addition for the index. 
    gets the vector addition by using the function add_vectors(vector_a,vector_b) 
    to add the vectors (lists of floats) stored at each index of mtx_1 and mtx_2

    Args:
        mtx_1: A matrix stored as a list of lists of floats.
        mtx_2: A matrix stored as a list of lists of floats.
        
    Returns:
        The sum of two matricies after matrix addition.
    """

    result: list = [0 for element in mtx_1]
    
    for index in range(len(result)):
      result[index] = add_vectors(mtx_1[index],mtx_2[index])
   
    return result


#End Problem #3


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Problem 04



def matrix_vector_mult(mtx_1: list,vec_1: list):

    """
    Implements matrix-vector multiplication using the linear combination of 
    columns method.
    
    
    Creates an empty result list of the appropriate size equal to the input vector
    then creates an empty temp list of size equal to the input vector 
    next for each index in the range of the temp list it stores the result of
    vector-scalar multiplication into the temp vector, where the vector is each
    vector(element) stored in mtx_1 and the scalar is each element of vec_1 list
    then stores result of vector-vector addition which adds each result of 
    the scalar-vector multiplication into a single result vector(list)
    
    Args:
        mtx_1: A matrix stored as a list of lists of floats.
        vec_1: A vector stored as a list of floats.
        
    Returns:
        the result of the matrix multiplied with a vector stored as a list of 
        floats
    """
    
    result: list = [0 for element in vec_1]
    
    temp: list = [0 for element in vec_1]
     
    
    for index in range(len(temp)):
      
      temp = scalar_vector_mult(vec_1[index],mtx_1[index])
      result = add_vectors(result,temp)
    
    return result

#End Problem #4


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Problem 05



def matrix_matrix_mult(mtx_1: list,mtx_2: list):
    
    """
    Implement matrix-matrix multiplication 
    
    Create an empty list result of the size equal to input matrix 1, and for 
    each index in the result list, it stores the return vector of the matrix-vector 
    multiplication algorithm, where the matrix 
    is mtx_1 and the vector is each element of mtx_2 
    
    Args:
       mtx_1: A matrix stored as a list of lists of floats.
       mtx_2: A matrix stored as a list of lists of floats. 
        
    Returns:
        the product of matrix x matrix multiplication stored as a list of lists
        of floats
    """

    result: list = [0 for element in mtx_1]
    
    for index in range(len(result)):
      result[index] = matrix_vector_mult(mtx_1,mtx_2[index])
    
    return result


#End Problem #5

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def conjugate(scalar: complex) -> complex:
    result = scalar.real
    result -=scalar.imag
    return result

#Problem 01

def absolute_value(num_1: complex) -> float:
    
    """
    figures the absolute value of a number 
    
    Create a result float that is equal to the square root of the real part
    of the complex number squared plus the imaginary part of the complex number
    squared
    
    Args:
       num_1: a number of complex type 
        
    Returns:
        the absolute value of a complex number stored as a float
    """
    
    result: float = (num_1.real**2 + num_1.imag**2)**(1/2)
    return result
    

      
#End Problem #1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    
#Problem 02

def pNorm(vec_1: list, num_1: float=2) -> float:
    
    """
    figures the pNorm of a vector and p = (a scalar number) 
    
    Create a result float that is origionally set to 0
    for each element in the input vector takes the absolute value of the element
    to the power of the input scalar
    then adds the resulting float to the result variable
    returns the num_1 root of the total result float 
    
    Args:
       vec_1: a list of real and/or complex numbers of complex type
       num_1: a scalar number of float type which defaults to 2 if no input
        
    Returns:
        the pNorm (stored as a float) of a vector where p is a scalar input 
    """
    
    result: float = 0
    for element in vec_1:
        result += absolute_value(element)** num_1
    return result**(1/num_1)
    

#End Problem #2



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Problem 03

def infNorm(vec_1: list) -> float:
    
    """
    figures the infinity Norm of a vector
    
    for each element in vector if the result is smaller than the element set the result to the element
    
    Args:
       vec_1: a list of real and/or complex numbers of complex type
        
    Returns:
        the infinity Norm of a vector (stored as a float)
    """
    result = 0
    for element in vec_1:
        if absolute_value(element)> result:
            result = absolute_value(element)
    return result
    

#End Problem #3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Problem 04

def normSelect(vec_1: list, num_1: float=2,isInf: bool=False)->float:
    
    """
    selects the function whether the norm is infinite or not
    
    if the norm is infinite return the result of the infiniy norm functin
    else the norm is NOT infinite return the result of the pNorm function
    
    Args:
       vec_1: a list of real and/or complex numbers of complex type
       num_1: a scalar of type float that defaults to 2 if no input arg
       inInf: a bool that defaults to False
        
    Returns:
        the result of the infinity norm or the p norm depending on if infinite
        or not
    """
    
    
    if isInf == True:
        return infNorm(vec_1)
    else:
        return pNorm(vec_1,num_1)
    
    

#End Problem #4

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   

#Problem 05



def innerProd(vec_1: list, vec_2: list)-> float:
    
    """
    calculates the inner product of two vectors
    
    creates a result of type float set to 0
    next for each index in range vec_1 add to result the product of the corresponding
    element of vector 1 multiplied with the element of vector 2 
    
    Args:
       vec_1: a list of real and/or complex numbers of complex type
       vec_2: a list of real and/or complex numbers of complex type
        
    Returns:
        the result of the inner product of the two vectors stored as a float
    """
    
    result: float = 0
    for index in range(len(vec_1)):
        result += vec_1[index].conjugate() *vec_2[index]
    
    return result

#End Problem #5


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     
