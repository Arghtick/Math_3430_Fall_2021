import LA


    
def stable_GramSchmidt(mtx_1: list):
    """
    performs the stable version of Gram-Schmidt for reduced QR factorization

    first initializes a square matrix or zeros R equal to the columns of the input matrix
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
    scalar vec multiplication of the element of R and the vector at Q index

    Parameters
    ----------
    mtx_1 : list
        an input matrix stored as a list of lists

    Returns
    -------
    list
        the orthogonal matrix stored as the first element of list
        and the upper triangular matrix R stored as the second element of list
      
    """
    
    Q: list = []
    V: list = []
    R: list = []
    for element in mtx_1:
        R.append([0 for i in range(len(mtx_1))])
        
    
    for index in range(len(mtx_1)):
        V.append(mtx_1[index])
       
        #print(V[index])
    for index in range(len(mtx_1)):
        R[index][index] = LA.pNorm(V[index])
        Q.append(LA.scalar_vector_mult(1/R[index][index], V[index]))
        
        for inner_index in range(index +1 ,len(mtx_1)):
            R[inner_index][index] = LA.innerProd(Q[index], V[inner_index])
            V[inner_index] = LA.add_vectors(V[inner_index], LA.scalar_vector_mult(-R[inner_index][index], Q[index]))
    
    return [Q, R]


def orthonormal_vectorset(mtx_1: list):
    """
    creates an orthonormal list of vectors 

    first initializes a list of zeros R equal to the columns of the input list
    also initializes a zero list of equal size to the input list
    then for each element in the input list( appends the element of the input to V
    for each element in each element(vector) of the list (the corrosponding element of R
    is set to the inner product of vector of the Q list and V list
    V at the index is then set to the vector subtraction of itself and the scalar vector multiplication of 
    the scalar element in R list and the vector column element of Q)
    the diagonal elements of R are set to equal the norm of the V index)
    the orthoganal vector set Q is then set to be the list V divided by the diagonal scalar elements of R

    Parameters
    ----------
    mtx_1 : list
        an input matrix stored as a list of lists

    Returns
    -------
    list
        the orthogonal matrix stored as a list
        
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
    """Performs Householder triangularization

    Parameters
    ----------
    mtx : list
        A input matrix of floats

    Returns
    -------
    a list where first index is an orthogonal matrix Q and the second element 
    is an upper triangular matrix R

    """
    
    #m = len(mtx)
    #n = len(mtx[0])
    R:list = deep_copy(mtx)
    Q_list: list = []
    
    
    for k in range(len(R)):
        x: list = Q_builder(R,k)
        
        
        R = LA.matrix_matrix_mult(x, R)
        
        Q_list.append(x)
        
    
    Q: list = Q_list[-1]
    
    Q: list = conjugate_transpose(Q_list[0])
    
    for index in range (1, len(Q_list)):
        ct = conjugate_transpose(Q_list[index])
        Q = LA.matrix_matrix_mult(Q, ct)
    print([Q,R])
    print("~~~~~~~~~~~~~~~~~~~~~`")
    print(LA.matrix_matrix_mult(Q, R))
    return[Q,R]



def i_mtx(x: int)->list:
    i_list: list = [[0 for element in range(x)] for index in range(x)]
    for index in range(x):
       # for element in range(x):
        
        i_list[index][index] = 1
    return i_list
  
    
  
    
  
def sign(x: float)-> float:
    if x>=0:
        return 1
    else:
        return -1
    
def vec_vec_mult(vector_1, vector_2):
    result = []
    vector_1 == vector_2
    for x in range(len(vector_1)):
        result.append(LA.scalar_vector_mult(vector_1[x], vector_2))
    return result
    
def F_builder(vec: list)->list:
    s = -2/(LA.pNorm(vec))**2
    x = LA.scalar_matrix_mult(s, vec_vec_mult(vec, vec))
    y = LA.add_matrix(i_mtx(len(vec)), x)
    return y
    
def Q_builder(mtx:list, n: int):
    """
    builds a iteration of the orthogonal matrix Q
    
    Parameters
    ----------
    mtx : list
        in input matrix stored as a list of lists.
    n : int
        iteration index.

    Returns
    -------
     Q 

    """ 
    
    A:list = [[0 for j in range (n, len(mtx[i]))]for i in range(n,len(mtx))]
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            if n+i < len(mtx[i]):
                if n+j < len(mtx[i]):
                    A[i][j] = mtx[n+i][n+j]
    
    v = reflect_vec(A[0])
    
    f = F_builder(v)
    Q = i_mtx(len(mtx))
    for i in range(n,len(Q)):
        for j in range(n,len(Q)):
            Q[i][j] = f[i-n][j-n]
    return Q
    
    
def reflect_vec(vec: list)->list:
    e = [0 for element in range(len(vec))]
    e[0]=1
    v = LA.add_vectors(LA.scalar_vector_mult(sign(vec[0])*LA.pNorm(vec), e),vec)
    return v

def deep_copy(mtx:list)-> list:
    a: list = [[0 for element in range(len(mtx[0]))]for index in range(len(mtx))]
    for index in range(len(mtx)):
        for element in range(len(mtx[index])):
            a[index][element]= mtx[index][element]
    return a



def conjugate_transpose(mtx_1: list)-> list:
    con_mtx: list =[[0 for element in range(len(mtx_1[0]))]for index in range(len(mtx_1))]
    tran_mtx: list = [[0 for element in range(len(mtx_1[0]))]for index in range(len(mtx_1))]
    for i in range (len(mtx_1)):
        for j in range(len(mtx_1)):
            con_mtx[i][j]=(LA.conjugate(mtx_1[i][j]))
            
    for i in range (len(mtx_1)):
        for j in range(len(mtx_1)):
            tran_mtx[i][j]=(con_mtx[j][i])
    return tran_mtx


x = [[2,2,1],[-2,1,2],[18,0,0]]
householder(x)

    