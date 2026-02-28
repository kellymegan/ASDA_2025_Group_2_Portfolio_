# **Introduction**

# **Authors**

# **Outline**

# 1. Data

# 2. Predicting Train Delay Duration

This section investigates how much of the variance in train delay duration can be explained by observable operational and structural factors, and what the limits of predictability are.

Delay duration is defined as delay=max(delay_in_min,0) to exclude early arrivals from the reliability measure. 

![alt text](../additional_materials/images/delay_distrib.png)

Due to strong right-skewness and a large mass at zero, the dependent variable is transformed as log(1+delay).

![alt text](../additional_materials/images/lTransformedDistr.png)

## Model Specification and Assumption Diagnostics

We first estimate a log-linear regression using operational variables (departure hour, weekday, month, weekend indicator, and line position).

Residual diagnostics indicate:
- The log transformation substantially reduces skewness
- Mild right-skewness remains due to heavy-tailed delay events.
- Some heteroskedasticity persists, though reduced compared to the untransformed model.
- Residual normality is not fully satisfied in the tails, which is expected given the large sample size and extreme delay events.
- Overall, model assumptions are reasonably satisfied for predictive purposes, though extreme delays remain difficult to capture.

Diagnostic plots (residual distribution (Figure 1), residuals vs fitted (Figure 2), Q-Q plot (Figure 3)) are provided in the Appendix.

## Incremental Model Comparison

Three models are estimated:

- Model 1: Operational variables only → R² ≈ 0.04 
    - Variables: Train line station number (train_line_station_num), Departure Hour (dep_hour), Departure Day of Week (dep_dow), Departure Month (dep_month), Departure is on Weekend (is_weekend)
- Model 2: + Train type → R² ≈ 0.16
    - Variables: Train line station number (train_line_station_num), Departure Hour (dep_hour), Departure Day of Week (dep_dow), Departure Month (dep_month), Departure is on Weekend (is_weekend), Train type (train_type)
- Model 3: + Station identity → R² ≈ 0.21
    - Variables: Train line station number (train_line_station_num), Departure Hour (dep_hour), Departure Day of Week (dep_dow), Departure Month (dep_month), Departure is on Weekend (is_weekend), Train type (train_type), Station Name (station_name).

Model 3:

![alt text](../additional_materials/images/ridge_model_fit.png)


This suggests that operational timing alone explains little variation, and structural variables, especially train type and station, increase explanatory power. However, since the explained variance (0.21) is still quite low, we analyzed nonlinear effects using a Random Forest model. Here, the R² is approx. 0.26.

![alt text](../additional_materials/images/modelComparison.png)

 The plot shows that nonlinear modeling improves performance moderately, suggesting interaction effects but no dramatic hidden structure.

## Model Fit and Predictability Limits

Observed vs. predicted plots reveal:
- Good performance for small and moderate delays.
- Systematic underprediction of large delays.
- Compression of predictions toward lower values.

![alt text](../additional_materials/images/rf_fit.png)

Interpretation: 

- The model captures typical delay patterns but fails to predict extreme disruption events. 
- Large delays seem to be driven by factors not contained in schedule-based structural variables.

## Feature Importance

The permutation importance analysis shows three key findings:
- Station identity and train type are the dominant predictors.
- Temporal variables contribute less.
- Line position has moderate importance.

![alt text](../additional_materials/images/rf_feature_importance.png)

This suggests that duration is primarily structured by infrastructural and operational system characteristics rather than simple time-of-day effects.

## Conclusion

Observable operational and structural variables explain roughly 20–26% of the variation in train delay duration. Although delays show clear structural patterns across train types and stations, most of the variation cannot be explained using the available data. In particular, large delay events are difficult to predict, suggesting that additional unobserved factors, such as infrastructure disruptions, weather conditions, or network spillovers, play an important role in train delays.


# 3. RQ2

# 4. RQ3

# 5. RQ4 

# 6. RQ5

# 7. RQ 6

# 8. Appendix

Figure 1: Residual distribution: ![alt text](../additional_materials/images/residualsRR.png).png)

Figure 2: Residuals vs Fitted: ![alt text](../additional_materials/images/resVSfitted.png).png)

Figure 3: Q-Q Plot: ![alt text](../additional_materials/images/qqPlot.png).png)


