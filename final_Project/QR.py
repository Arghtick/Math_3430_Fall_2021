"""
Name: Rider Jefferies
Date: 12/8/2021


"""

import LA


    
def stable_GramSchmidt(mtx_1: list):
    """Performs the stable version of Gram-Schmidt for reduced QR factorization.

    First initializes a square matrix or zeros R equal to the columns of the input matrix
    also initializes a zero matrix of equal size to the input matrix
    then for each element in the input matrix( appends the element of the input to V matrix
    for each element in each element(vector) of the matrix
    for each index in the input matrix
    the corrosponding corrosponding element on the diagonal of R is set to the 
    norm of the V vector at index. the scalar vector multiplication of the 
    vector of V index divided by the element of R on the diagonal index
    for each inner index from the index +1 to the length of the matrix
    the corrosponding element in R is set the the inner product of Q index vector
    and V inner index vector. V at the inner index is then set to itself minus the 
    scalar vec multiplication of the element of R and the vector at Q index.

    Args:
        mtx_1 : an input matrix stored as a list of lists

    Returns:
        The orthogonal matrix stored as the first element of list
        and the upper triangular matrix R stored as the second element of list
      
    """
    
    Q: list = []
    V: list = []
    R: list = []
    for element in mtx_1:
        R.append([0 for i in range(len(mtx_1))])
        
    
    for index in range(len(mtx_1)):
        V.append(mtx_1[index])
       
        
    for index in range(len(mtx_1)):
        R[index][index] = LA.pNorm(V[index])
        Q.append(LA.scalar_vector_mult(1/R[index][index], V[index]))
        
        for inner_index in range(index +1 ,len(mtx_1)):
            R[inner_index][index] = LA.innerProd(Q[index], V[inner_index])
            V[inner_index] = LA.add_vectors(V[inner_index], LA.scalar_vector_mult(-R[inner_index][index], Q[index]))
    
    return [Q, R]


def orthonormal_vectorset(mtx_1: list):
    """Creates an orthonormal list of vectors 

    First initializes a list of zeros R equal to the columns of the input list
    also initializes a zero list of equal size to the input list
    then for each element in the input list( appends the element of the input to V
    for each element in each element(vector) of the list (the corrosponding element of R
    is set to the inner product of vector of the Q list and V list
    V at the index is then set to the vector subtraction of itself and the scalar vector multiplication of 
    the scalar element in R list and the vector column element of Q)
    the diagonal elements of R are set to equal the norm of the V index)
    the orthoganal vector set Q is then set to be the list V divided by the diagonal scalar elements of R.

    Args:
        mtx_1 : an input matrix stored as a list of lists.

    Returns:
        The orthogonal matrix stored as a list.
        
    """
    
    Q: list = []
    V: list = []
    R: list = []
    for element in mtx_1:
        R.append([0 for i in range(len(mtx_1))])
        Q.append([0 for i in range(len(element))])
    
    
    for index in range(len(mtx_1)):
        V.append(mtx_1[index])
        
        for inner_index in range(0,index):
            R[index][inner_index] = LA.innerProd(Q[inner_index], V[index])
            V[index] = LA.add_vectors(V[index], LA.scalar_vector_mult(-R[index][inner_index], Q[inner_index]))
        R[index][index] = LA.pNorm(V[index])
        Q[index] = (LA.scalar_vector_mult(1/R[index][index], V[index]))
    
    return Q


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def householder(mtx:list):
    """Performs householder decomposition of a input matrix.
    
    Copies the input matrix to R
    initialize Q list
    for each column in the input matrix
        set a list equal to the output of Q_builder
        set R equal to the output of the matrix matrix mutltiplication of x and R
        append x to Q_list
    take the conjugate transpose of the first element of the Q list 
    multiply the conjugate transpose of each element of Q list together and 
    store it in Q.
    
    Args:
       mtx: matrix of floats stored as a list of lists of floats.
       
        
    Returns:
        A List with the first element is a orthogonal matrix Q and the second
        element is an upper triangular matrix R. 
        Stored as a list of two lists of lists of floats.
        
    """
    
    R:list = deep_copy(mtx)
    Q_list: list = []
    for k in range(len(R)):
        x: list = Q_builder(R,k)
        R = LA.matrix_matrix_mult(x, R)
        Q_list.append(x)
        
    Q: list = conjugate_transpose(Q_list[0])
    
    for index in range (1, len(Q_list)):
        ct = conjugate_transpose(Q_list[index])
        Q = LA.matrix_matrix_mult(Q, ct)
    
    return[Q,R]



