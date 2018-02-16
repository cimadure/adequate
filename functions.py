from sklearn import manifold
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline

def reduce_dimension(x):
    mds = manifold.MDS(n_components=2, max_iter=100, n_init=1)
    return mds.fit_transform(x)


def rescale_dimension(x):
    return RobustScaler(quantile_range=(25, 75)).fit_transform(x)


def pipeline_data():
    pass

