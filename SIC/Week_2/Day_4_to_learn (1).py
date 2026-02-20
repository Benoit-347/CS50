import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_datareader import data as pdr
from pandas_datareader import wb
import datetime
from datetime import timedelta
import os

# =====================================================================
# CHUNK 1: Remote Data Services (FRED & World Bank) & Pivoting
# =====================================================================
print("--- Remote Data Services ---")
# Fetching 10-Year Treasury Constant Maturity Rate from FRED
start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2021, 1, 1)
try:
    gs10 = pdr.DataReader('GS10', 'fred', start, end)
    gs10.plot(title="10-Year Constant Maturity Yield", figsize=(10, 4))
    plt.show()
except Exception as e:
    print(f"FRED fetch failed: {e}")

# Fetching World Bank Data (Life Expectancy)
indicators = wb.get_indicators()
print("Top 5 Indicators:\n", indicators.head(5))

# Searching for life expectancy indicators
matches = wb.search('life expectancy')
print("Life Expectancy Indicators:\n", matches.iloc[:5, :2])

# Fetching Life Expectancy data for US, Canada, Mexico
try:
    le_data = wb.download(indicator='SP.DYN.LE00.IN', country=['US', 'CA', 'MX'], start=2015, end=2020)
    print("Life Expectancy Data:\n", le_data.head())
    
    # Pivoting the dataset
    le_pivot = le_data.reset_index().pivot(index='country', columns='year', values='SP.DYN.LE00.IN')
    print("Pivoted Life Expectancy:\n", le_pivot)
    
    # Finding the country with the minimum life expectancy each year
    print("Min Life Expectancy per year:\n", le_pivot.idxmin(axis=0, skipna=True))
except Exception as e:
    print(f"World Bank fetch failed: {e}")


# =====================================================================
# CHUNK 2: DataFrame Row/Column Operations (Dropping & Renaming)
# =====================================================================
print("\n--- DataFrame Manipulations ---")
# Mock Universities Dataset
univ_data = {
    "title": ["MIT", "Stanford", "Harvard", "Caltech", "Oxford", "Cambridge"],
    "location": ["US", "US", "US", "US", "UK", "UK"],
    "students staff ratio": [8.7, 9.9, 8.9, 6.5, 11.2, 10.9],
    "gender ratio": [45, 46, 49, 39, 46, 47],
    "score": [100, 99.5, 99.0, 98.5, 98.0, 97.5]
}
rank = pd.DataFrame(univ_data)

# Dropping Rows and Columns
rank_dropped_rows = rank.drop([0, 1], axis=0, inplace=False)
rank_dropped_cols = rank.drop(["students staff ratio", "gender ratio"], axis=1, inplace=False)

