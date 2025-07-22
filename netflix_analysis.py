# Steps to visualize the data:
# 1. Load the data: Read the CSV file using pandas.
# 2. Clean the data: Handle missing values, remove duplicates, and fix column names if needed.
# 3. Understand the data: Use pandas functions to explore.
# 4. Identify questions to answer: What insights do we want?
# 5. Visualize the data: Use matplotlib to draw charts to answer these questions visually.
# 6. Save the plots.

# ----------------------------------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"C:\Users\lalkesh yaduvanshi\Documents\netflix1.csv")

# Uncomment below to clean the data
df = df.dropna(subset=["type", "release_year", "rating", "country", "duration"])

# 1. Bar chart: Number of Movies vs TV Shows
type_count = df["type"].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(type_count.index, type_count.values, color=['skyblue', 'orange'])
plt.title("Number of Movies and TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("movies_vs_tv.jpg")
plt.show()

# 2. Pie chart: Content Rating Distribution
rating_counts = df["rating"].value_counts()
plt.figure(figsize=(12, 10))
plt.pie(rating_counts, labels=rating_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Percentage of Content Ratings")
plt.tight_layout()
plt.savefig("content_rating.png")
plt.show()

# 3. Histogram: Movie Duration Distribution
movie_df = df[df["type"] == "Movie"].copy()
movie_df = movie_df[movie_df["duration"].str.contains("min", na=False)]
movie_df["duration_int"] = movie_df["duration"].str.replace("min", "").str.strip().astype(int)

plt.figure(figsize=(8, 6))
plt.hist(movie_df["duration_int"], bins=30, color="purple", edgecolor="black")
plt.title("Distribution of Movie Duration")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig("movie_duration_histogram.jpg")
plt.show()

# 4. Scatter Plot: Release Year vs Number of Shows
release_count = df["release_year"].value_counts().sort_index()
plt.figure(figsize=(11, 8))
plt.scatter(release_count.index, release_count.values, color="red")
plt.title("Release Year vs Number of Shows")
plt.xlabel("Release Year")
plt.ylabel("Number of Shows")
plt.tight_layout()
plt.savefig("release_year_plot.jpg")
plt.show()

# 5. Horizontal Bar Chart: Top 10 Countries by Number of Shows
country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(8, 6))
plt.barh(country_counts.index, country_counts.values, color="teal")
plt.title("Top 10 Countries by Number of Shows")
plt.ylabel("Country")
plt.xlabel("Number of Shows")
plt.tight_layout()
plt.savefig("top_10_countries.png")
plt.show()

# 6. Line Charts: Movies vs TV Shows Released Over the Years
content_by_year = df.groupby(["release_year", "type"]).size().unstack().fillna(0)
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Line chart for Movies
ax[0].plot(content_by_year.index, content_by_year["Movie"], color="blue")
ax[0].set_title("Movies Released per Year")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number of Movies")

# Line chart for TV Shows
ax[1].plot(content_by_year.index, content_by_year["TV Show"], color="orange")
ax[1].set_title("TV Shows Released per Year")
ax[1].set_xlabel("Year")
ax[1].set_ylabel("Number of TV Shows")

fig.suptitle("Comparison of Movies and TV Shows Released Over the Years")
plt.tight_layout()
plt.savefig("movies_tv_shows_comparison.png")
plt.show()