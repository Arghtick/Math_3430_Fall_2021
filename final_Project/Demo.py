
"""
Name: Rider Jefferies
Date: 12/8/2021


"""

import LA
import QR
import LS


print("Hello, my name is Rider Jefferies");
print("This library is a collection of different linear algebra functions");
print("the function explinations and examples are below.");
print(" ");

print(" ")
print("~~~LA.py~~~")
print(" ")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("add_vectors") 
print(" ")
print("takes in two vectors and returns their sum")
print("Example: ")
print("vector_a = [1, 2, 4], vector_b = [3, 1, 2] then add_vectors(a,b) returns:")
print(" ")
vector_a: list = [1, 2, 4];
vector_b: list = [3, 1, 2];
print(LA.add_vectors(vector_a, vector_b))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("scalar_vector_mult")
print(" ")
print("takes in a scalar and a vector and teturns their product")
print("Example: ")
print("num_1 = 2, vec_1 = [1, 2, 4] then scalar_vector_mult returns:")
print(" ")
num_1: float = 2;
vec_1: list = [1,2,4]
print(LA.scalar_vector_mult(num_1, vec_1))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("scalar_matrix_mult") 
print(" ")
print("takes in a scalar and a matrix and returns their scalar-matrix multiplication")
print("Example: ")
print("if num_1 = 2, mtx_1 = [[1, 2, 4],[3, 1, 2],[5, 3, 1]] then scalar_matrix_mult returns:")
print(" ")
num_1: float = 2;
mtx_1: list = [[1, 2, 4],[3, 1, 2],[5, 3, 1]];
print(LA.scalar_matrix_mult(num_1, mtx_1))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("add_matrix ")
print(" ")
print("takes in two matrix and returns thier sum")
print("Example: ")
print("mtx_1 = [[1, 2, 4],[3, 1, 2],[5, 3, 1]], mtx_2 = [[1, 2, 4],[3, 1, 2],[5, 3, 1]]")
print("add_matrix returns: ")
print(" ")
mtx_1: list = [[1, 2, 4],[3, 1, 2],[5, 3, 1]]
mtx_2: list = [[1, 2, 4],[3, 1, 2],[5, 3, 1]]
print(LA.add_matrix(mtx_1, mtx_2))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("matrix_vector_mult ")
print(" ")
print("takes in a matrix and a vector and returns matrix vector multiplication")
print("Example: ")
print("mtx_1 = [[1, 2, 4],[3, 1, 2],[5, 3, 1]], vec_1 = [1, 2, 4] then matrix_vector_mult")
print("returns:")
print(" ")
mtx_1: list = [[1, 2, 4],[3, 1, 2],[5, 3, 1]]
vec_1: list = [1, 2, 4]
print(LA.matrix_vector_mult(mtx_1, vec_1))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("matrix_matrix_mult")
print(" ")
print("takes in takes in two matrix and returns their matrix matrix multiplication")
print("Example: ")
print("if mtx_1 = mtx_2 = [[1, 2, 4],[3, 1, 2],[5, 3, 1]] then matrix_matrix_mult returns:")
print(" ")
mtx_1: list = [[1, 2, 4],[3, 1, 2],[5, 3, 1]]
mtx_2: list = [[1, 2, 4],[3, 1, 2],[5, 3, 1]]
print(LA.matrix_matrix_mult(mtx_1, mtx_2))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("absolute_value")
print(" ")
print("takes in a complex number and returns the absolute value")
print("Example: ")
print("num_1 = 3 - 4j then absolute_value returns: ")
print(" ")
num_1: complex = 3 - 4j;
print(LA.absolute_value(num_1))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("pNorm")
print(" ")
print("takes in a vector and a float and returns the p-norm of the vector,")
print("p is the float and defaults to 2.")
print("Example: ")
print("vec_1 = [3 + 4j, 1, 4-3j] then pNorm returns")
print(" ")
vec_1: list = [3 + 4j, 1, 4-3j];
print(LA.pNorm(vec_1))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("infNorm")
print(" ")
print("takes in a vector and returns the infinity norm")
print("Example: ")
print("vec_1 = [3 + 4j, 1, 4-3j] then infNorm returns:")
print(" ")
vec_1: list = [3 + 4j, 1, 4-3j]
print(LA.infNorm(vec_1))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("normSelect")
print(" ")
print("takes in a vector a float and a boolean and returns infinity norm")
print("if bool is true and returns p-norm if bool is false")
print("Example: ")
print("if vec_1 = [3 + 4j, 1, 4-3j], num_1 = 2, bool = False, then normSelect returns:")
print(" ")
vec_1: list = [3 + 4j, 1, 4-3j]
num_1: float = 2
print(LA.normSelect(vec_1,num_1,False))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("innerProd")
print(" ")
print("takes two vectors and returns the inner product.")
print("Example: ")
print("if vec_1 = [1, 2, 4], vec_2 = [5, 3, 1] then innerProd returns:")
print(" ")
vec_1: list = [1, 2, 4]
vec_2: list = [5, 3, 1]
print(LA.innerProd(vec_1, vec_2))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(" ")
print("~~~QR.py~~~")
print(" ")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("stable_GramSchmidt")
print(" ")
print("takes in a matrix and implements gram-schmidt and returns")
print("the Q, R matrices")
print("Example: ")
print("if mtx_1 = [[2,2,1],[-2,1,2],[18,0,0]] then stable_GramSchmidt returns:")
print(" ")
mtx_1: list = [[2,2,1],[-2,1,2],[18,0,0]]
print(QR.stable_GramSchmidt(mtx_1))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("orthonormal_vectorset")
print(" ")
print("takes in a list of vectors returns orthonormal list of vectors")
print("Example: ")
print("if mtx_1 =  [[2,2,1],[-2,1,2],[18,0,0]] then orthonormal_vectorset returns:")
print(" ")
mtx_1: list = [[2,2,1],[-2,1,2],[18,0,0]]
print(QR.orthonormal_vectorset(mtx_1))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("householder")
print(" ")
print("takes in a martix implements householder orthogonalization,")
print("returns the Q and R matrixes")
print("Example: ")
print("if mtx_1 = [[12,6,-4],[-51,167,24],[4,-68,-41]] then householder returns: ")
mtx_1: list = [[12,6,-4],[-51,167,24],[4,-68,-41]]
print(" ")
print(QR.householder(mtx_1))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("i_mtx")
print(" ")
print("takes in a integer number and returns the identity matrix of input size")
print("Example: ")
print("if x = 3 then i_mtx returns:")
print(" ")
x: int = 3
print(QR.i_mtx(x))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("sign")
print(" ")
print("takes in a integer number and returns 1 if input is positive and -1 else")
print("Example: ")
print("if x = -5 then i_mtx returns:")
print(" ")
x: float = -5
print(QR.sign(x))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("F_builder")
print(" ")
print("takes in a vector and builds the F part of orthogonal matrix Q")
print("Example: ")
print("if vec = [5,2,1] then F_builder returns:")
print(" ")
vec: list = [5,2,1] 
print(QR.F_builder(vec))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("Q_builder")
print(" ")
print("takes in a matrix and a integer and returns a iteration of the orthogonal matrix Q")
print("Example: ")
print("if mtx = [[2, 2, 1], [-2, 1, 2], [18, 0, 0]] and n = 0 then Q_builder returns:")
print(" ")
mtx: list = [[2, 2, 1], [-2, 1, 2], [18, 0, 0]]
n: int = 0
print(QR.Q_builder(mtx, n))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("reflect_vec")
print(" ")
print("takes in a vector and calculates the reflection of the vector")
print("Example: ")
print("if vec = [2,3,1] then reflect_vec returns:")
print(" ")
vec: list = [2,3,1]
print(QR.reflect_vec(vec))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("deep_copy")
print(" ")
print("takes in a matrix and copies it and returns the copy")
print("Example: ")
print("if mtx = [[1,2,3],[4,5,6],[7,8,9]] then deep_copy returns:")
print(" ")
mtx: list = [[1,2,3],[4,5,6],[7,8,9]]
print(QR.deep_copy(mtx))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("conjugate_transpose")
print(" ")
print("takes in a matrix and returns the conjugate transpose of the matrix")
print("Example: ")
print("if mtx_1 = [[1-2j,2,3+ 4j],[4,5-2j,6]] then conjugate_transpose returns:")
print(" ")
mtx_1: list = [[1-2j,2,3+ 4j],[4,5-2j,6]]
print(QR.conjugate_transpose(mtx_1))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


print(" ")
print("~~~LS.py~~~")
print(" ")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("least_squares")
print(" ")
print("takes in a matrix and a vector and returns the least squares solution")
print("Example: ")
print("if mtx = [[-1,2,-1],[2,-3,3]] and vec = [4,1,2] then leastSquare returns:")
print(" ")
mtx: list = [[-1,2,-1],[2,-3,3]]
vec: list = [4,1,2]
print(LS.leastSquare(mtx, vec))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("backsub")
print(" ")
print("takes in a matrix and a vector returns the back substitution using the two")
print("Example: ")
print("if mtx = [[1,0,0],[2,3,0],[4,5,6]] and vec =  [7,8,9] then backsub returns:")
print(" ")
mtx: list = [[1,0,0],[2,3,0],[4,5,6]]
vec: list =  [7,8,9]
print(LS.backsub(mtx, vec))
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

