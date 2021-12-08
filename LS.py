#LS.py
import LA
import QR



def leastSquare(mtx: list, vec: list):
    """
    calculates least squares solution using QR factorization method
    
    

    """
    temp = QR.stable_GramSchmidt(mtx)
    Q = temp[0]
    R = temp[1]
    
    Q_tran = QR.conjugate_transpose(Q)
    Q_temp = LA.matrix_vector_mult(Q_tran, vec)
    
    x = backsub(R, Q_temp)
    return x
    


def backsub(mtx: list, vec: list):
    result: list = []
    a = 1/(mtx[len(mtx)-1][len(mtx[0])-1])
    temp = a * vec[len(vec)-1]
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

print(leastSquare([[1,1,1],[1,2,3],[2,3,4]], [0,1,3]))