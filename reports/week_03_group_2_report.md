# **Basic EDA Report**

1. Dataset Overview

| Item | Description |
| :---- | :---- |
| Dataset name | Titanic Dataset |
| Number of rows | 891 |
| Number of columns | 12 |
| Format file (.csv, .txt, etc) | .csv |
| Authors of the dataset | M Yasser H |
| Source (name) | Kaggle – M Yasser H |
| Source (link) | https:/[/www.kaggle.com/datasets/yasserh/titanic](http://www.kaggle.com/datasets/yasserh/titanic) \-dataset |

Short description (what is it about?)

The sinking of the Titanic is one of the most infamous shipwrecks in history.

On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding with an iceberg. Unfortunately, there weren’t enough lifeboats for everyone on board, resulting in the death of 1502 out of 2224 passengers and crew.

While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others.

In this challenge, we ask you to build a predictive model that answers the question: “what sorts of people were more likely to survive?” using passenger data (ie name, age, gender, socio-economic class, etc).

2. Structure of the dataset

| Column name | Data type | Non-null count | Unique values | Example values |
| :---- | :---- | :---- | :---- | :---- |
| PassengerId | Int64 | 891 | 891 | 1 |
| Survived | Int64 | 891 | 2 | 0 |
| Pclass | Int64 | 891 | 3 | 3 |
| Name | Object | 891 | 891 | Braund, Mr. Owen |
| Sex | Object | 891 | 2 | male |
| Age | Float64 | 714 | 88 | 22.0 |
| SibSp | Int64 | 891 | 7 | 1 |
| Parch | Int64 | 891 | 7 | 0 |

| Ticket | Object | 891 | 681 | A/5 21171 |
| :---- | :---- | :---- | :---- | :---- |
| Fare | Float64 | 891 | 248 | 7.25 |
| Cabin | Object | 204 | 147 | C85 |
| Embarked | object | 889 | 3 | S |

3. Descriptive statistics Numeric columns

Categorical/object columns

3. Missing values and duplicates

| Column name | Missing count | % Missing |
| :---- | :---- | :---- |
| PassengerId | 0 | 0.00 % |
| Survived | 0 | 0.00 % |
| Pclass | 0 | 0.00 % |
| Name | 0 | 0.00 % |
| Sex | 0 | 0.00 % |

| Age | 177 | 19.87 % |
| :---- | :---- | :---- |
| SibSp | 0 | 0.00 % |
| Parch | 0 | 0.00 % |
| Ticket | 0 | 0.00 % |
| Fare | 0 | 0.00 % |
| Cabin | 687 | 77.10 % |
| Embarked | 2 | 0.22 % |

Total missing values: 866

Percentage of dataset affected: 8.10 %

Duplicated rows found: 0  
Percentage of rows in dataset affected: 0.00 %

4. Data consistency

| Item | Description |
| :---- | :---- |
| Does the dataset contain unnecessary columns? Which? | No unnecessary columns; all are relevant (e.g., Name for identification, Survived for outcome). However, PassengerId and Ticket could be optional depending on analysis |
| Do the data types correspond to the columns? | Yes, mostly: Survived, Pclass, SibSp, Parch (int), Name, Sex, Ticket, Cabin, Embarked (object), Age, Fare (float). No mismatches. |
| Is the labelling of the columns appropriate? | Yes, labels like Sex, Age, Fare are clear and meaningful. |
| Are there mixed values in column (e.g., number and characters)? | No, columns are consistent (e.g., Ticket has mixed formats but all strings). |
| Are string column clean? | Mostly yes; Cabin has missing values (687/891), Embarked has 2 missing, but no trailing spaces or invalid entries. |
| Does the dataset look machine generated? | No, it’s a historical dataset from the 1912 Titanic disaster. |
| Other | None |

5. Overall assessment

Is it worth it to further analyze the dataset?

* Yes, the Titanic dataset is worth further analyzing. With 891 rows and rich features (e.g., Survived, Pclass, Sex, Age), it’s ideal for exploring survival patterns, building predictive models, and learning data science techniques. Its historical context adds value for insights into socio-economic factors.

What possible analysis can be performed?

* **EDA**: Histograms for Age, bar plots for Sex/Pclass vs. Survived, correlation heatmap.  
* **Stats**: T-tests to compare survival rates by Pclass, outlier detection in Fare.

* **Advanced**: Logistic regression for Survived, clustering by SibSp/Parch, feature engineering (e.g., FamilySize \= SibSp \+ Parch).

6. Next steps

- Handling missing values? How?

Yes, handle Cabin (687 missing), Age (177 missing), Embarked (2 missing). Use:

* For Age our strategy would be to look at the title present in the passenger’s name. For a person having Mr. or Mrs. title, we would just impute the mean of the respected titles.

  * For missing values in the *Embarked* column, we can impute them based on the mean *Fare* of each embarkation point, as the Fare generally correlates with where passengers boarded.

  * Further we can just drop Cabin as it is not very informative.


  
\-Removing duplicates?

Check with df.duplicated().sum(); if any, remove with df.drop\_duplicates(). Typically, no duplicates in Titanic.

\-Cleaning the columns? Which?

* Cabin: Many missing; consider dropping or extracting deck info (first letter).

* Ticket: Mixed formats; might need parsing or dropping.

* Name: Extract titles (e.g., "Mr", "Mrs") for feature engineering.

\-Creating a subset of the dataframe?

* df\[\['Survived', 'Pclass', 'Sex', 'Age'\]\] for survival analysis.

* df\[df\['Pclass'\] \== 1\] for first-class passengers only.