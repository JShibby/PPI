# -*- coding: utf-8 -*-
"""
Models data.
"""

#%%  Packages
from sklearn import preprocessing, linear_model
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import r2_score

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#%%  Plotting
def scatter(y, yp,title = ''):
    '''Justin's scatter for presenting model performance.''' 
    plt.figure()
    plt.scatter(y, yp, alpha = .2)
    r2 = r2_score(y, yp).round(3)
    plt.xlabel('poverty_probability')
    plt.ylabel('prediction')
    t = title + '\nR2: '+str(r2)
    plt.title(t)  

#%%  Regression
lin_mod = linear_model.LinearRegression()
lin_mod.fit(X, y)
yp = lin_mod.predict(X2)

yp = pd.Series(yp, index = y2.index)
yp = yp.map(lambda x: max(x, 0))

scatter(y2, yp, title = "Linear Reg.")


#%%  Regression with Ridge
clf = Ridge(alpha=1.0)
clf.fit(X, y)
yp = clf.predict(X2)
scatter(y2, yp, 'Linear Regression Model with Ridge Regression')
