#Demo.py

import LA
import QR
import LS


print("Hello, my name is Rider Jefferies");
print("This library is a collection of different linear algebra functions");
print("the function explinations and examples are below.");
print(" ");


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("add_vectors") 
print("takes in two vectors and returns their sum")
print("Example: ")
print("a = [1, 2, 4], b = [3, 1, 2] then add_vectors(a,b) returns:")
print(" ")
a = [1, 2, 4];
b = [3, 1, 2];
print(LA.add_vectors(a, b))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("scalar_vector_mult")
print("takes in a scalar and a vector and teturns their product")
print("Example: ")
print("x = 2, a = [1, 2, 4] then scalar_vector_mult returns:")
print(" ")
x = 2;
a = [1,2,4]
print(LA.scalar_vector_mult(x, a))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("scalar_matrix_mult") 
print("takes in a scalar and a matrix and returns their scalar-matrix multiplication")
print("Example: ")
print("x = 2, mtx = [[1, 2, 4],[3, 1, 2],[5, 3, 1]] then scalar_matrix_mult returns:")
print(" ")
x = 2;
mtx = [[1, 2, 4],[3, 1, 2],[5, 3, 1]];
print(LA.scalar_matrix_mult(x, mtx))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("add_matrix ")
print("takes in two matrix and returns thier sum")
print("Example: ")
print("a = [[1, 2, 4],[3, 1, 2],[5, 3, 1]], b = [[1, 2, 4],[3, 1, 2],[5, 3, 1]]")
print("add_matrix returns: ")
print(" ")
a = [[1, 2, 4],[3, 1, 2],[5, 3, 1]]
b = [[1, 2, 4],[3, 1, 2],[5, 3, 1]]
print(LA.add_matrix(a, b))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("matrix_vector_mult ")
print("takes in a matrix and a vector and returns matrix vector multiplication")
print("Example: ")
print("mtx = [[1, 2, 4],[3, 1, 2],[5, 3, 1]], vec = [1, 2, 4] then matrix_vector_mult")
print("returns:")
print(" ")
mtx = [[1, 2, 4],[3, 1, 2],[5, 3, 1]]
vec = [1, 2, 4]
print(LA.matrix_vector_mult(mtx, vec))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("matrix_matrix_mult")
print("takes in takes in two matrix and returns their matrix matrix multiplication")
print("Example: ")
print("mtx = [[1, 2, 4],[3, 1, 2],[5, 3, 1]] then matrix_matrix_mult returns:")
print(" ")
mtx = [[1, 2, 4],[3, 1, 2],[5, 3, 1]]
print(LA.matrix_matrix_mult(mtx, mtx))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("conjugate")
print("takes in a complex number and returns the complex conjugate")
print("Example: ")
print("x= 3 + 4j then conjugate returns:")
print(" ")
x = 3 + 4j;
print(LA.conjugate(x))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("absolute_value")
print("takes in a complex number and returns the absolute value")
print("Example: ")
print("x = 3 - 4j then absolute_value returns: ")
print(" ")
x = 3 - 4j;
print(LA.absolute_value(x))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("pNorm")
print("takes in a vector and a float and returns the p-norm of the vector,")
print("p is the float and defaults to 2.")
print("Example: ")
print("vec = [3 + 4j, 1, 4-3j] then pNorm returns")
print(" ")
vec = [3 + 4j, 1, 4-3j];
print(LA.pNorm(vec))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("infNorm")
print("takes in a vector and returns the infinity norm")
print("Example: ")
print("vec_1 = [3 + 4j, 1, 4-3j] then infNorm returns:")
print(" ")
vec_1 = [3 + 4j, 1, 4-3j]
print(LA.infNorm(vec_1))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("normSelect")
print("takes in a vector a float and a boolean and returns infinity norm")
print("if bool is true and returns p-norm if bool is false")
print("Example: ")
print("if vec_1 = [3 + 4j, 1, 4-3j], num_1 = 2, bool = False, then normSelect returns:")
print(" ")
vec_1 = [3 + 4j, 1, 4-3j]
num_1 = 2
print(LA.normSelect(vec_1,num_1,False))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("innerProd")
print("takes two vectors and returns the inner product.")
print("Example: ")
print("if vec_1 = [1, 2, 4], vec_2 = [5, 3, 1] then innerProd returns:")
print(" ")
vec_1 = [1, 2, 4]
vec_2 = [5, 3, 1]
print(LA.innerProd(vec_1, vec_2))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(" ")
print("~~~QR.py~~~")
print(" ")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("stable_GramSchmidt")
print("takes in a matrix and implements gram-schmidt and returns")
print("the Q, R matrices")
print("Example: ")
print("if mtx_1 = [[2,2,1],[-2,1,2],[18,0,0]] then stable_GramSchmidt returns:")
print(" ")
mtx_1 = [[2,2,1],[-2,1,2],[18,0,0]]
print(QR.stable_GramSchmidt(mtx_1))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("orthonormal_vectorset")
print("takes in a list of vectors returns orthonormal list of vectors")
print("Example: ")
print("if mtx_1 =  [[2,2,1],[-2,1,2],[18,0,0]] then orthonormal_vectorset returns:")
print(" ")
mtx_1 = [[2,2,1],[-2,1,2],[18,0,0]]
print(QR.orthonormal_vectorset(mtx_1))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("householder")
print("takes in a martix implements householder orthogonalization,")
print("returns the Q and R matrixes")
print("Example: ")
print("if mtx_1 = [[12,6,-4],[-51,167,24],[4,-68,-41]] then householder returns: ")
mtx_1 = [[12,6,-4],[-51,167,24],[4,-68,-41]]
print(" ")
print(QR.householder(mtx_1))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print(" ")
print("~~~LS.py~~~")
print(" ")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("least_squares")
print("takes in a matrix and a vector and returns the least squares solution")
print("Example: ")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
