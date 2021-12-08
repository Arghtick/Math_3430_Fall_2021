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




