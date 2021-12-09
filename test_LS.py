#test_LS
import pytest
import LA
import LS

test_vec1: list = [4,1,2]
test_mtx1: list= [[-1,2,-1],[2,-3,3]]

def test_leastSquare1():
    expected: list = [3,2]
    LS_result: list = LS.leastSquare(test_mtx1, test_vec1)
    for index in range(len(LS_result)):
        assert LA.absolute_value(LS_result[index] - expected[index]) <=0.001

def test_leastSquare2():
    expected: list = [3,2]
    LS_result: list = LS.leastSquare(test_mtx1, test_vec1)
    for index in range(len(LS_result)):
        assert LA.absolute_value(LS_result[index] - expected[index]) <=0.001

def test_backsub1():
    assert LS.backsub([[2,0,0],[4,4,0],[3,1,6]], [9,5,6]) == [1,1,1]

def test_backsub2():
    expected: list = [2/3, 1/6,3/2]
    x: list = LS.backsub([[1,0,0],[2,3,0],[4,5,6]], [7,8,9])
    for i in range(len(x)):
        assert LA.absolute_value(x[i] -expected[i]) <= 0.001 