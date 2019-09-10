# PPI
Welcome to my repository for *Predicting the Poverty Probability Index.*  In this project, I attempted to predict the PPI from high-level data about individuals provided by the Finanical Inclusion Insights household surveys.  

The project's metric was the R2 score.  The result was disappointing: only a low R2 score of 0.422 was acieved.  I investigate this low performance and point to the relatively uninformativeness of the features as the primary problem.  The PPI is a continuous variable, so represents a regression problem.  But the dataset effectively offers no numerical basis for regression: after proper coding, it contains almost entirely boolean and categorical information.  

This repository holds the data report, scripts, and data files used for review.  All the analysis appears in the data report *Predicting the PPI.pdf*.

## Scripts
Several scripts must be run in succession to respect dependencies: *data*, *encode*, and *model*.  In addition, two other supplemental scripts can be run optionally.  Numbers show necessary scripts; bullets show the optional scripts.
1. data.py
   * explore.py
2. encode.py
3. model.py
   * present.py