def i_mtx(x: int)->list:
    """Creates the identity matrix of input size.
    
    Creates a martix of zeros the size of input int then sets the diagonal
    elements to 1.

    Args:
        x: input size of identity matrix stored as int.

    Returns
        The identity matrix stored as a list of lists.
    """
    i_list: list = [[0 for element in range(x)] for index in range(x)]
    for index in range(x):
        i_list[index][index] = 1
    return i_list
  
    
  
    
  
def sign(x: float)-> float:
    """Figures if the input float is pos or neg.
    
    If input is greater than 0 returns 1, else (input is less than 0) 
    returns -1.
    
    Args:
        x: input number stored as a float.
        
    Returns:
        Either 1 if x is pos or -1 if x is negative.
    """
    if x>=0:
        return 1
    else:
        return -1
    
def vec_vec_mult(vector_1, vector_2):
    """Calculates the vector vector multiplication.
    
    For each element in vector_1 perform scalar vector multiplication and append
    retuned value to result
    
    Args: 
        vector_1: a input vector stored as a list of floats.
        vector_2: a input vector stored as a list of floats.
        
    Return:
        The result of vector vector multiplication stored as a list.
    """
    result: list = []
    
    for x in range(len(vector_1)):
        result.append(LA.scalar_vector_mult(vector_1[x], vector_2))
    return result
    


def F_builder(vec: list)->list:
    """Builds the F section of the orthogonal matrix Q.
    
    adds the identity matrix of size equal to input vec to the result of 
    (-2 divided by the pnorm of the vector squared) multiplied with 
    the input vector multiplied with itself.
    
    Args:    
        vec: input vector stored as a list of floats.

    Returns:
        A matrix stored as a list of lists.

    """
    s: float = -2/(LA.pNorm(vec))**2
    x: list = LA.scalar_matrix_mult(s, vec_vec_mult(vec, vec))
    y: list = LA.add_matrix(i_mtx(len(vec)), x)
    
    return y
    


def Q_builder(mtx:list, n: int):
    """Builds a iteration of the orthogonal matrix Q.
    
    for each index in the input matrix
        for the matrix within the column/row that is at the current itteration
        index coppies the input matrix
        for the F_builder taking in the reflect vector as its argument
        adds f to the lower right section of Q.
    
    Args:
        mtx: an input matrix stored as a list of lists.
        n : iteration index stored as a int.

    Returns:
        Matrix Q stored as a list of lists.

    """ 
    
    A:list = [[0 for j in range (n, len(mtx[i]))]for i in range(n,len(mtx))]
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            if n+i < len(mtx[i]):
                if n+j < len(mtx[i]):
                    A[i][j] = mtx[n+i][n+j]
    
    v: list = reflect_vec(A[0])
    
    f: list = F_builder(v)
    Q: list = i_mtx(len(mtx))
    for i in range(n,len(Q)):
        for j in range(n,len(Q)):
            Q[i][j] = f[i-n][j-n]
    return Q
    
    
def reflect_vec(vec: list)->list:
    """Calculates the reflection vector of a input vector.
    
    The sign of vector times the pNorm of the vector times the vector [1,0,...]
    added with the input vector.
    
    vec:
        an vector stored as a list of floats.

    Returns:
        The reflection of the input vector stored as a list of floats.

    """
    e: list = [0 for element in range(len(vec))]
    e[0]=1
    v: list = LA.add_vectors(LA.scalar_vector_mult(sign(vec[0])*LA.pNorm(vec), e),vec)
    return v



def deep_copy(mtx:list)-> list:
    """Deeply copies the input vector.
    
    Copies each index in the matrix to a new matrix.

    Args:
        mtx: an input matrix stored as a list of lists.
        

    Returns:
        A copy of input stored as a list of lists.

    """
    a: list = [[0 for element in range(len(mtx[0]))]for index in range(len(mtx))]
    for index in range(len(mtx)):
        for element in range(len(mtx[index])):
            a[index][element]= mtx[index][element]
    return a



def conjugate_transpose(mtx_1: list)-> list:
    """Performs the conjugate transpose of a matrix.

    Takes the conjugate for each element in the input matrix
    then transposes the matrix.
    

    Args:
        mtx_1: input matrix. 

    Returns:
        A matrix stored as a list of lists.

    """
    
    
    con_mtx: list =[[0 for element in range(len(mtx_1[0]))]for index in range(len(mtx_1))]
    tran_mtx: list = [[0 for element in range(len(mtx_1))]for index in range(len(mtx_1[0]))]
    for i in range (len(mtx_1)):
        for j in range(len(mtx_1[0])):
            x: complex = mtx_1[i][j]
            con_mtx[i][j]=(x.conjugate())
    for i in range (len(mtx_1[0])):
        for j in range(len(mtx_1)):
            tran_mtx[i][j]=(con_mtx[j][i])
    return tran_mtx

    