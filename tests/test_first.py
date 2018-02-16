import numpy as np
from functions import reduce_dimension, rescale_dimension, hash_data, reshape_data, process
from sklearn.pipeline import Pipeline
import pandas as pd

np.random.seed(124)


def test_reduce_dimension():
    x = np.random.rand(3, 9)
    result = reduce_dimension(x)
    answer = [[0.06025243, 0.65487387], [0.36690512, -0.59016376], [-0.42715755, -0.06471012]]
    np.testing.assert_allclose(result, answer)


def test_rescale_dimension():
    x = np.random.rand(3, 2)
    result = rescale_dimension(x)
    answer = [[0., -0.64130691], [0.87964569, 0.], [-1.12035431,  1.35869309]]
    np.testing.assert_allclose(result, answer)

def test_re():
    # Load the Iris Data Set
    df = pd.read_csv("data/data_vendors.csv")
    print(reshape_data(df))
    assert  1 ==0


def test_hash_data():
    d = [{'dog': 1, 'cat': 2, 'elephant': 4}, {'dog': 2, 'run': 5}]
    result = hash_data(d, n_features=2)
    answer = [[-4.,  1.],[-5., -2.]]
    np.testing.assert_allclose(result, answer)

def test_hash_data2():
    d = [{'dog': 'da1', 'cat': 'da2', 'elephant': 'da3'}, {'dog': 'da1', 'run': 'da4'}]
    result = hash_data(d, n_features=2)
    answer = [[1.,  0.],[-2., -0.]]
    np.testing.assert_allclose(result, answer)



def test_qwe():
    df = pd.read_csv("data/data_vendors.csv")
    print(process(df))
    assert  1 ==0