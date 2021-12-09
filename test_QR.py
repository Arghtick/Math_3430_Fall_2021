import pytest
import LA
import QR

test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]
test_vector_03 = [5, 3, 1]
test_const_01 = 2
test_const_02 = 3
test_identity_mtx = [[1, 0, 0],[0, 1, 0],[0, 0, 1]]
test_matrix_01 = [test_vector_01, test_vector_02, test_vector_03]
test_comp_const_01 = 3 + 4j
test_comp_const_02 = -3
test_comp_vec_01 = [3 + 4j, 1, 4-3j]
test_GS_mtx1 = [[2,2,1],[-2,1,2],[18,0,0]]
test_GS_mtx2 = [[12,6,-4],[-51,167,24],[4,-68,-41]]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_orthonormal_vectorset1():
    expected: list = [[2/3,2/3,1/3],[-2/3,1/3,2/3],[1/3,-2/3,2/3]]
    for column in range(len( QR.orthonormal_vectorset(test_GS_mtx1))):
        for element in range(len(QR.orthonormal_vectorset(test_GS_mtx1)[column])):
            x= QR.orthonormal_vectorset(test_GS_mtx1)[column][element]
            y=expected[column][element]
            assert abs(x-y) <= 0.00001

def test_orthonormal_vectorset2():
    expected: list = [[6/7,3/7,-2/7],[-69/175,158/175,6/35],[-58/175,6/175,-33/35]]
    for column in range(len( QR.orthonormal_vectorset(test_GS_mtx2))):
        for element in range(len(QR.orthonormal_vectorset(test_GS_mtx2)[column])):
            x= QR.orthonormal_vectorset(test_GS_mtx2)[column][element]
            y=expected[column][element]
            assert abs(x-y) <= 0.00001


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_stable_GramSchmidt1():
    expected: list = [[3,0,0],[0,3,0],[12,-12,6]]
    for index in range(0,2):
        for column in range(len( QR.stable_GramSchmidt(test_GS_mtx1)[1])):
            for element in range(len(QR.stable_GramSchmidt(test_GS_mtx1)[1][column])):
                assert LA.absolute_value(QR.stable_GramSchmidt(test_GS_mtx1)[1][column][element] - expected[column][element]) <= 0.001

def test_stable_GramSchmidt2():
    expected: list =  [[14,0,0],[21,175,0],[-14,-70,35]]
    for index in range(0,2):
        for column in range(len( QR.stable_GramSchmidt(test_GS_mtx2)[1])):
            for element in range(len(QR.stable_GramSchmidt(test_GS_mtx2)[1][column])):
                assert LA.absolute_value(QR.stable_GramSchmidt(test_GS_mtx2)[1][column][element] - expected[column][element]) <= 0.001

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_Householder1():
    #i think this is the matrix you said we shouldnt use but it is the same 
    #matrix i used for the last homework too i didnt know if that meant it was
    #fine for me to still use in that case or if i need to come up with a whole
    #new test
    expected: list = [[-3,0,0],[0,-3,0],[-12,12,-6]]
    for index in range(0,2):
        for column in range(len( QR.householder(test_GS_mtx1)[1])):
            for element in range(len(QR.householder(test_GS_mtx1)[1][column])):
                assert LA.absolute_value(QR.householder(test_GS_mtx1)[1][column][element] - expected[column][element]) <= 0.00001

def test_Householder2():
    expected: list =  [[-14,0,0],[-21,-175,0],[14,70,35]]
    for index in range(0,2):
        for column in range(len( QR.householder(test_GS_mtx2)[1])):
            for element in range(len(QR.householder(test_GS_mtx2)[1][column])):
                assert LA.absolute_value(QR.householder(test_GS_mtx2)[1][column][element] - expected[column][element]) <= 0.000001

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_i_mtx1():
    assert QR.i_mtx(3) == [[1,0,0],[0,1,0],[0,0,1]]
    
def test_i_mtx2():
    assert QR.i_mtx(5) == [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]  

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_sign1():
    assert QR.sign(1.23) == 1
    
def test_sign2():
    assert QR.sign(-3.21) == -1
   
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_vec_vec_mult1():
    assert QR.vec_vec_mult([1,2,3], [2,4,3]) == [[2,4,3],[4,8,6],[6,12,9]]
    
def test_vec_vec_mult2():
    assert QR.vec_vec_mult([3,-1,5], [2,4,-3]) == [[6,12,-9],[-2,-4,3],[10,20,-15]]
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_F_builder1():
    expected: list = [[-2/3,-2/3,-1/3],[-2/3,11/15,-2/15], [-1/3,-2/15,14/15]]
    F: list = QR.F_builder([5,2,1])
    for element in range(len(F)):
        for index in range(len(F[0])):
            assert LA.absolute_value(F[element][index] - expected[element][index]) <= 0.001

def test_F_builder2():
    expected: list = [[-3/5,-4/5],[-4/5,3/5]]
    F: list = QR.F_builder([4.8,2.4])
    for element in range(len(F)):
        for index in range(len(F[0])):
            assert LA.absolute_value(F[element][index] - expected[element][index]) <= 0.001

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_Q_builder1():
    expected: list = [[-2/3,-2/3,-1/3],[-2/3,11/15,-2/15], [-1/3,-2/15,14/15]]
    Q: list = QR.Q_builder([[2, 2, 1], [-2, 1, 2], [18, 0, 0]],0)
    for element in range(len(Q)):
        for index in range(len(Q[0])):
            assert LA.absolute_value(Q[element][index] - expected[element][index]) <= 0.001

def test_Q_builder2():
    expected: list = [[1, 0, 0], [0, -3/5, -4/5], [0, -4/5, 3/5]]
    Q: list = QR.Q_builder([[-3,0,0], [0, 1.8, 2.4], [-12,-12,-6]],1)
    for element in range(len(Q)):
        for index in range(len(Q[0])):
            assert LA.absolute_value(Q[element][index] - expected[element][index]) <= 0.001

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_deep_copy1():
    assert QR.deep_copy([[1,2,3],[4,5,6],[7,8,9]]) == [[1,2,3],[4,5,6],[7,8,9]]

def test_deep_copy2():
    assert QR.deep_copy([[3 + 4j ,5.4,12],[-4,5-3j, 0.7]]) == [[3 + 4j ,5.4,12],[-4,5-3j, 0.7]]
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_conjugate_transpose1():
    assert QR.conjugate_transpose([[1,2,3],[4,5,6]]) == [[1,4],[2,5],[3,6]]

def test_conjugate_transpose2():
    assert QR.conjugate_transpose([[1-2j,2,3+ 4j],[4,5-2j,6]]) == [[1+2j,4],[2,5+2j],[3-4j,6]]


