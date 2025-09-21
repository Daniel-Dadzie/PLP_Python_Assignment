Analyzing the Iris Dataset with Pandas and Visualizing Results with Matplotlib
📌 Description & Objective

The objective of this assignment is to:

Load and analyze the Iris dataset using the pandas library in Python.

Perform basic data exploration and statistical analysis.

Create simple plots and charts with matplotlib (and seaborn for styling) to visualize results.

The Iris dataset is a classic dataset widely used in machine learning and statistics. It contains 150 samples of iris flowers with four numerical features (sepal length, sepal width, petal length, petal width) and a categorical target (species: setosa, versicolor, virginica).

📂 Tasks
Task 1: Load and Explore the Dataset

The dataset was loaded using sklearn.datasets.load_iris() and converted into a pandas DataFrame.

Displayed the first few rows with .head().

Explored dataset structure (data types, shape, missing values).

Verified that the dataset contains no missing values.

Task 2: Basic Data Analysis

Computed descriptive statistics (.describe()) for all numerical columns.

Grouped the dataset by species and calculated the mean for each feature.

Observed patterns such as:

Setosa flowers generally have smaller petal lengths and widths.

Virginica flowers typically have the largest petals.

Versicolor values fall in between the two.

Task 3: Data Visualization

Created at least four different plots using matplotlib and seaborn:

Line Chart – Showed feature values across samples to observe trends.

Bar Chart – Compared average petal length per species.

Histogram – Displayed the distribution of sepal length.

Scatter Plot – Visualized the relationship between sepal length and petal length.

Each visualization includes titles, axis labels, and legends for clarity.

📊 Dataset Details

Name: Iris Dataset

Source: sklearn.datasets.load_iris()

Features:

Sepal Length (cm)

Sepal Width (cm)

Petal Length (cm)

Petal Width (cm)

Target (Species):

Iris-setosa

Iris-versicolor

Iris-virginica

🛠️ Technologies Used

Python 3.x

pandas

matplotlib

seaborn

scikit-learn
 (for loading dataset)

⚡ Error Handling

Implemented exception handling for:

Dataset loading.

Handling missing or invalid values (not applicable here since the Iris dataset is clean).

📑 Submission Requirements

The submission includes:

A Jupyter Notebook (.ipynb) or Python Script (.py) with:

Data loading and exploration.

Descriptive statistics and group analysis.

At least four visualizations with proper labels and titles.

Observations noted after analysis.

🚀 How to Run the Code

Clone/download this repository.

Install dependencies (if not already installed):

pip install pandas matplotlib seaborn scikit-learn


Run the Jupyter notebook:

jupyter notebook iris_analysis.ipynb


OR run the Python script:

python iris_analysis.py

✨ Findings/Observations

Setosa flowers have the smallest petals and largest sepal width.

Virginica flowers have the largest petals overall.

Versicolor features are intermediate, making it harder to distinguish from Virginica than Setosa.

Scatter plots clearly show separability between Setosa and the other two species, but overlap exists between Versicolor and Virginica.