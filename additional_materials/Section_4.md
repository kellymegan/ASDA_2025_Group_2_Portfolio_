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

Section 4.2: Minor Data Inconsistencies:

In addition to major cleaning efforts, minor issues included potential outliers in 'number of studs' (e.g., 0 values for certain pieces) and slight variations in data entry across sheets, such as inconsistent spacing. These were mitigated through normalization like lowercase conversion and targeted fills, ensuring uniformity without data loss. No row duplicates were detected post-combination, and the dataset structure was preserved for analysis.