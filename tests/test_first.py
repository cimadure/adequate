import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline

from functions import reduce_dimension, rescale_dimension, hash_data, reshape_data, process, stack_scoring, convert_text_to_features, INDEXES
from functions import *

pd.set_option('expand_frame_repr', False)

np.random.seed(124)
DF_EXAMPLE = df = pd.DataFrame([{'Category': 'CA1', 'Criteria': "cr1", 'target': 1},
                      {'Category': 'CA1', 'Criteria': "cr2", 'target': 22},
                      {'Category': 'CA2', 'Criteria': "cr3", 'target': 3},
                      {'Category': 'CA3', 'Criteria': "cr4", 'target': 4},
                      {'Category': 'CA3', 'Criteria': "cr3", 'target': 5}])


def test_reduce_dimension():
    np.random.seed(124)
    x = np.random.rand(3, 9)
    result = reduce_dimension(x)
    answer = [[0.06025243, 0.65487387], [0.36690512, -0.59016376], [-0.42715755, -0.06471012]]
    np.testing.assert_allclose(result, answer)


def test_rescale_dimension():
    np.random.seed(124)
    x = np.random.rand(3, 2)
    result = rescale_dimension(x)
    answer = [[-1.195246,  1.218414], [0.804754,  0.], [0., -0.781586]]
    np.testing.assert_allclose(result, answer, rtol=1e-06)


def test_re():
    df = pd.read_csv("data/data_vendors.csv")
    print(reshape_data(df))
    assert 1 == 1


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


def test_text_features():
    print(DF_EXAMPLE)
    df = convert_text_to_features(DF_EXAMPLE)
    print(df)


def test_process():
    df = pd.read_csv("data/data_vendors.csv")
    df = reshape_data(df).transpose()
    train = df.loc['Target']
    xy = i_dont_know(df, train=train)
    print(xy)
    # df = convert_text_to_features(DF_EXAMPLE)
    # print(df)
    # df = rescale_dimension(df[INDEXES])
    # print(df)
    # df = reduce_dimension(df,)
    # print(df)


def test_simple_quadran():
    df = pd.DataFrame(np.tile(np.array([1, 2, 3, 4, 5]), (5, 1)), columns=list('ABCDE'))
    df = df.transpose()
    print(df)
    train = df.loc['C']
    print(i_dont_know(df, train=train))


def test_simple_quadran():
    df = pd.DataFrame(np.tile(np.array([1, 2, 3, 4, 5]), (3, 1)), columns=list('ABCDE'))
    df = df.transpose()
    df.loc['F'] = [3.5, 3.5, 3.5]
    print(df)
    train = df.loc['C']
    result = i_dont_know(df, train=train)
    print(result)
    df = pd.DataFrame(result)
    print(df)


df = pd.DataFrame([{'Category': 'CA1', 'Criteria': "cr1", 'score': 1},
                      {'Category': 'CA1', 'Criteria': "cr2", 'score': 22},
                      {'Category': 'CA2', 'Criteria': "cr3", 'score': 3},
                      {'Category': 'CA3', 'Criteria': "cr4", 'score': 4},
                      {'Category': 'CA3', 'Criteria': "cr3", 'score': 5}])

df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                   'B': ['A', 'B', 'C'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})


