# -*- coding: utf-8 -*-
"""
Preps data for sklearn modeling.  Encoding, scaling as necessary.

Created on Mon Jul 22 17:38:31 2019
@author: justi
"""
#%%  Packages
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

#%%  Encode
def encode_string(cat_features):
    ## First encode the strings to numeric categories
    enc = preprocessing.LabelEncoder()
    enc.fit(cat_features)
    enc_cat_features = enc.transform(cat_features)
    ## Now, apply one hot encoding
    try:
        ohe = preprocessing.OneHotEncoder(categories = 'auto')
    except TypeError:
        ohe = preprocessing.OneHotEncoder()
    encoded = ohe.fit(enc_cat_features.reshape(-1,1))
    return encoded.transform(enc_cat_features.reshape(-1,1)).toarray()


#%%  Categoricals
print('Encode  ...')    
Features = np.empty((df.shape[0],0))

categorical_columns = df.columns[(df.dtypes == 'bool') | (df.dtypes == 'object')]

for column in categorical_columns:
    x = encode_string(df[column])
    Features = np.concatenate([Features, x], axis = 1)


#%%  Add numerics, Scale data
print('Numerics ...')
numeric_columns = df.columns[(df.dtypes == 'float64') | (df.dtypes == 'int64')]
numeric_columns = list(numeric_columns)
numeric_columns.remove('poverty_probability')
numeric_columns

for column in numeric_columns:
    x = df[column]
    x = np.array(x).reshape(-1,1)
    scaler = preprocessing.StandardScaler().fit(x)
    x = scaler.transform(x)
    Features = np.concatenate([Features, x], axis = 1)
            
#%%  Split
print('Split ...')
label = df.poverty_probability
X, X2, y, y2 = train_test_split(Features, label)
y.shape
