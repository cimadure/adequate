import numpy as np
from functions import reduce_dimension

np.random.seed(124)

def test_other():
    x = np.random.rand(3, 9)
    print(x)
    print(' --- --- ---')
    result = reduce_dimension(x)
    answer = [[0.06025243, 0.65487387], [0.36690512, -0.59016376], [-0.42715755, -0.06471012]]
    print(result)

    np.testing.assert_allclose(result, answer)

