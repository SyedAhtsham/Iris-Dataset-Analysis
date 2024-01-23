import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# write a function that loads the iris dataset and plots a scatter plot of sepal length vs sepal width, iris dataset from sklearn libaray
def load_and_plot():
    # Load the Iris dataset from scikit-learn
    iris = load_iris()
    print("Shape of the data: ", iris.data.shape)
    print("Yes")

    # Create a DataFrame from the iris data
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target

    # Scatter plot of sepal_length vs sepal_width
    plt.scatter(df["sepal length (cm)"], df["sepal width (cm)"], c=df['target'], cmap='viridis', edgecolors='k')
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")
    plt.title("Iris Dataset: Sepal Length vs Sepal Width")
    print("Save the plot as a png file")
    plt.savefig("Iris_dataset.png")

    plt.show()

#call the above function
load_and_plot()