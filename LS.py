
"""
Name: Rider Jefferies
Date: 12/8/2021


"""

import LA
import QR



def leastSquare(mtx: list, vec: list):
    """Calculates the least squares solution of a martix.

    first takes the result of the stable_GramSchmidt function using the input matrix
    then splits up the Q and R parts. next takes the conjugate transpose of Q
    then the product of Q Transpose and the input vector
    finally takes the back substitution of the product vector and the triangular 
    matrix R.

    Args:
        mtx: A matrix stored as a list of lists of floats.
        vec: A vector stored as a list of floats.

    Returns:
        A vector result of the least squares stored as a list.
    """
    temp: list = QR.stable_GramSchmidt(mtx)
    Q: list= temp[0]
    R: list = temp[1]
    
    Q_tran: list = QR.conjugate_transpose(Q)
    Q_temp: list = LA.matrix_vector_mult(Q_tran, vec)
    
    result: list = backsub(R, Q_temp)
    return result
    


def backsub(mtx: list, vec: list):
    """Calculates the back substitution using a matrix and vector

    first divides the last element of the vector by the last element of the matrix
    and appends the quotient to the result list. Next for each index >1 subtract
    the elements to the right of the diagonal multiplied with the solution 
    next divide by the diagonal. Then append the quotient to the result list.
    finally flips the result and returns it

    Args:
        mtx: A matrix stored as a list of lists of floats.
        vec: A vector stored as a list of floats.

    Returns:
        A vector result of the back substitution stored as a list.
    """
    result: list = []
    a: float = 1/(mtx[len(mtx)-1][len(mtx[0])-1])
    temp: float = a * vec[len(vec)-1]
    result.append(temp)
    for index in range(1,len(mtx)):
        current: int = len(mtx) - 1 - index
        temp: float = vec[current]
        for solution_index in range(len(result)):
            temp -= mtx[len(mtx) - 1 - solution_index][current] * result[solution_index]
        temp = temp * (1/(mtx[current][current]))
        result.append(temp)
    new_temp: list = []
    for index in range(len(result)):
        new_temp.append(result[len(result) - 1 - index])
    
    result = new_temp
    return result
