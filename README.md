# Forest Fires Temperature & Wind Linear Regression Analysis

This repository contains an end-to-end data analytics and statistical modeling project. It explores the relationship between wind speed and ambient temperature using the open-source **Forest Fires** dataset.

## Project Overview
- **Objective:** To statistically model the linear relationship between wind speed (`wind`) and temperature (`temp`) using Ordinary Least Squares (OLS) regression.
- **Dataset:** 517 complete observations from the Forest Fires dataset.
- **Methodology:** Descriptive and inferential statistical analysis implemented in Python.

## Technologies & Libraries Used
- **Python**
- **Pandas** (Data loading and preprocessing)
- **Statsmodels** (OLS Linear Regression modeling and statistical summaries)
- **Matplotlib** (Data visualization)

## Statistical Results & Insights
The theoretical model established is:
Y = -0.2045 * X + 19.3900
*(where Y is expected Temperature in °C, and X is Wind Speed in km/h)*

- **Intercept (b = 19.3900):** Under theoretical conditions with zero wind speed, the baseline expected average temperature is 19.39 °C.
- **Slope (a = -0.2045):** Indicates a slight inverse relationship. Each 1 km/h increase in wind speed is associated with an average decrease of 0.2045 °C in temperature.
- **Statistical Significance (p-value = 0.1017):** Since the p-value is greater than the standard 0.05 alpha level, the effect of wind speed on temperature is **not statistically significant** at the 95% confidence level for this specific dataset.
- **Goodness of Fit (R² = 0.0052):** Only 0.52% of the variance in temperature is explained by wind speed. This low value highlights the existence of critical **omitted variables** (e.g., season, month, relative humidity, and solar radiation) that primarily drive temperature fluctuations.

## Model Visualization
Below is the scatter plot of the 517 observation points along with the fitted OLS regression line:

![Regression Line](regresyon_grafigi.png)

## Full Academic Report
For comprehensive interpretations, hypothesis testing details, and a critical evaluation of model limitations, please review the complete final document: **[Report.pdf](Report.pdf)**.
