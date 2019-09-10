#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Explores model predictions.  Prepares plots for data reports.

Run cells individually.
"""
#%%  Integer Presentation
# =============================================================================
# col = 'num_times_borrowed_last_year'
# fig, axarr = plt.subplots(1,2, figsize = (12,5))
# plt.subplots_adjust(hspace=0.5)
# 
# data = df.groupby('num_times_borrowed_last_year')['poverty_probability'].mean()
# data.plot.bar(ax = axarr[0])
# 
# data = df.groupby('num_formal_institutions_last_year')['poverty_probability'].mean()
# data.plot.bar(ax = axarr[1])
# =============================================================================

#%%  Float Present
fig, axarr = plt.subplots(1,2, figsize = (12,5))
plt.subplots_adjust(hspace=0.5)

ax = axarr[0]
col = 'avg_shock_strength_last_year'
df.plot.scatter(x = col, y='poverty_probability', 
                alpha = 0.2, ax = ax)
corr = df[col].corr(df.poverty_probability).round(3)
title = 'Correlation: '+str(corr)
ax.set_title(title)

ax = axarr[1]
col = 'age'
df.plot.scatter(x = col, y='poverty_probability', 
                alpha = 0.2, ax = ax)
corr = df[col].corr(df.poverty_probability).round(3)
title = 'Correlation: '+str(corr)
ax.set_title(title)
 
#%%  Misconstrued floats
('education_level', 'share_hh_income_provided')
df.plot.scatter(x = 'education_level', y = 'poverty_probability')