# Renaming Indexes and Columns
rank.rename(columns={"score": "total_score"}, inplace=True)
rank.rename(index={0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f"}, inplace=True)
print(rank.head())


# =====================================================================
# CHUNK 3: Slicing & Element Selection (loc & iloc)
# =====================================================================
print("\n--- Slicing DataFrames ---")
# iloc: Integer position-based indexing
print("iloc slicing:\n", rank.iloc[1:4])

# loc: Label-based indexing
print("loc slicing:\n", rank.loc[["a", "b"]])

# Selecting Columns
titles = rank["title"] # Returns a Series
titles_and_locs = rank[["title", "location"]] # Returns a DataFrame

# Selecting specific elements [row, col]
print("Specific element iloc:", rank.iloc[2, 1])
print("Specific element loc:", rank.loc["c", "location"])


# =====================================================================
# CHUNK 4: Filtering & Aggregating (Spotify Dataset Example)
# =====================================================================
print("\n--- Filtering & Logic ---")
spotify_data = {
    "Track": ["Song A", "Song B", "Song C", "Song D", "Song E"],
    "Artist": ["Post Malone", "Post Malone", "BTS", "Drake", "BTS"],
    "Artist_popularity": [96, 96, 98, 95, 98],
    "tempo": [120, 110, 105, 130, 115]
}
song = pd.DataFrame(spotify_data)

# Filtering with logical operators
pop_song = song[song["Artist_popularity"] >= 95]

# Finding unique artists and counting songs
unique_artists = pop_song["Artist"].unique()
print("Unique Artists:", unique_artists)

artist_counts = pop_song["Artist"].value_counts()
print("Songs per artist:\n", artist_counts)

# Filtering for specific string
bts_songs = song[song["Artist"] == "BTS"]
print("BTS Songs:\n", bts_songs)

# Resetting index
bts_songs = bts_songs.reset_index(drop=True)


# =====================================================================
# CHUNK 5: Correlation & Heatmaps
# =====================================================================
print("\n--- Correlation & Visualization ---")
# Creating numeric data to test correlation
corr_data = pd.DataFrame({
    "popularity": [80, 85, 90, 95, 99],
    "tempo": [110, 115, 120, 125, 130],
    "danceability": [0.6, 0.7, 0.8, 0.85, 0.9]
})

df_corr = corr_data.corr(method='pearson')
print("Correlation Matrix:\n", df_corr)

# Matplotlib Scatter Plot
plt.figure(figsize=(6, 4))
plt.scatter(corr_data["tempo"], corr_data["popularity"], color='blue')
plt.title("Tempo vs Popularity")
plt.xlabel("Tempo")
plt.ylabel("Popularity")
plt.grid(True)
plt.show()

# Heatmap using imshow
plt.figure(figsize=(6, 4))
plt.imshow(df_corr, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Correlation Heatmap')
plt.xticks(range(len(df_corr.columns)), df_corr.columns)
plt.yticks(range(len(df_corr.columns)), df_corr.columns)
plt.show()


# =====================================================================
# CHUNK 6: Data Tidying (Identifying Missing Data)
# =====================================================================
print("\n--- Data Tidying (Missing Data) ---")
# Loading seaborn titanic dataset
titanic = sns.load_dataset('titanic')

# Checking for missing data
print("Total NaN per column:\n", titanic.isnull().sum())
print("Non-null data per column:\n", titanic.notnull().sum())


# =====================================================================
# CHUNK 7: Dropping & Replacing Missing Data
# =====================================================================
print("\n--- Dropping & Replacing ---")
# Dropping columns with a threshold (e.g., must have 500 non-NaN values)
titanic_dropped_cols = titanic.dropna(axis=1, thresh=500, inplace=False)

# Dropping rows containing any NaN
titanic_dropped_rows = titanic.dropna(axis=0, how='any', inplace=False)

# 1) Replacing with Mean & Median
avg_age = titanic['age'].mean()
median_age = titanic['age'].median()
titanic['age_filled_mean'] = titanic['age'].fillna(avg_age)
titanic['age_filled_median'] = titanic['age'].fillna(median_age)

# 2) Replacing with Maximum/Most frequent value
most_embarked = titanic['embark_town'].value_counts(dropna=True).idxmax()
titanic['embark_town_filled'] = titanic['embark_town'].fillna(most_embarked)
print(f"Replaced missing embark_town with: {most_embarked}")


# =====================================================================
# CHUNK 8: Descriptive Statistics & Visualizations
# =====================================================================
print("\n--- Descriptive Stats & Box/Hist Plots ---")
# Simple numeric dataframe for stats
grades = pd.DataFrame({
    "absences": [0, 2, 4, 10, 20, 1, 0, 5, 8],
    "G1": [15, 14, 12, 10, 8, 16, 18, 11, 9],
    "G3": [16, 14, 13, 11, 7, 18, 19, 10, 8]
})

print("Variance:\n", grades.var())
print("Standard Deviation:\n", grades.std())

# Coefficient of Variation (CV) = std / mean
cv = grades.std() / grades.mean()
print("Coefficient of Variation (CV):\n", cv)

print("Covariance Matrix:\n", grades.cov())

# Histogram
plt.figure(figsize=(6, 4))
plt.hist(grades["absences"], bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram of Absences")
plt.grid(True)
plt.show()

# Boxplot
plt.figure(figsize=(6, 4))
plt.boxplot([grades["G1"], grades["G3"]], labels=["1st Semester", "Final Grade"])
plt.title("Grades Box Plot")
plt.grid(True)
plt.show()


# =====================================================================
# CHUNK 9: Time Series Basics (Datetime, Timedelta, Period)
# =====================================================================
print("\n--- Time Series Generation ---")
# 1. Python Datetime
today = datetime.date.today()
now = datetime.datetime.now()
print(f"Today: {today.year}-{today.month}-{today.day}")

# 2. Pandas Timestamp
ts1 = pd.Timestamp('2021-01-01 15:30:00')
print("Timestamp:", ts1)

# 3. Pandas Timedelta
td1 = pd.Timedelta(days=50, hours=8, minutes=5)
print("Timedelta added to Timestamp:", ts1 + td1)

# 4. Pandas Period
p1 = pd.Period('2021-07', freq='M')
print(f"Period starts: {p1.start_time}, ends: {p1.end_time}")
print("Shifted Period (+2 months):", p1 + 2)


# =====================================================================
# CHUNK 10: Datetime Indexing & Slicing
# =====================================================================
print("\n--- Datetime Indexing ---")
date_strings = ["2021-01-01", "2021-02-01", "2021-03-01", "2021-04-01"]
values = [100, 110, 105, 120]

df_time = pd.DataFrame({"Date": date_strings, "Value": values})

# Convert string to datetime and set as index
df_time["Date"] = pd.to_datetime(df_time["Date"], errors='coerce')
df_time.set_index("Date", inplace=True)
df_time = df_time.sort_index()

print("Time Series Slicing (Jan to Feb):")
print(df_time.loc['2021-01-01':'2021-02-28'])


# =====================================================================
# CHUNK 11: Date Ranges & Frequencies
# =====================================================================
print("\n--- Date Ranges & Period Ranges ---")
# Creating a date range (Daily frequency)
dr_daily = pd.date_range(start='2021-01-01', periods=5, freq='D')
print("Daily Range:", dr_daily)

# Creating a date range (Business Days)
dr_business = pd.date_range(start='2021-01-01', periods=5, freq='B')
print("Business Range:", dr_business)

# Creating a period range
pr_monthly = pd.period_range(start='2021-01', periods=5, freq='M')
print("Monthly Period Range:", pr_monthly)


# =====================================================================
# CHUNK 12: Rolling Windows & Area Plots (Seafood Dataset Logic)
# =====================================================================
print("\n--- Rolling Windows & Aggregations ---")
# Simulating Stock / Moving Average Data
np.random.seed(42)
days = pd.date_range(start='2020-01-01', periods=100, freq='D')
stock_prices = pd.DataFrame({"Close": np.random.randn(100).cumsum() + 50}, index=days)

# Calculating Rolling Moving Averages
stock_prices["5_day_MA"] = stock_prices["Close"].rolling(window=5).mean()
stock_prices["10_day_MA"] = stock_prices["Close"].rolling(window=10).mean()

# Line Plot with Rolling Windows
plt.figure(figsize=(10, 5))
plt.plot(stock_prices.index, stock_prices["Close"], label="Close", linewidth=2)
plt.plot(stock_prices.index, stock_prices["5_day_MA"], label="5-Day MA")
plt.plot(stock_prices.index, stock_prices["10_day_MA"], label="10-Day MA")
plt.title("Stock Price & Moving Averages")
plt.legend()
plt.show()

# Simulating Global Seafood Data for Area Chart
fish_data = pd.DataFrame({
    "Year": [1960, 1970, 1980, 1990, 2000, 2010, 2020],
    "Capture_Fisheries": [20, 30, 40, 50, 55, 58, 60],
    "Aquaculture": [2, 5, 10, 20, 35, 60, 85]
})
fish_data["Year"] = pd.to_datetime(fish_data["Year"], format='%Y')
fish_data.set_index("Year", inplace=True)

# Grouping (if we had multiple countries, we would group by index year)
global_fish = fish_data.groupby(fish_data.index).sum()

# Plotting an Area Graph
plt.figure(figsize=(10, 5))
global_fish.plot(kind='area', stacked=False, alpha=0.5, figsize=(10, 5))
plt.title("Capture Fisheries vs Aquaculture Production")
plt.ylabel("Production Volume")
plt.grid(True)
plt.show()

# Searching for specific country (Categorical simulation)
countries = pd.Series(["United States", "China", "India", "Norway"])
print("\nSearch for 'Norway' in countries:", (countries == "Norway").any())