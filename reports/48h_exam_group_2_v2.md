# Introduction

Railway reliability indicates how well a transport system works in practice. When trains are delayed or cancelled, it affects passengers directly, and it can also point to deeper issues in how the network is managed, how capacity is allocated, and how daily operations are coordinated.

Using a dataset of over 1.9 million Deutsche Bahn observations from October 2025, this report investigates reliability from multiple analytical perspectives. Specifically, we examine:
- How much of delay duration can be predicted using observable operational variables.
- Whether delay behavior differs structurally across train types.
- Whether delay severity escalates into cancellation risk.
- Which systemic factors drive cancellations across time and geography.
- How stations cluster based on performance profiles.

By combining regression modeling, distributional analysis, hypothesis testing, and clustering techniques, this report provides an assessment of operational instability in the German rail network. Reliability is mainly analyzed through delay duration and cancellation incidence.

# Authors
Megan Kelly-Ortiz, Anna Perkova, Ayush Singh, Tusar , Kush Shah, Onkar Mane

# 1. Data
| Item | Description |
|------|--------------|
| **Dataset name** | Deutsche Bahn Data |
| **Number of rows** | 1989180 |
| **Number of columns** | 16 |
| **File format** | CSV |
| **Authors of the dataset** | Piet Brömmel |
| **Source name** | Huggingface |
| **Source link** | [Deutsche Bahn Data - Huggingface](https://huggingface.co/datasets/piebro/deutsche-bahn-data) |
| **Date of download/analysis** | 27.02.2026 |

A detailed overview of the raw data can be found in the Appendix (Appendix: Table 1.1 & Appendix:Table 1.2).


# 2. Predicting Train Delay Duration

This section investigates how much of the variance in train delay duration can be explained by observable operational and structural factors, and what the limits of predictability are.

Delay duration is defined as delay=max(delay_in_min,0) to exclude early arrivals from the reliability measure. (Appendix: Figure 2.1 - Delay Distribution)

Due to strong right-skewness and a large mass at zero, the dependent variable is finally transformed as log(1+delay).

![alt text](../additional_materials/images/lTransformedDistr.png)

## 2.1 Model Specification and Assumption Diagnostics

We estimate a log-linear regression and assess residual diagnostics on the transformed outcome.

Residual diagnostics indicate:
- The log transformation substantially reduces skewness (Appendix: Figure 2.2 – Residual Distribution).
- Mild right-skewness remains due to heavy-tailed delay events (Appendix: Figure 2.2).
- Some heteroskedasticity persists, as indicated by a slight funnel shape in the residuals vs. fitted plot (Appendix: Figure 2.3 – Residuals vs Fitted).
- Residual normality is not fully satisfied in the tails, as visible from deviations in the upper quantiles of the Q–Q plot (Appendix: Figure 2.4 – Q–Q Plot).
- Overall, model assumptions are reasonably satisfied for predictive purposes, though extreme delays remain difficult to capture (Figures 2.2–2.4).


## 2.2 Incremental Model Comparison


Three models are estimated, where the variables dep_hour, dep_dow, dep_month, and is_weekend where created from departure_planned_time.

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

## 2.3 Model Fit and Predictability Limits

Observed vs. predicted plots reveal:
- Good performance for small and moderate delays.
- Underprediction of large delays.
- Compression of predictions toward lower values.

![alt text](../additional_materials/images/rf_fit.png)

Interpretation: 

- The model captures typical delay patterns but fails to predict extreme events. 
- Large delays seem to be driven by factors not contained in schedule-based structural variables.

## 2.4 Feature Importance

The permutation importance analysis shows three key findings:
- Station identity and train type are the dominant predictors.
- Temporal variables contribute less.
- Line position has moderate importance.

![alt text](../additional_materials/images/rf_feature_importance.png)

This suggests that duration is primarily structured by infrastructural and operational system characteristics rather than simple time-of-day effects.

## 2.5 Conclusion

Although structural variables such as train type and station identity improve explanatory power, the models explain only around 20–26% of delay variation. We therefore next examine whether delay behavior differs systematically across train types.

# 3. Do Train Types Differ in Delay Structure?

To evaluate whether delay duration differs across train types, both descriptive and inferential methods were applied.

## 3.1 Descriptive Evidence

Average delay was calculated across train categories to assess performance differences. The analysis reveals substantial variation between train types, with NJ (23.1 minutes) and NEX (21.8 minutes) recording the highest average delays in the network.

[![Top_10_Train_Types_with_Highest_Average_Delay.png](https://i.postimg.cc/rmVj7wZv/Top_10_Train_Types_with_Highest_Average_Delay.png)](https://postimg.cc/cKzfn0Sm)


## 3.2 Distribution Analysis

To examine variability, a boxplot comparison was conducted for the top 10 most frequent train types.

[![Delay_Distribution.png](https://i.postimg.cc/9MmbsQgK/Delay_Distribution.png)](https://postimg.cc/QBzcTh3J)

**The distribution analysis reveals:**

• ICE and IC trains exhibit greater variability in delay duration.

• Regional services show comparatively tighter distributions.

• Some train types demonstrate extreme values, indicating unstable punctuality performance

## 3.3 ANOVA Test

A one-way ANOVA was conducted to test whether mean delay differs significantly across train types.

F(54, 1,989,070) \= 4638.44

p \< 0.001

The results indicate a statistically significant difference in mean delay between train types.

## 3.4 Effect Size (Eta Squared)

Eta² \= 0.1118

Approximately 11.18% of the total variance in delay duration is explained by train type.

This represents a moderate practical effect, suggesting that the train category plays a meaningful role in punctuality outcomes.

These differences suggest that train types vary in both typical delay levels and in extreme delay events. We next examine tail risk and full distributional differences across train types before testing whether delays escalate into cancellations.

# 4. Structural Differences in Delay Distributions and Tail Risk

While Section 3 focused on mean differences, this section examines the full distributional structure of delays, including variability and tail behavior.

## 4.1 Distribution Structure Across Train Types
Delay distributions vary across train types. Long-distance services (e.g., ICE, IC) show larger median delay and IQR values, indicating higher variability.

The 90th percentile (p90) indicates significant tail behavior for certain train types. A large gap between median and p90 suggests strong right-skewness and frequent extreme delays in long-distance services.

**Figure 1:** Train-type delay structure (Median + IQR + p90 tail)  
![Figure 1: Train-type delay structure](../additional_materials/images/1.png)

## 4.2 Tail Behavior (ECDF)
ECDF curves highlight differences in distributional form. Train types with flatter curves indicate heavier tails and more extreme delays, exceeding the global p90 threshold. These findings show that differences are not limited to central tendency but also reflect changes in tail behavior.

**Figure 3:** Delay tail behavior by train type (ECDF) + global p90  
![Figure 3: ECDF tail behavior](../additional_materials/images/3.png)

## 4.3 Tail Risk and Cancellation Relationship
There is a weak positive relationship between tail delays (p90) and cancellation rate. Although train types with heavier tail risk tend to show higher cancellation probability, the overall association is moderate (Spearman’s ρ ≈ 0.18). This suggests extreme delays contribute to cancellations but are not the only factor.

**Figure 4:** Tail risk (p90) vs cancellation rate (train types)  
![Figure 4: Tail vs cancellation](../additional_materials/images/4.png)

## 4.4 Statistical Evidence
- **Kruskal–Wallis Test:** Significant differences exist in delay distributions between train types (p < 0.05).
- **Distributional Metrics:** Clear differences in median, IQR, and p90 values.
- **Correlation Analysis:** Moderate positive correlation between tail delay and cancellation rate.

## 4.5 Key Findings

| Dimension | Result |
|---|---|
| Central Tendency | Median delay differs across train types |
| Variability | IQR shows strong dispersion differences |
| Tail Behavior | ICE and major hubs exhibit heavier tails |
| Cancellation Link | Tail delay positively but moderately associated with cancellations |

These findings suggest that delay variability and tail risk differ substantially across train types. The next step is to assess whether increasing delay severity translates into higher cancellation probability.

# 5. Does Delay Escalate Into Cancellation?

## 5.1 Statistical Tests

To examine whether increased delay leads to higher cancellation risk, delay duration was categorized into three levels:

• On-time/Early (≤5 minutes)

• Minor Delay (6–15 minutes)

• Severe Delay (\>15 minutes)

### 5.1.1 Crosstab Results

| Delay Category | Not Canceled (%) | Canceled (%) |
| ----- | ----- | ----- |
| On-time/Early | 95.1% | 4.9% |
| Minor Delay | 97.6% | 2.4% |
| Severe Delay | 90.8% | 9.2% |

The heatmap clearly shows that trains with severe delays (\>15 minutes) experience the highest cancellation rate (9.2%).

### 5.1.2 Chi-Square Test

χ² \= 10152.4

df \= 2

p \< 0.001

The Chi-square test confirms a statistically significant association between delay severity and cancellation.

### 5.1.3 Effect Size (Cramér’s V)

Cramér’s V \= 0.0714

This indicates a small but statistically reliable association. While the effect size is modest, the relationship is meaningful given the large sample size.


## 5.2 How does operational stress escalate across delay levels, time-of-day, and station-level congestion?

This section investigates whether operational instability in the German rail network follows an escalation pattern across delay magnitude, time-of-day, and station-level congestion. Specifically, we examine whether increasing delays systematically raise cancellation probability and whether peak-hour stress amplifies both delay volatility and spatial concentration of failures.

![alt text](../additional_materials/images/heatmap_station.png)

**Key Observations:**

- Clear peak cancellation zones during late afternoon and early evening (15:00–19:00).

- Some stations consistently show higher cancellation intensity across most hours.

- Major hubs (e.g., Berlin Südkreuz, Hamburg Hbf) display pronounced evening spikes.

- Early morning hours generally show lower cancellation intensity.

**Interpretation:**

- Cancellations are not evenly distributed.

- Instability concentrates in peak commuter periods.

- Certain stations act as persistent high-risk nodes, independent of hour.

- Suggests infrastructure saturation and network strain during high-demand windows.

---
![alt text](../additional_materials/images/median.png)

**Key Observations:**

- Median delay remains relatively stable (around 0–2 minutes).

- However, delay dispersion widens significantly during daytime and evening.

- Early morning shows high variance, likely due to sparse traffic and occasional extreme events.

- Evening volatility expands again, indicating peak-hour instability.

**Interpretation:**

- Reliability deterioration manifests more in variance expansion than median increase.

- Even if central delay stays moderate, unpredictability grows during peak periods.

- Increased volatility suggests a system operating near capacity limits.

---
![alt text](../additional_materials/images/bands.png)

**Key Observations:**

- Cancellation probability rises steadily as delay magnitude increases.

- Beyond moderate delay thresholds (~60–90 minutes), cancellation risk increases sharply.

- Extremely high delays (>120 min) show volatile but elevated cancellation probabilities.

- Non-zero cancellation probability even at small delays suggests preemptive cancellations.

**Interpretation:**

- There appears to be a non-linear escalation pattern.

- The system likely operates with implicit operational thresholds beyond which cancellation becomes more efficient than recovery.

- Cancellation is not merely random but linked to accumulated operational stress.

While delay severity clearly increases cancellation probability, cancellations may also reflect broader systemic stress patterns beyond immediate delay accumulation. We therefore analyze which structural and operational factors independently drive cancellation risk.

## 5.3 Statistical Summary of Core Findings

| Relationship | Result | Statistical Evidence |
|--------------|--------|----------------------|
| Train Type → Delay | Significant mean differences | ANOVA p < 0.001 (Eta² = 0.11) |
| Delay → Cancellation | Severe delays increase cancellation risk | Chi-square p < 0.001 (Cramér’s V = 0.07) |

Overall, the results indicate that train type explains a meaningful share of delay variation, and that delay severity increases cancellation risk. However, effect sizes suggest that delay alone cannot account for cancellation behavior, so a deeper analysis of systemic operational drivers will follow.

# 6.What Drives Train Cancellations Systemically?

After showing that cancellations concentrate in peak hours and specific stations, we now examine which operational factors are most strongly associated with cancellation risk.

## 6.1 Influence of Train Category

Analysis shows that **Metronom (ME)** and **Intercity (IC)** services face the highest cancellation risks, peaking at **7.36%** and **6.75%** respectively.  
Conversely, **Bus services** are the most reliable mode with a near-zero failure rate.

[![Train-category.png](https://i.postimg.cc/65sj5YFk/Train-category.png)](https://postimg.cc/CdNHcHh7)

*Figure 3.1: Comparison of cancellation rates across major train categories.*

To complement the category-level comparison, we also examine cancellation probability at the more granular train-type level.

[![Cancellation_Rate.png](https://i.postimg.cc/0QknhyXh/Cancellation_Rate.png)](https://postimg.cc/5Hr8CbVm)

Certain train types demonstrate higher cancellation risk, aligning partially with delay rankings. This suggests that operational complexity linked to specific train categories contributes to reliability challenges.

## 6.2 Temporal & Geographical "Blackspots"

#### Geographical Hubs
- **Hamburg Dammtor** is a significant outlier with a **27.56%** cancellation rate, identifying it as a critical infrastructure bottleneck.
#### The Wednesday Peak
- Service instability peaks on **Wednesdays (5.99%)**, suggesting mid-week operational strain.

[![Station-wise-cancellation.png](https://i.postimg.cc/ydgj7Zjj/Station-wise-cancellation.png)](https://postimg.cc/5YJL3jZQ)

*Figure 3.2: Mapping critical failure points across the German rail network.*

## 6.3 Operating Patterns & Rush Hour Collapse

While diversity in train types at hubs increases complexity, the inability to manage simultaneous peak-hour arrivals leads to localized collapses.

[![peak-hours-train-chart.png](https://i.postimg.cc/MZB541v8/peak-hours-train-chart.png)](https://postimg.cc/4nJpH768)

*Figure 3.3: Visualizing the performance dip of S-Bahn and ICE services during peak hours.*

## 6.4 Advanced Insight: The "Route Fatigue" Phenomenon

Cancellations are cumulative. Logistic regression confirms that as a train progresses through its **Stop Sequence**, the probability of termination increases significantly.
Every additional stop adds a layer of risk.

[![route-fatigue.png](https://i.postimg.cc/SsM6BpQf/route-fatigue.png)](https://postimg.cc/S2mY93Mn)

*Figure 3.4: Statistical proof of the correlation between stop number and cancellation risk.*

## 6.5 Key Cancellation Drivers

| Factor        | Key Finding | Statistical Support (p-value) |
|--------------|------------|-------------------------------|
| **Train Type** | IC (6.75%) and S-Bahn (5.93%) are the most vulnerable. | Chi-Square p < 0.001 |
| **Time of Day** | Peak cancellations occur at 18:00. | Logistic Regression p < 0.001 |
| **Day of Week** | Wednesday is the most unstable day. | Chi-Square p < 0.001 |
| **Location** | Hamburg Dammtor (27.56%) is the primary failure point. | Chi-Square p < 0.001 |
| **Fatigue** | Risk increases as the Stop Sequence progresses. | Logistic Regression p < 0.001 |

## 6.6 Conclusion

These findings indicate that cancellations arise from layered mechanisms: delay accumulation, peak-hour congestion, infrastructure bottlenecks, and route progression effects. Having examined train-level drivers of cancellations, we now shift perspective to stations as operational nodes within the network.

# 7. How Do Stations Differ Structurally?

## 7.1 Distributional Delay Structure Across Stations

Major hub stations exhibit larger median delays and wider IQR ranges than smaller stations. High p90 values imply a higher occurrence of extreme delays at these stations.

Overall, infrastructure complexity and traffic density appear to contribute to structural delay heterogeneity.

**Figure 2:** Station delay structure (Median + IQR + p90 tail)  
![Figure 2: Station delay structure](../additional_materials/images/2.png)

While distributional metrics highlight structural delay heterogeneity across stations, clustering techniques allow us to group stations into broader operational profiles.

## 7.2 How do different station clusters perform based on delay and other factors? 

We transformed the data on train rides into a set of profiles for each of the 107 traced stations, which includes average delay, cancellation rate, amount of trains passing through, and maximum delay for each station. 

### 7.2.1 Checking distribution of delays, cancellations and traffic volume

The distribution plots show that the majority of stations handle standard train volumes and keep average delays between 2 and 6 minutes. However, a small number of extreme outliers exist with exceptionally high traffic and severe delays.

![alt text](../additional_materials/images/exam_distributions.png)

### 7.2.2 Exploring correlation between delays and traffic volume

 Our assumption that high traffic volume alone does not cause high delays was confirmed by a Pearson correlation test with coefficient = -0.018. This means operational problems are linked to specific local conditions at the stations, rather than just their size. Distribution plotting showed skewed distribution, so data was normalised and scaled for further clustering of stations.

 ### 7.2.3 Identifying clusters of stations

To group the stations by their operational performance, we applied Agglomerative hierarchical clustering, which showed 3 distinct clusters of stations.

![alt text](../additional_materials/images/exam_dendrogram.png)

Based on this, we used Principal Component Analysis to check how features contributed to clustering. We found that:
- the PCA explains 71% of variance, which is a strong result that our analysis can explain tendencies reliably
- cluster 1 tends to be the most efficient, having lower delay times, while clusters 2 and 3 have more delays and cancellations
- cluster 2 tends to include busier stations with more traffic than cluster 3, while cluster 1 includes both quiet and busy stations. 
This indicates an opportunity for comparing high-performing and low-performing stations of the same size and finding what is different between them.

![alt text](../additional_materials/images/exam_pca.png)

### 7.2.4 Comparing profiles of station clusters

The clustering results show three distinct types of train stations based on their daily operations. A silhouette score of 0.25 confirms that these three groups are clearly separated and represent actual operational patterns in the railway network.

![alt text](../additional_materials/images/exam_clusters.png)

**Cluster 1** (55 stations): These stations handle an average of 11,547 trains and maintain the lowest average delay across the network at 3.87 minutes. This is also the largest group, including almost 50% of all stations in the dataset, which points at a relative reliability of the railway service. These stations can serve as example of best practices for stations in other clusters.

**Cluster 2** (13 stations): This small group (around 10% of all stations) represents severe outliers in punctuality. While they have the lowest average traffic volume of 10,798 trains, their average delay is the highest at 8.08 minutes. It is recommended to address this underperformance by investigating structural issues in the timetable or local infrastructure.

**Cluster 3** (39 stations): This group represents the major network hubs, accounting for around 40% of all stations. They handle almost three times the traffic volume of the other clusters at 31,120 trains on average, and they carry the highest average cancellation rate of 0.046. They are likely to have certain infrastructural challenges as well, since our analysis shows that traffic volume alone cannot explain high delays and cancellations.

### 7.2.5 Comparing stations across regions

While our analysis is strictly limited to a sample of 107 monitored stations and does not represent the entirety of Germany's railway network, mapping these stations geographically reveals clear operational patterns. The standard stops in Cluster 1 and the major hubs in Cluster 3 closely follow the baseline distribution, with the highest station counts predictably located in heavily populated states like North Rhine-Westphalia, Bavaria, and Baden-Württemberg. 

In contrast, the underperforming stations in Cluster 2 show a distinct regional anomaly, as they are disproportionately concentrated in Lower Saxony rather than following the expected nationwide baseline. In particular, while Lower Saxony accounts for only 8% of the total monitored network, it contains nearly 40% of the heavily delayed stations, including Lüneburg.

![alt text](../additional_materials/images/exam_regions.png)

## 7.3 Conclusion

Our analysis of 107 stations demonstrates that traffic volume is not the primary driver of delays, but rather specific operational profiles. Agglomerative clustering identified three distinct groups: low-delay stations (50%), underperforming stations (10%) and busy transport hubs (40%). A geographic mapping revealed regional bottlenecks in Lower Saxony and North Rhine-Westphalia. These findings suggest that infrastructure investments should be prioritised in certain regions. Station-level heterogeneity confirms that unreliability is not merely a function of traffic volume but of structural operational profiles embedded in specific regions and hubs.

# 8. Disclaimer on Methodogical Limitations

This analysis is based on a subset of monitored stations and a single month (October 2025). As a result, findings may not generalize to underrepresented regions or to periods with unusual disruption. In addition, the dataset does not include exogenous drivers such as infrastructure failures or weather conditions, which likely contribute to extreme delays and cancellations. Therefore, the results should be interpreted as structural associations rather than causal effects.

# 9. Overall Conclusion
This study provides a multi-layered analysis of railway reliability in the German rail network.
First, delay duration proves difficult to predict using observable operational variables, with models explaining only around one quarter of variance. Extreme delay events remain largely unexplained.
Second, substantial structural differences exist across train types, particularly in variability and delay magnitude. Long-distance and operationally complex services exhibit greater instability.
Third, delay severity significantly increases cancellation probability, revealing a clear escalation mechanism. However, effect sizes suggest that cancellations cannot be explained by delay alone.
Fourth, systemic drivers, including peak-hour congestion, geographic bottlenecks, and route fatigue, play a decisive role in shaping cancellation risk.
Finally, station-level clustering demonstrates that unreliability reflects distinct operational profiles rather than simple traffic volume. Certain regions and hubs exhibit persistent structural weaknesses.
Overall, railway unreliability appears to be a layered phenomenon driven by interaction between structural heterogeneity, accumulated operational stress, and extreme disruption events that remain difficult to forecast using schedule-based variables alone.

# 9. AI Disclaimer
AI was used to create visualizations, resolve coding errors, and refine the text.

# 10. Appendix

Table 1.1: 

| Feature/variable          | Description | Data type | Number of Unique values | Missing values | Example values |
|:--------------------------|:------------|:----------|------------------------:|---------------:|:---------------|
| station_name              | Name of the station | object | 107 | 0 | Hamburg Hbf, München Ost, Köln Hbf, Stuttgart Hbf, Duisburg Hbf |
| xml_station_name          | Station name from the XML response | object | 130 | 0 | Hamburg Hbf, München Ost, Köln Hbf, Stuttgart Hbf, Duisburg Hbf |
| eva                       | EVA station number (unique station identifier used by Deutsche Bahn) | int64 | 131 | 0 | 8002549, 8000262, 8000207, 8000096, 8000086 |
| train_name                | Name of the train (e.g., "ICE 123", "RE 5") | object | 1573 | 0 | ME RB41, S 1, S 11, RE 8, RE 3 |
| final_destination_station | Final destination of the train | object | 1353 | 0 | Hamburg Hbf, Freising, Norf, Stuttgart Hbf, Düsseldorf Hbf |
| delay_in_min              | Delay in minutes (negative values indicate early arrival) | int64 | 367 | 0 | 34, 7, 16, 8, 21 |
| time                      | Actual event timestamp of the observation (arrival or departure record) | object | 44530 | 0 | 2025-10-01 00:00:00, 2025-10-01 00:01:00 |
| is_canceled               | Indicates whether the train stop was canceled | bool | 2 | 0 | False, True |
| train_type                | Category/type of train service (e.g., ICE, IC, RE, S-Bahn) | object | 55 | 0 | ME, S, RE, RB, ag |
| train_line_ride_id        | Unique identifier for a specific train ride (route instance) | float64 | 28924 | 988616 | 1859923136648078848, 579376073596484480 |
| train_line_station_num    | Position of the station within the train’s route sequence | int64 | 48 | 0 | 15, 2, 8, 5, 9 |
| arrival_planned_time      | Scheduled arrival time | object | 44338 | 446738 | 2025-09-30 23:26:00, 2025-09-30 23:52:00 |
| arrival_change_time       | Actual or updated arrival time | object | 44365 | 446699 | 2025-10-01 00:00:00, 2025-09-30 23:56:00 |
| departure_planned_time    | Scheduled departure time | object | 44353 | 445857 | 2025-09-30 23:53:00, 2025-09-30 23:44:00 |
| departure_change_time     | Actual or updated departure time | object | 44354 | 445805 | 2025-10-01 00:00:00, 2025-10-01 00:01:00 |
| id                        | Unique identifier for each train stop observation | object | 1989180 | 0 | -8566953819069085350-2509302158-15 |

Table 1.2: 

|                                    |   delay_in_min |
|:-----------------------------------|---------------:|
| count                              |     1989180.00 |
| mean                               |           4.89 |
| std                                |          10.95 |
| min                                |       -1435.00 |
| 25%                                |           0.00 |
| 50%                                |           1.00 |
| 75%                                |           5.00 |
| max                                |         386.00 |
| Variance                           |         119.79 |
| Dispersion index (Variance / Mean) |          24.50 |

Figure 2.1: Delay Distribution:

![alt text](../additional_materials/images/delay_distrib.png)

Figure 2.2: Residual Distribution: 

![alt text](../additional_materials/images/residualsRR.png)

Figure 2.3: Residuals vs Fitted: 

![alt text](../additional_materials/images/resVSfitted.png)

Figure 2.4: Q-Q Plot: 

![alt text](../additional_materials/images/qqPlot.png)


