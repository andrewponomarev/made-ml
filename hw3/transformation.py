from sklearn.pipeline import Pipeline

#Transformer without polynomial features
Full_Transformer =\
Pipeline([('Feature_Engineering', FeatureUnionTransformer),
          ('Min_Max_Transformer', MaxAbsScaler())
         ])
