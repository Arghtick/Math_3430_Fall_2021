import LA

def unstable_GramSchmidt(mtx_1: list):
    """
    performs the unstable version of Gram-Schmidt for reduced QR factorization

    first initializes a square matrix or zeros R equal to the columns of the input matrix
    also initializes a zero matrix of equal size to the input matrix
    then for each element in the input matrix( appends the element of the input to V
    for each element in each element(vector) of the matrix (the corrosponding element of R
    is set to the inner product of vector of the Q martix and V matrix
    V at the index is then set to the vector subtraction of itself and the scalar vector multiplication of 
    the scalar element in R matrix and the vector column element of Q)
    the diagonal elements of R are set to equal the p norm of the V index)
    the orthoganal matrix Q is then set to be the matrix V divided by the diagonal scalar elements of R

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
        Q.append([0 for i in range(len(element))])
    
    
    for index in range(len(mtx_1)):
        V.append(mtx_1[index])
        
        for inner_index in range(0,index):
            R[index][inner_index] = LA.innerProd(Q[inner_index], V[index])
            V[index] = LA.add_vectors(V[index], LA.scalar_vector_mult(-R[index][inner_index], Q[inner_index]))
        R[index][index] = LA.pNorm(V[index])
        Q[index] = (LA.scalar_vector_mult(1/R[index][index], V[index]))
    
    return [Q, R]


    

    
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



