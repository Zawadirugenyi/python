# Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# -------------------------
# Task 1: Load and Explore Dataset
# -------------------------

try:
    # Load the Iris dataset from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame  # Convert to Pandas DataFrame

    print("✅ Dataset loaded successfully!\n")
    
    # Display first few rows
    print("First 5 rows of dataset:")
    print(df.head(), "\n")

    # Check dataset structure
    print("Dataset Info:")
    print(df.info(), "\n")

    # Check for missing values
    print("Missing values in each column:")
    print(df.isnull().sum(), "\n")

    # Cleaning: fill missing values (if any)
    df.fillna(df.mean(numeric_only=True), inplace=True)

except FileNotFoundError:
    print("❌ Error: Dataset file not found.")
except Exception as e:
    print("❌ An error occurred while loading dataset:", e)

# -------------------------
# Task 2: Basic Data Analysis
# -------------------------

print("Basic Statistics:")
print(df.describe(), "\n")

# Grouping by species and computing mean of numerical columns
species_mean = df.groupby("target").mean()
print("Mean values grouped by species:")
print(species_mean, "\n")

# Identifying patterns
print("Observation: Iris-setosa tends to have smaller sepal length & petal length compared to others.\n")

# -------------------------
# Task 3: Data Visualization
# -------------------------

sns.set(style="whitegrid")

# 1. Line Chart (Sepal length trend across dataset index)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length", color="blue")
plt.title("Line Chart: Sepal Length Trend")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart (Average petal length per species)
plt.figure(figsize=(8,5))
sns.barplot(x="target", y="petal length (cm)", data=df, palette="viridis", ci=None)
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species (0=setosa, 1=versicolor, 2=virginica)")
plt.ylabel("Avg Petal Length (cm)")
plt.show()

# 3. Histogram (Distribution of Sepal Width)
plt.figure(figsize=(8,5))
plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot (Sepal Length vs Petal Length)
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="target", data=df, palette="deep")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
