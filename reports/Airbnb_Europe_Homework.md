# Airbnb Europe Homework

## 0. Authors of the Report

| Name | Contribution |
|------|---------------|
|   Ayush   |       Analysis with Visualisations       |
|   Onkar   |       Summarising and Report Creation    |
|   Anna    |       Statistical tests                  |
|      |               |
|      |               |

---

## 1. Dataset Overview

| Item | Description |
|------|--------------|
| **Dataset name** | Airbnb Prices in European Cities |
| **Number of rows** | 51,707 |
| **Number of columns** | 26 |
| **File format** | Excel (.xlsx) |
| **Authors of the dataset** | Publicly compiled dataset |
| **Source name** | Airbnb Prices in European Cities Data |
| **Source link** | [Google Sheets - Airbnb Prices Dataset](https://docs.google.com/spreadsheets/d/1ecopK6oyyb4d_7-QLrCr8YlgFrCetHU7-VQfnYej7JY/export?format=xlsx) |

---

## 2. Dataset Structure

| Feature / Variable | Data Type | Description | # Unique Values | Example Values |
|--------------------|------------|--------------|------------------|----------------|
| **price** | Float | The total price of the Airbnb listing (`realSum`) | Continuous | 194.03, 211.34 |
| **city** | Object | City where the listing is located | 10 | london, amsterdam, vienna |
| **country** | Object | Country where the listing is located | 10 | uk, netherlands, austria |
| **weekday/weekend** | Object | Indicates if the pricing is for weekdays or weekends | 2 | weekdays, weekends |
| **room_type_clean** | Object | Categorized type of room | 3 | entire home/apt, private room, shared room |
| **person_capacity** | Int | Max number of people accommodated | 6 | 2, 4 |
| **host_is_superhost** | Bool | Indicates if host is a Superhost | 2 | True, False |
| **guest_satisfaction_overall** | Int | Overall guest satisfaction (0–100) | 81 | 95, 100 |
| **dist** | Float | Distance from city center (km) | Continuous | 3.19, 1.45 |
| **bedrooms** | Int | Number of bedrooms | 11 | 1, 2 |

---

## 3. Data Cleaning Summary

| Issue | Columns Affected | Description | Action Taken |
|--------|------------------|--------------|---------------|
| **Inconsistent column labeling** | `realSum`, `sheet` | Price column named `realSum`, metadata in sheet names | Renamed `realSum` → `price`. Extracted city and weekday/weekend info. |
| **Wrong data types** | `guest_satisfaction_overall` | Loaded as float/decimal | Converted to `int64` |
| **Missing values** | All columns | Checked for missing values | None found (dataset complete) |
| **Duplicates** | All columns | Checked for exact duplicates | None found |
| **Inconsistent categories** | `room_shared`, `room_private`, `room_type` | Redundant boolean columns | Consolidated into `room_type_clean` (3 categories) |
| **Other** | `city`, `multi`, `biz` | Missing grouping for country; fragmented host data | Added `country` and `host_listing_count` features |

---

## 4. Descriptive Statistics

### Numeric Columns

| Statistic | Price | Guest Satisfaction | Distance (km) |
|------------|--------|--------------------|----------------|
| **Count** | 51,707 | 51,707 | 51,707 |
| **Mean** | 277.26 | 92.63 | 3.19 |
| **Std. Dev.** | 331.25 | 8.95 | 2.39 |
| **Min** | 13.79 | 20.00 | 0.02 |
| **25%** | 148.75 | 90.00 | 1.45 |
| **50% (Median)** | 211.34 | 95.00 | 2.61 |
| **75%** | 319.69 | 99.00 | 4.26 |
| **Max** | 18,545.45 | 100.00 | 25.28 |

---

### Categorical Columns

| Column | # Unique | Most Frequent | Frequency | Least Frequent | Frequency |
|---------|-----------|----------------|-------------|----------------|-------------|
| **city** | 10 | London | 9,993 | Budapest | 2,697 |
| **room_type_clean** | 3 | Entire home/apt | 32,648 | Shared room | 2,588 |
| **host_is_superhost** | 2 | False | 39,019 | True | 12,688 |

---

## 5. Analysis – Research Question

> *How do Airbnb listings, prices, and guest satisfaction differ across European cities, and do any of these patterns suggest housing pressure or early signs of gentrification?*

[![Screenshot-2025-11-10-at-10-49-03-PM](https://i.postimg.cc/DZZhX6S7/Screenshot-2025-11-10-at-10-49-03-PM.png)](https://postimg.cc/wtSnKh5r)
- **Cities with larger Airbnb markets like London, Rome, and Paris dominate in listing volumes**, highlighting their popularity and maturity in the short-term rental space.  
- **Amsterdam and Paris command the highest median prices (€460 and €317)**, indicating strong demand despite smaller supply — a sign of **tight regulation and premium market positioning**.

[![Screenshot-2025-11-10-at-10-49-16-PM](https://i.postimg.cc/1ttSqB83/Screenshot-2025-11-10-at-10-49-16-PM.png)](https://postimg.cc/DWtRVqQ9)
## Insights from the East-West Comparison of Airbnb Markets

-   **Clear Price Divide Between Regions**\
    Western cities (London, Paris, Amsterdam) have **significantly
    higher median prices**, reflecting stronger tourism demand and
    higher living costs.

-   **Noticeable Gap in Guest Satisfaction**\
    The **\~2-point lower median satisfaction** in Western cities is
    meaningful, suggesting **higher expectations and reduced perceived
    value** among guests.

-   **Better Value Perception in the East**\
    Eastern cities (Budapest, Athens, Vienna) combine **lower prices
    with higher satisfaction**, offering **better value-for-money
    experiences**.


[![Screenshot-2025-11-10-at-10-49-40-PM](https://i.postimg.cc/0QBsdSSP/Screenshot-2025-11-10-at-10-49-40-PM.png)](https://postimg.cc/dkrpJLnx)
## Insights from City-Level Price and Satisfaction Comparison

- **Inverse Relationship Between Price and Satisfaction**  
  Cities with **higher median prices (Paris, London)** generally show **lower guest satisfaction**, indicating diminishing perceived value at higher cost levels.  

- **High Satisfaction in Lower-Priced Markets**  
  **Athens, Budapest, and Vienna** achieve the **highest satisfaction scores** despite lower median prices, emphasizing **better affordability and experience balance**.  


[![Screenshot-2025-11-10-at-10-49-53-PM](https://i.postimg.cc/yddKZjDW/Screenshot-2025-11-10-at-10-49-53-PM.png)](https://postimg.cc/Y4JTc1fw)
##  Superhosts and Guest Satisfaction Across Cities

- **Superhosts Consistently Outperform Non-Superhosts**  
  Listings managed by **Superhosts show noticeably higher median satisfaction** and smaller variability, indicating a more reliable guest experience.  

- **Cities with More Superhosts Tend to Score Higher**  
  Cities like **Athens and Budapest**, which have a **larger share of Superhosts**, also report **higher overall satisfaction**, suggesting that host professionalism directly influences guest ratings.  

- **Why Does Athens Lead in Guest Satisfaction?**  
  **Athens stands out with both the highest Superhost ratio (~43%) and top satisfaction scores**, showing that a **greater concentration of experienced hosts** drives better service quality and trust among guests.  

[![Screenshot-2025-11-10-at-10-50-09-PM](https://i.postimg.cc/9MM27bDD/Screenshot-2025-11-10-at-10-50-09-PM.png)](https://postimg.cc/bGK4XQHP)
 ## What's wrong with the high priced listings ?
**High-priced listings show greater variability in satisfaction**, indicating that **paying more doesn’t guarantee a better experience** — premium properties have **inconsistent service quality** leading to wider satisfaction spread. Amongst all the other price quartiles, listings that are listed on a premium price have higher variability of guest satisfaction. The reason could be that guests often have high expectations with regards to the price they are paying and these listings might not be able to justify that.

[![Screenshot-2025-11-10-at-10-50-21-PM](https://i.postimg.cc/4dSgbccJ/Screenshot-2025-11-10-at-10-50-21-PM.png)](https://postimg.cc/8JM9Tjw3)
## Is there a trend in these markets with respect to weekends and weekdays? 
**Weekend price surges vary sharply across cities**, with **Amsterdam charging ~€60 more** on weekends, while **Barcelona and Athens show no weekend premium** — likely because they **receive similar or higher booking volumes on weekdays**, keeping demand (and prices) steady throughout the week.

[![Screenshot-2025-11-10-at-10-50-31-PM](https://i.postimg.cc/Y9sHfFF9/Screenshot-2025-11-10-at-10-50-31-PM.png)](https://postimg.cc/0MDF9bcR)
## Do hosts of all levels provide similiar Guest experience?
**Hosts with fewer listings achieve higher guest satisfaction**, as **individual hosts (single-property owners)** tend to provide **more personal attention and better service**, while large multi-listing hosts often face **quality consistency issues** across their properties.

[![Screenshot-2025-11-10-at-10-50-40-PM](https://i.postimg.cc/26KDFWWV/Screenshot-2025-11-10-at-10-50-40-PM.png)](https://postimg.cc/zbK6qV0r)
## Does Guest satisfaction vary with respect to room type?
**Shared rooms consistently receive lower guest satisfaction** across most cities, likely due to **reduced privacy and comfort levels** — however, **Budapest stands out** as an exception, where **shared accommodations outperform** other room types, suggesting **better community-oriented experiences or host quality**.

[![Screenshot-2025-11-10-at-10-50-57-PM](https://i.postimg.cc/Y9sHfFFG/Screenshot-2025-11-10-at-10-50-57-PM.png)](https://postimg.cc/ygct7kvs)


This exploratory analysis aims to:
- Compare Airbnb price distributions across major European cities.  
- Assess whether distance from the city center correlates with price or satisfaction.  
- Explore whether Superhost status, room type, and capacity influence listing prices.  
- Identify potential signs of gentrification by examining pricing and availability patterns near city centers.

---

### Notes
- Statistical tests confirmed significant difference of the factors described in the report.
- All code and figures supporting this report are included in the accompanying Jupyter Notebook.  
- The goal is to provide insights for policymakers focused on sustainable urban housing.

---

*Prepared for the European Commission for Sustainable Cities*  
*Exploratory Data Analysis: Airbnb Europe Dataset*
