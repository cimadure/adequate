from sklearn import manifold
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction import FeatureHasher
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import Imputer

INDEXES = ['Category', 'Criteria']


def reduce_dimension(x):
    mds = manifold.MDS(n_components=2, max_iter=100, n_init=1)
    return mds.fit_transform(x)


def rescale_dimension(x):
    return RobustScaler(quantile_range=(25, 75)).fit_transform(x)


def hash_data(x, n_features=10):
    h = FeatureHasher(n_features=n_features)
    f = h.transform(x)
    return f.toarray()


def reshape_data(df):
    df = df.set_index(INDEXES)
    return df
    #return df.stack()


def process(df):
    dfs = np.split(reshape_data(df), [1], axis=1)

    print(dfs[0].head(4))
    print(dfs[1].head(4))
    #print(dfs[0].index)

    #m = df.as_matrix(INDEXES)
    #print(m)
    h = FeatureHasher(n_features=2)
    f = h.transform(df.to_dict())
    print(f)
    #cols  = hash_data(df.as_matrix(INDEXES), n_features=2)
    #print(cols)

    # from sklearn.preprocessing import LabelEncoder
    #
    # lb_make = LabelEncoder()
    # obj_df["make_code"] = lb_make.fit_transform(obj_df["make"])
    # obj_df[["make", "make_code"]].head(11)


def stack_scoring(df):
    return reshape_data(df).stack()
    # return df.stack()


def convert_text_to_features(df):
    label_category = preprocessing.LabelEncoder()
    label_category.fit(df['Category'])
    df['Category'] = label_category.transform(df['Category'])

    label_criteria = preprocessing.LabelEncoder()
    label_criteria.fit(df['Criteria'])
    df['Criteria'] = label_criteria.transform(df['Criteria'])
    return df
    #yield label_category
    #yield label_criteria


def i_dont_know(df, train):

    #df = reduce_dimension(df)
    print(df)

    # example fill with 5 in train section
    imp = Imputer(missing_values='NaN', strategy='mean', axis=1) # axis 0 in examples
    imp.fit(train)
    X = imp.transform(df)
    print(X)
    xy = reduce_dimension(X)
    return xy