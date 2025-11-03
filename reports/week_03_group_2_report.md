# **Group 2 Lego Dataset Report**

03/11/2025

---

## 1.  **Dataset Overview**

|  Item |  Description |
|--------|----------------|
|  Dataset name | Lego_Database1-11-2025.xlsx |
|  Authors | Leuphana Applied Statistical Data Analysis students of WiSe2025 |
|  Number of entries | 204 |
|  Number of features/variables | 12 |
|  Format file (.csv, .txt, etc) | .xlsx (clean exported to .csv) |

---
## 2. Dataset Structure (of the clean version)

| Feature/variable | Data type | Description | Number of Unique values | Example values |
| :---- | :---- | :---- | :---- | :---- |
| Color | Object | The color of the piece. | 12 | Blue, green, red, yellow, orange |
| Is Duplo? | Object | If the piece is duple or not. | 2 | 1, 0 |
| Size type | Object | The type of the piece, brick or plate. | 2 | Brick, plate |
| Base shape | object | The shape of the piece. | 8 | Rectangle, square, circle, triangle, trapezoid. |
| Base dimensions | object | Dimensions of the base. Counted using the number of studs. | 13 | 2x4, 2x2, 2x8, 1x4, 1x3 |
| Number of studs | float64 | The number of studs per piece. | 10 | 1, 3, 4, 6, 8 |
| Has slope? | Object | If the piece has slope | 2 | 1, 0 |
| Slope degree | float64 | Degree of the slope if has. | 4 | 0, 15, 30, 45 |
| In stock | Object | If the piece is in the bag. | 2 | 1, 0 |
| Transparent | Object | If the piece is transparent or not. | 2 | 1, 0 |
| Base color shade | Object | The base color of the piece | 12 | Green, blue, red, yellow, orange |

## 3. Descriptive statistics (of the clean version)

#### Numeric columns

| Metric | id | number of studs | slope degree | in stock |
|:--|--:|--:|--:|--:|
| **Count** | 204 | 204 | 204 | 204 |
| **Mean** | 102.50 | 4.9069 | 5.0735 | 1.0000 |
| **Standard deviation** | 59.0339 | 4.9962 | 14.1114 | 0.0000 |
| **Min** | 1.0 | 0.0 | 0.0 | 1.0 |
| **25%** | 51.75 | 2.00 | 0.00 | 1.0 |
| **50%** | 102.5 | 4.0 | 0.00 | 1.0 |
| **75%** | 153.25 | 6.0 | 0.00 | 1.0 |
| **Max** | 204.0 | 24.0 | 45.0 | 1.0 |

---

#### Categorical/object columns

| Metric | color | color base shade | is duplo? | size type | base shape | transparent |
|:--|--:|--:|--:|--:|--:|--:|
| **Count** | 204 | 204 | 204 | 204 | 204 | 204 |
| **Number of unique values** | 63 | 12 | 2 | 2 | 5 | 2 |
| **Most frequent value** | yellow | blue | False | plate | rectangle | False |
| **Most frequent value (frequency)** | 16 | 39 | 171 | 108 | 109 | 200 |
| **Least frequent value** | transparentskyblue | transparent | True | brick | triangle | True |
| **Least frequent value (frequency)** | 1 | 1 | 33 | 96 | 3 | 4 |


