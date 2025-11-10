# Airbnb Europe Homework

## 0. Authors of the Report

| Name | Contribution |
|------|---------------|
|      |               |
|      |               |
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

This exploratory analysis aims to:
- Compare Airbnb price distributions across major European cities.  
- Assess whether distance from the city center correlates with price or satisfaction.  
- Explore whether Superhost status, room type, and capacity influence listing prices.  
- Identify potential signs of gentrification by examining pricing and availability patterns near city centers.

---

### Notes
- The analysis is descriptive — no predictive modeling or statistical testing was performed.  
- All code and figures supporting this report are included in the accompanying Jupyter Notebook.  
- The goal is to provide insights for policymakers focused on sustainable urban housing.

---

*Prepared for the European Commission for Sustainable Cities*  
*Exploratory Data Analysis: Airbnb Europe Dataset*
