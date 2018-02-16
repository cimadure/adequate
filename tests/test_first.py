import numpy as np
from functions import reduce_dimension, rescale_dimension, pipeline_data
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

    print(df)

    assert  1 ==0