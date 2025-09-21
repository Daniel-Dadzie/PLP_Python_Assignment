 

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

 

try:
    # Load the iris dataset from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame  # Convert to pandas DataFrame
    
    print("✅ Dataset loaded successfully!\n")
except Exception as e:
    print("❌ Error loading dataset:", e)

# Display first few rows
print("First 5 rows of dataset:")
print(df.head(), "\n")

# Check structure: data types and missing values
print("Dataset info:")
print(df.info(), "\n")

print("Missing values per column:")
print(df.isnull().sum(), "\n")

# (No missing values in iris, but here's how you would handle them)
df = df.dropna()
 

# Descriptive statistics
print("Descriptive statistics:")
print(df.describe(), "\n")

# Group by species and compute mean
grouped = df.groupby("target").mean()
print("Mean values grouped by species (target):")
print(grouped, "\n")

# Rename target column values for clarity
df["species"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

# Interesting finding (example)
print("Observation: Virginica tends to have the longest petals and sepals.\n")

 

# Set seaborn style for better visuals
sns.set(style="whitegrid")

# 1. Line chart (simulate a trend by plotting sepal length across samples)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.title("Line Chart - Sepal Length Trend")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart (average petal length per species)
plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal length (cm)", data=df, estimator="mean")
plt.title("Bar Chart - Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal width)
plt.figure(figsize=(8,5))
plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram - Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (Sepal length vs Petal length)
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df)
plt.title("Scatter Plot - Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
 