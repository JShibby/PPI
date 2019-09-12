# Predicting the PPI
Welcome to my repository for *Predicting the Poverty Probability Index.*  In this project, I attempted to predict the PPI from high-level data about individuals provided by the Finanical Inclusion Insights household surveys.  

The project's metric was the R2 score.  The result was disappointing: only a low R2 score of 0.422 was acieved.  I investigate this low performance and point to two issues in the data:
1. The target is a continuous variable, but the data provides almost no numerical basis for regression.
2. The features exhibit a fair amount of information overlap.

This repository holds the data report, scripts, and data files used for review.  All the analysis appears in the data report **["Predicting the PPI."](PPI_data_report.pdf)**

## Scripts
Several Python scripts must be run in succession to respect dependencies: *data*, *encode*, and *model*.  In addition, two other supplemental scripts can be run optionally.  Numbers show necessary scripts; bullets show the optional scripts.  

1. data.py
   * explore.py
2. encode.py
3. model.py
   * present.py
   
The final modeling was done in Azure Machine Learning Studio, so that bit does not appear in these scripts.
