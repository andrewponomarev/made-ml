from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import MaxAbsScaler, FunctionTransformer
from sklearn.impute import SimpleImputer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.neighbors import KNeighborsRegressor as KNNR

import numpy as np
import pandas as pd

from data_preparation.columns import *


#functions to get columns for featrue tranformers
def get_col_to_fillna_most_frequent(df):
    return df[col_to_fillna_most_frequent]

def get_col_long_text_cols(df):
    return df['description']

def get_sum_long_text_cols(s):
    return pd.DataFrame(s.apply(lambda s: len(s.split(' '))))

def get_col_to_fillna_bool(df):
    return df[long_text_cols]

def get_col_to_fillna_mean(df):
    return df[col_to_fillna_mean]

def get_col_to_get_dummies(df):
    return df[col_to_getdummies]


def get_lat_long(df):
    return df[['latitude','longitude']]

# def get_amenities(df):
#     return df['amenities']
#
# def get_amenities2(df):
#     return df[['amenities']]

def get_col_no_change(df):
    return df[col_no_change]

# def get_sum_amenities(s):
#     return pd.DataFrame(s.apply(lambda s: len(s.split(' '))))


class MyTransformer(TransformerMixin, BaseEstimator):
    '''A template for a custom transformer.'''

    def __init__(self, model):
        self.model=model
        pass

    def fit(self, X, y=None):
        self.model.fit(X, y)
        return self

    def transform(self, X):
        # transform X via code or additional methods
        return pd.DataFrame(self.model.predict(X))

TSVD_n_components=10
KNN_neighbors=200

TruncatedSVD_features=TruncatedSVD(n_components=TSVD_n_components)
KNN_Reg = KNNR(n_neighbors=KNN_neighbors)

Transformer_fillna_most_frequent =\
Pipeline([('Select_col_to_fillna_most_frequent',
           FunctionTransformer(func=get_col_to_fillna_most_frequent,
                               validate=False)),
          ('Fill_Null',
           SimpleImputer(missing_values=np.nan,
                         strategy='most_frequent')),
          ('To_float_transformer',FunctionTransformer(
              func=lambda x: x.astype(float) ,validate=False))
         ])

Transformer_fillna_mean =\
Pipeline([('Select_col_to_fillna_mean',
           FunctionTransformer(func=get_col_to_fillna_mean,
                               validate=False)),
          ('Fill_Null',
           SimpleImputer(missing_values=np.nan, strategy='mean'))
         ])

Transformer_OneHotEncoder =\
Pipeline([('Select_col_to_get_dummies',
           FunctionTransformer(func=get_col_to_get_dummies, validate=False)),
          ('OneHotEncoder_transform',
           OneHotEncoder(handle_unknown='ignore'))
         ])

# Transformer_amenities =\
# Pipeline([('Select_col_to_get_amenities',
#            FunctionTransformer(func=get_amenities, validate=False)),
#           ('CountVectorizer_transform', CountVectorizer(min_df=0.02)),
#           ('Feature_extractor_TSVD', TruncatedSVD_features)
#          ])


# Transformer_sum_amenities=\
# Pipeline([('Select_col_to_get_amenities',FunctionTransformer(
#     func=get_amenities, validate=False)),
#           ('Get_sum_amenities', FunctionTransformer(
#               func=get_sum_amenities, validate=False)),
#          ])

Transformer_sum_text=\
Pipeline([('Select_col_to_get_long_text_cols',FunctionTransformer(
    func=get_col_long_text_cols, validate=False)),
          ('Get_sum_long_text_cols', FunctionTransformer(
              func=get_sum_long_text_cols, validate=False)),
         ])


Transformer_get_columns =\
Pipeline ([('Select_col_no_change',
            FunctionTransformer(func=get_col_no_change, validate=False))
          ])

Transformer_lat_long =\
Pipeline ([('Select_col_lat_long_price',
            FunctionTransformer(func=get_lat_long, validate=False)),
           ('MyTransformer', MyTransformer(KNN_Reg))
          ])

FeatureUnionTransformer =\
FeatureUnion([('FTfillna_frequent',   Transformer_fillna_most_frequent),
              ('FTfillna_mean',       Transformer_fillna_mean),
              ('FTget_OneHotEncoder', Transformer_OneHotEncoder),
              # ('FTamenities',         Transformer_amenities),
              # ('FT_sum_amenities',    Transformer_sum_amenities),
#               ('FTtext',              Transformer_text),
#               ('FT_sum_text',         Transformer_sum_text),
              ('FT_lat_long',         Transformer_lat_long),
              ('FT_get_columns',      Transformer_get_columns)
             ], n_jobs = -1)

#Transformer without polynomial features
Full_Transformer =\
Pipeline([('Feature_Engineering', FeatureUnionTransformer),
          ('Min_Max_Transformer', MaxAbsScaler())
         ])
