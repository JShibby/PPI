# -*- coding: utf-8 -*-
"""
Models data.
"""

#%%  Packages
import numpy.random as nr
from sklearn import preprocessing, linear_model
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import r2_score

import warnings
#warnings.filterwarnings("ignore", category=FutureWarning)

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

#%%  Tracking
results = pd.Series(name = 'Results')    

#%%  Regression
lin_mod = linear_model.LinearRegression()
lin_mod.fit(X, y)
yp = lin_mod.predict(X2)

yp = pd.Series(yp, index = y2.index)
# Linear regression can give far-off predictions.
yp = yp.map(lambda x: max(x, 0))
yp = yp.map(lambda x: min(x, 1))

scatter(y2, yp, title = "Linear Reg.")

r2 = r2_score(y2, yp).round(3)
results['Linear Reg.'] = r2

#%%  Regression with Ridge
clf = Ridge(alpha=1)
clf.fit(X, y)
yp = clf.predict(X2)

scatter(y2, yp, 'Linear Regression Model with Ridge Regression')

r2 = r2_score(y2, yp).round(3)
results['Lin-Ridge'] = r2

#%%  Decision Tree Regressor
from sklearn.tree import DecisionTreeRegressor
tree = DecisionTreeRegressor(random_state=0, max_depth = 10)
tree.fit(X, ya)
yp = tree.predict(X2)

scatter(y2, yp, title = "DTR")

r2 = r2_score(y2, yp).round(3)
results['DTR'] = r2

#%%  DTR Sweep
depth_list = [5,6,7,8,9,10]
s = pd.Series(name = 'DTR Sweep')

for depth in depth_list:
    tree = DecisionTreeRegressor(random_state=0, max_depth = depth)
    tree.fit(X, y)
    yp = tree.predict(X2)
    r2 = r2_score(y2, yp).round(3)
    s.loc[depth] = r2

s.plot()
sns.barplot()
s.max()

#%%  Janke Tree
'''
This cell uses the decision tree classifier as a janke regressor.
It does not work.
'''

r = .01
ya = y // r * r
ya = ya.astype(str)

from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier(random_state=0, max_depth = 7)
tree.fit(X, ya)
yp = tree.predict(X2).astype(float)
r2_score(y2, yp).round(3)

#%%  AdaBoost
from sklearn.ensemble import AdaBoostRegressor

clf = AdaBoostRegressor(random_state=0)
clf.fit(X, y)  
yp = clf.predict(X2)

yp = pd.Series(yp, index = y2.index)
scatter(y2, yp, title = "Adaboost")

r2 = r2_score(y2, yp).round(3)
results['Adaboost'] = r2

#%%  Export
results['Drop uninformative'] = drop_uninformative
results['Recode ints'] = recode_ints
results

''' 
s['Comment'] = 'No removing uninformative, no reclassifying integers.'
s.to_csv("data/No changes.csv")
'''
