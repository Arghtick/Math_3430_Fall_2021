
import pytest
import LA

test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]
test_vector_03 = [5, 3, 1]
test_const_01 = 2
test_const_02 = 3
test_identity_mtx = [[1, 0, 0],[0, 1, 0],[0, 0, 1]]
test_matrix_01 = [test_vector_01, test_vector_02, test_vector_03]

def test_add_vectors1():
    
    assert LA.add_vectors(test_vector_01, test_vector_02) == [4,3,6]
  
def test_add_vectors2():
    
    assert LA.add_vectors(test_vector_02,test_vector_03) == [8,4,3]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      
def test_scalar_vector_mult1():
    
    assert LA.scalar_vector_mult(test_const_01, test_vector_01) == [2,4,8]
    
def test_scalar_vector_mult2():
    
    assert LA.scalar_vector_mult(test_const_02, test_vector_02) == [9,3,6]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_scalar_matrix_mult1():
    
    assert LA.scalar_matrix_mult(test_const_01, test_matrix_01) == [[2,4,8],[6,2,4],[10,6,2]]
  
def test_scalar_matrix_mult2():
    
    assert LA.scalar_matrix_mult(test_const_01,test_identity_mtx) == [[2,0,0],[0,2,0],[0,0,2]]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_add_matrix1():
    assert LA.add_matrix(test_matrix_01,test_matrix_01) == [[2,4,8],[6,2,4],[10,6,2]]

def test_add_matrix2():
    assert LA.add_matrix(test_matrix_01,test_identity_mtx) == [[2,2,4],[3,2,2],[5,3,2]]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
def test_matrix_vector_mult1():
    assert LA.matrix_vector_mult(test_matrix_01,test_vector_01) == [27, 16, 12]

def test_matrix_vector_mult2():
    assert LA.matrix_vector_mult(test_matrix_01,test_vector_02) == [16,13,16]
   
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
   
def test_matrix_matrix_mult1():
    assert LA.matrix_matrix_mult(test_matrix_01, test_matrix_01) == [[27,16,12],[16,13,16],[19,16,27]]
    
def test_matrix_matrix_mult2():
    assert LA.matrix_matrix_mult(test_matrix_01, test_identity_mtx) == [[1,2,4],[3,1,2],[5,3,1]]
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    