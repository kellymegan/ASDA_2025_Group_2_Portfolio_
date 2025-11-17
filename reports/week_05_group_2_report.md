**World Bank Project Report**

0\. **Authors of the report**

| Name | Contribution |
| :---- | :---- |
| Megan Kelly-Ortiz | Data Cleaning, Group Comparison (Life Expectancy) |
|  |   |
|  |   |
|  |   |
|  |   |

1\. **Dataset Overview** 

| Item | Description |
| :---- | :---- |
| Dataset name | World Bank Development Indicators |
| Number of rows |  17272 |
| Number of columns | 50  |
| Format file (.csv, .txt, etc) | .csv  |
| Authors of the dataset |  World Bank Group |
| Source (name) |  World Bank Group  |
| Source (link) |  https://github.com/datagus/ASDA2025/tree/main/datasets/homework_week5 |

   
   
2\. **Dataset Structure** 

| Feature/variable                          | Data type   | Description   |   Number of Unique values | Example values                                                                                                                               |
|:------------------------------------------|:------------|:--------------|--------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------|
| country                                   | object      |               |                       203 | Afghanistan, Albania, Algeria, Angola, Antigua and Barbuda                                                                                   |
| date                                      | object      |               |                        62 | 1960-01-01, 1961-01-01, 1962-01-01, 1963-01-01, 1964-01-01                                                                                   |
| agricultural_land%                        | float64     |               |                      7634 | 57.88, 57.96, 58.03, 58.12, 58.12                                                                                                            |
| forest_land%                              | float64     |               |                      4834 | 1.85, 28.79, 28.72, 28.65, 28.57                                                                                                             |
| land_area                                 | float64     |               |                       724 | 652230.00, 27400.00, 2381740.00, 2381741.00, 1246700.00                                                                                      |
| avg_precipitation                         | float64     |               |                       175 | 327.00, 1485.00, 89.00, 1010.00, 1030.00                                                                                                     |
| trade_in_services%                        | float64     |               |                      6669 | 5.94, 4.93, 5.61, 20.21, 20.56                                                                                                               |
| control_of_corruption_estimate            | float64     |               |                      4226 | -1.29, -1.18, -1.27, -1.25, -1.34                                                                                                            |
| control_of_corruption_std                 | float64     |               |                      2436 | 0.34, 0.32, 0.35, 0.35, 0.27                                                                                                                 |
| access_to_electricity%                    | float64     |               |                      3062 | 4.45, 9.29, 14.13, 18.97, 23.81                                                                                                              |
| renewvable_energy_consumption%            | float64     |               |                      3824 | 23.00, 23.69, 27.38, 28.50, 30.14                                                                                                            |
| electric_power_consumption                | float64     |               |                      5628 | 532.03, 568.40, 593.45, 591.03, 739.35                                                                                                       |
| CO2_emisions                              | float64     |               |                      5535 | 2046.87, 1941.37, 1525.47, 1527.89, 1493.59                                                                                                  |
| other_greenhouse_emisions                 | float64     |               |                      5641 | 11630.80, 11899.99, 11548.26, 11678.76, 11733.05                                                                                             |
| population_density                        | float64     |               |                     11003 | 13.48, 13.75, 14.04, 14.34, 14.67                                                                                                            |
| inflation_annual%                         | float64     |               |                      8093 | 12.69, 6.78, 8.68, 26.42, -6.81                                                                                                              |
| real_interest_rate                        | float64     |               |                      4173 | 10.05, -3.59, 12.56, 17.54, 11.36                                                                                                            |
| risk_premium_on_lending                   | float64     |               |                      2192 | 9.69, 6.18, 6.15, 0.11, 4.08                                                                                                                 |
| research_and_development_expenditure%     | float64     |               |                      2162 | 0.09, 0.15, 0.23, 0.37, 0.20                                                                                                                 |
| central_goverment_debt%                   | float64     |               |                      1766 | 35.76, 37.48, 53.11, 55.57, 69.64                                                                                                            |
| tax_revenue%                              | float64     |               |                      4142 | 6.97, 5.28, 6.09, 8.48, 9.17                                                                                                                 |
| expense%                                  | float64     |               |                      3952 | 20.58, 24.24, 50.72, 44.32, 50.86                                                                                                            |
| goverment_effectiveness_estimate          | float64     |               |                      4109 | -2.18, -2.10, -2.17, -1.59, -1.18                                                                                                            |
| goverment_effectiveness_std               | float64     |               |                      1606 | 0.19, 0.30, 0.33, 0.26, 0.30                                                                                                                 |
| human_capital_index                       | float64     |               |                       559 | 0.39, 0.39, 0.40, 0.54, 0.62                                                                                                                 |
| doing_business                            | float64     |               |                       179 | 173.00, 82.00, 157.00, 177.00, 113.00                                                                                                        |
| time_to_get_operation_license             | float64     |               |                       232 | 13.80, 13.70, 21.20, 12.20, 10.90                                                                                                            |
| statistical_performance_indicators        | float64     |               |                      1006 | 37.22, 42.58, 49.84, 49.76, 54.40                                                                                                            |
| individuals_using_internet%               | float64     |               |                      4384 | 0.00, 0.00, 0.00, 0.09, 0.11                                                                                                                 |
| logistic_performance_index                | float64     |               |                       507 | 1.21, 2.24, 2.30, 2.07, 2.14                                                                                                                 |
| military_expenditure%                     | float64     |               |                      7125 | 1.63, 1.87, 1.61, 1.72, 2.05                                                                                                                 |
| GDP_current_US                            | float64     |               |                      9602 | 537777811.11, 548888895.56, 546666677.78, 751111191.11, 800000044.44                                                                         |
| political_stability_estimate              | float64     |               |                      4219 | -2.42, -2.43, -2.44, -2.04, -2.20                                                                                                            |
| political_stability_std                   | float64     |               |                       555 | 0.47, 0.44, 0.45, 0.44, 0.35                                                                                                                 |
| rule_of_law_estimate                      | float64     |               |                      4292 | -1.79, -1.73, -1.78, -1.67, -1.56                                                                                                            |
| rule_of_law_std                           | float64     |               |                      2430 | 0.35, 0.33, 0.29, 0.30, 0.30                                                                                                                 |
| regulatory_quality_estimate               | float64     |               |                      4212 | -2.09, -2.06, -2.08, -1.81, -1.46                                                                                                            |
| regulatory_quality_std                    | float64     |               |                      1510 | 0.39, 0.44, 0.42, 0.30, 0.24                                                                                                                 |
| government_expenditure_on_education%      | float64     |               |                      4592 | 1.16, 1.12, 1.43, 1.30, 1.74                                                                                                                 |
| government_health_expenditure%            | float64     |               |                      3721 | 0.08, 0.65, 0.54, 0.53, 0.50                                                                                                                 |
| multidimensional_poverty_headcount_ratio% | float64     |               |                       264 | 51.70, 49.40, 51.80, 49.00, 46.20                                                                                                            |
| gini_index                                | float64     |               |                       369 | 27.00, 31.70, 30.60, 30.00, 29.00                                                                                                            |
| birth_rate                                | float64     |               |                      8499 | 50.34, 50.44, 50.57, 50.70, 50.83                                                                                                            |
| death_rate                                | float64     |               |                      7189 | 31.92, 31.35, 30.84, 30.36, 29.87                                                                                                            |
| life_expectancy_at_birth                  | float64     |               |                     11081 | 32.53, 33.07, 33.55, 34.02, 34.49                                                                                                            |
| population                                | float64     |               |                     12303 | 8622466.00, 8790140.00, 8969047.00, 9157465.00, 9355514.00                                                                                   |
| rural_population                          | float64     |               |                     11792 | 7898093.00, 8026804.00, 8163985.00, 8308019.00, 8458694.00                                                                                   |
| voice_and_accountability_estimate         | float64     |               |                      4313 | -1.91, -2.04, -2.03, -1.43, -1.18                                                                                                            |
| voice_and_accountability_std              | float64     |               |                      2329 | 0.26, 0.26, 0.25, 0.19, 0.21                                                                                                                 |
| intentional_homicides                     | float64     |               |                      3702 | 4.07, 3.49, 4.21, 6.39, 9.98                                                                                                                 |
| Income_group                              | object      |               |                         4 | Low income, Upper middle income, Lower middle income, High income                                                                            |
| Region                                    | object      |               |                         7 | Middle East, North Africa, Afghanistan & Pakistan, Europe & Central Asia, Sub-Saharan Africa, Latin America & Caribbean, East Asia & Pacific |

 

3\. **Data cleaning** 

| Issue | Names of Columns affected | Description of the Issue | Action Taken |
| :---- | :---- | :---- | :---- |
| Inconsistent column labeling |   |   |   |
| Wrong data types |   |   |   |
| Missing values |   |   |   |
| Duplicates |   |   |   |
| Inconsistent categories |   |   |   |
| Other |  |  |  |

4\. **Descriptive statistics**   
Numeric columns

|   | Column 1 | Column 2 | Column 3 |
| :---- | :---- | :---- | :---- |
| Count |   |   |   |
| Mean |   |   |   |
| Standard deviation |   |   |   |
| Min |   |   |   |
| 25% |   |   |   |
| 50% |   |   |   |
| 75% |   |   |   |
| Max |   |   |   |

   
Category columns

|   | Column 1 | Column 2 | Column 3 |
| :---- | :---- | :---- | :---- |
| Count |   |   |   |
| Number of unique values |   |   |   |
| Most frequent value |   |   |   |
| Most frequent value (frequency) |   |   |   |
| Least frequent value |   |   |   |
| Least frequent value (frequency) |   |   |   |

 

**5\. Analysis \- Research question**

**6\. AI Disclaimer**

