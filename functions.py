from sklearn import manifold


def reduce_dimension(x):
    mds = manifold.MDS(n_components=2, max_iter=100, n_init=1)
    return mds.fit_transform(x)

