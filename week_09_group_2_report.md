**Interstate Metro Traffic Volume**

0\. **Authors of the report**

| Name | Contribution |
| :---- | :---- |
| Megan Kelly-Ortiz | Data preprocessing, GLM, Visulatizations, Report |
| Anna Perkova | Data preprocessing, GLM, Visulatizations, Report |
| Ayush | Data preprocessing, Random Forest Model, Visulatizations|
|  |   |
|  |   |
|  |   |

1\. **Dataset Overview** 

| Item | Description |
| :---- | :---- |
| Dataset name | Housing |
| Time Period | N/A |
| Number of rows | 1460 |
| Number of columns | 81 |
| Format file (.csv, .txt, etc) | .csv |
| Creator of the dataset | N/A |
| Source (name) | ASDA GitHub |
| Source (link) | N/A |

2\. **Dataset Structure** 

An initial selection of variables was made based on domain knowledge and check of category balance, with the selected features as follows:

| Feature/variable   | Data type   | Description   |   Number of Unique values | Example values                                        |
|:-------------------|:------------|:--------------|--------------------------:|:------------------------------------------------------|
| SalePrice          | int64       |               |                       663 | 208500.00, 181500.00, 223500.00, 140000.00, 250000.00 |
| LotArea            | int64       |               |                      1073 | 8450.00, 9600.00, 11250.00, 9550.00, 14260.00         |
| Neighborhood       | object      |               |                        25 | CollgCr, Veenker, Crawfor, NoRidge, Mitchel           |
| HouseStyle         | object      |               |                         8 | 2Story, 1Story, 1.5Fin, 1.5Unf, SFoyer                |
| YearBuilt          | int64       |               |                       112 | 2003.00, 1976.00, 2001.00, 1915.00, 2000.00           |
| YearRemodAdd       | int64       |               |                        61 | 2003.00, 1976.00, 2002.00, 1970.00, 2000.00           |
| Heating            | object      |               |                         6 | GasA, GasW, Grav, Wall, OthW                          |
| CentralAir         | object      |               |                         2 | Y, N                                                  |
| TotRmsAbvGrd       | int64       |               |                        12 | 8.00, 6.00, 7.00, 9.00, 5.00                          |
| FullBath           | int64       |               |                         4 | 2.00, 1.00, 3.00, 0.00                                |
| HalfBath           | int64       |               |                         3 | 1.00, 0.00, 2.00                                      |
| GrLivArea          | int64       |               |                       861 | 1710.00, 1262.00, 1786.00, 1717.00, 2198.00           |
| GarageCars         | int64       |               |                         5 | 2.00, 3.00, 1.00, 0.00, 4.00                          |
| PoolArea           | int64       |               |                         8 | 0.00, 512.00, 648.00, 576.00, 555.00                  |
| OpenPorchSF        | int64       |               |                       202 | 61.00, 0.00, 42.00, 35.00, 84.00                      |

3\. **Data cleaning** 

Since the selected features did not contain missing values and duplicates, data cleaning was not necessary. Categorical variables were encoded into dummy variables automatically by the models.

4\. **Descriptive statistics** 

Numeric columns

|                                    |      LotArea |   YearBuilt |   YearRemodAdd |   TotRmsAbvGrd |   FullBath |   HalfBath |   GrLivArea |   GarageCars |   PoolArea |   OpenPorchSF |
|:-----------------------------------|-------------:|------------:|---------------:|---------------:|-----------:|-----------:|------------:|-------------:|-----------:|--------------:|
| count                              |     1460.000 |    1460.000 |       1460.000 |       1460.000 |   1460.000 |   1460.000 |    1460.000 |     1460.000 |   1460.000 |      1460.000 |
| mean                               |    10516.828 |    1971.268 |       1984.866 |          6.518 |      1.565 |      0.383 |    1515.464 |        1.767 |      2.759 |        46.660 |
| std                                |     9981.265 |      30.203 |         20.645 |          1.625 |      0.551 |      0.503 |     525.480 |        0.747 |     40.177 |        66.256 |
| min                                |     1300.000 |    1872.000 |       1950.000 |          2.000 |      0.000 |      0.000 |     334.000 |        0.000 |      0.000 |         0.000 |
| 25%                                |     7553.500 |    1954.000 |       1967.000 |          5.000 |      1.000 |      0.000 |    1129.500 |        1.000 |      0.000 |         0.000 |
| 50%                                |     9478.500 |    1973.000 |       1994.000 |          6.000 |      2.000 |      0.000 |    1464.000 |        2.000 |      0.000 |        25.000 |
| 75%                                |    11601.500 |    2000.000 |       2004.000 |          7.000 |      2.000 |      1.000 |    1776.750 |        2.000 |      0.000 |        68.000 |
| max                                |   215245.000 |    2010.000 |       2010.000 |         14.000 |      3.000 |      2.000 |    5642.000 |        4.000 |    738.000 |       547.000 |
| Variance                           | 99625649.650 |     912.215 |        426.233 |          2.642 |      0.304 |      0.253 |  276129.633 |        0.558 |   1614.216 |      4389.861 |
| Dispersion index (Variance / Mean) |     9472.975 |       0.463 |          0.215 |          0.405 |      0.194 |      0.661 |     182.208 |        0.316 |    585.093 |        94.081 |

Categorical variables

|              |   Unique Values | Most Frequent   |   Frequency |   Percentage |
|:-------------|----------------:|:----------------|------------:|-------------:|
| Neighborhood |              25 | NAmes           |      225.00 |        15.41 |
| HouseStyle   |               8 | 1Story          |      726.00 |        49.73 |
| Heating      |               6 | GasA            |     1428.00 |        97.81 |
| CentralAir   |               2 | Y               |     1365.00 |        93.49 |






**6\. AI Disclaimer**
AI was used for the plots and conceptual understanding of the various parameters of the models 