## Visualizations
[![Screenshot-2025-11-03-at-7-04-28-PM.png](https://i.postimg.cc/FKWfP9P7/Screenshot-2025-11-03-at-7-04-28-PM.png)](https://postimg.cc/hJmPvqRB)
[![Screenshot-2025-11-03-at-7-06-04-PM.png](https://i.postimg.cc/HnCTzRC1/Screenshot-2025-11-03-at-7-06-04-PM.png)](https://postimg.cc/Pp2Gr6xS)
[![Screenshot-2025-11-03-at-7-07-03-PM.png](https://i.postimg.cc/YCVK8Z1D/Screenshot-2025-11-03-at-7-07-03-PM.png)](https://postimg.cc/SnWvxZ1c)
[![Screenshot-2025-11-03-at-7-08-22-PM.png](https://i.postimg.cc/QtJzLyTZ/Screenshot-2025-11-03-at-7-08-22-PM.png)](https://postimg.cc/MMX5Vt59)
[![Screenshot-2025-11-03-at-7-09-17-PM.png](https://i.postimg.cc/B64hCBwB/Screenshot-2025-11-03-at-7-09-17-PM.png)](https://postimg.cc/t1vtqWbs)
[![Screenshot-2025-11-03-at-7-10-42-PM.png](https://i.postimg.cc/j53zJ6V4/Screenshot-2025-11-03-at-7-10-42-PM.png)](https://postimg.cc/r0WdBrwD)

---

## **4. Data cleaning procedure**

### **4.1 Major data inconsistencies**

| Issue | Names of Columns Affected | Description of the Issue | Action Taken |
| --- | --- | --- | --- |
| Missing values in identifier column | id | The 'id' column was empty after combining sheets from the Excel file. | Assigned sequential integers starting from 0 to create unique identifiers for each row. |
| Inconsistent formatting in dimensions | base dimensions | Values had varying separators (e.g., 'x', 'X', '*', spaces) and orders, including one anomalous combined value ('2 x 4 + 2 x 2'). | Dropped the anomalous row; standardized by stripping spaces and replacing separators with '*' using a regex-based cleaning function. |
| Missing values in transparency indicator | transparent | Column had 164 missing values (NaN). | Filled missing values with 0 to indicate non-transparent. |
| Inconsistent casing across string columns | All string columns (e.g., color, base shape, size type) | Values had mixed capitalization, leading to potential duplicates in unique counts. | Converted all string values in the dataset to lowercase. |
| Mixed representations in boolean column | is duplo? | Column contained booleans (True/False) and strings ('yes'/'no'). | Mapped 'yes' to True and 'no' to False across the dataset. |
| Inconsistent synonyms in shape categories | base shape | Variations like 'trapezium' vs. 'trapezoid', 'round' vs. 'circle', and 'wadge' vs. 'triangle'. | Stripped spaces and mapped synonyms to standardized terms (e.g., 'trapezium' to 'trapezoid'). |
| Synonymous values in type column | size type | 'tile' was used interchangeably with 'plate'. | Replaced 'tile' with 'plate' for consistency. |
| Missing values in slope angle | slope degree | Column had 36 missing values (NaN) for non-sloped pieces. | Filled missing values with 0 to indicate no slope. |
| Inconsistent binary representation in stock | in stock | Column used booleans (True) instead of numeric indicators. | Replaced True with 1 for binary consistency. |
| Complex variations in color descriptions | color | Colors had descriptors (e.g., 'dark', 'neon'), synonyms, typos, and concatenations (e.g., 'darkblue'), leading to many unique values. | Created a new 'Base color' column by mapping to standardized base shades using a custom function handling descriptors, synonyms, and typos. |

### **4.2. Minor data inconsistencies**

In addition to major cleaning efforts, minor issues included potential outliers in 'number of studs' (e.g., 0 values for certain pieces) and slight variations in data entry across sheets, such as inconsistent spacing. These were mitigated through normalization like lowercase conversion and targeted fills, ensuring uniformity without data loss. No row duplicates were detected post-combination, and the dataset structure was preserved for analysis.

---

## **5. Recommendations for good practices regarding data collection**

- Define expected format (data type) of each column  
- For categorical values: create a list of valid entries to choose from and avoid using free-text fields (e.g. color)  
- Use standardized naming conventions for columns and variables  
- Handle missing values with predefined rules (e.g., "NA", "0", or "Unknown")  

---

## 6\. AI Disclaimer
Partially AI-generated code was for creation of the new column base shade.
