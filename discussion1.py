import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# KDE plot for petal length
plt.figure(figsize=(8,6))
sns.kdeplot(data=df, x='petal length (cm)', hue='species', fill=True, common_norm=False, alpha=0.5)
plt.title('Kernel Density Estimation of Petal Length by Species')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Density')
plt.show()