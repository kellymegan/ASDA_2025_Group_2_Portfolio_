# **Group 2 Lego Dataset Report**

03/11/2025

---

## 1.  **Dataset Overview**

| > Item | > Description |
|--------|----------------|
| > Dataset name | Lego_Database1-11-2025.xlsx |
| > Authors | Leuphana Applied Statistical Data Analysis students of WiSe2025 |
| > Number of entries | 204 |
| > Number of features/variables | 12 |
| > Format file (.csv, .txt, etc) | .xlsx (clean exported to .csv) |

---

## 2.  **Dataset Structure**

| > Feature/variable | > Data type | > Description | > Number of unique values | > Example values |
|---------------------|-------------|---------------|----------------------------|------------------|
|                     |             |               |                            |                  |
|                     |             |               |                            |                  |
|                     |             |               |                            |                  |

---

## **3. Descriptive statistics**

### Numeric columns

|              | > Column 1 | > Column 2 | > Column 3 |
|--------------|------------|------------|------------|
| > Count      |            |            |            |
| > Mean       |            |            |            |
| > Standard deviation |    |            |            |
| > Min        |            |            |            |
| > 25%        |            |            |            |
| > 50%        |            |            |            |
| > 75%        |            |            |            |
| > Max        |            |            |            |

---

### Categorical/object columns

|               | > Column 1 | > Column 2 | > Column 3 |
|---------------|------------|------------|------------|
| > Count       |            |            |            |
| > Number of unique values | |           |            |
| > Most frequent value |    |            |            |
| > Most frequent value (frequency) | |    |            |
| > Least frequent value |   |            |            |
| > Least frequent value (frequency) | |   |            |

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