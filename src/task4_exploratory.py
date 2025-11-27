import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def perform_eda(df):
    """
    Performs EDA including descriptive statistics, outlier detection,
    and correlation analysis.

    Parameters:
    df (DataFrame): A DataFrame containing data for EDA.
    """
    # 1. Descriptive Statistics
    print("=" * 50)
    print("DESCRIPTIVE STATISTICS")
    print("=" * 50)
    desc_stats = df.describe()
    print(desc_stats)
    print()
    
    # 2. Outlier Detection using Box Plots
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    df.boxplot(ax=ax1)
    ax1.set_title('Box Plot for Outlier Detection')
    ax1.set_ylabel('Values')
    
    # 3. Correlation Analysis with Heatmap
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', 
                center=0, ax=ax2, fmt='.2f')
    ax2.set_title('Correlation Matrix Heatmap')
    
    print("=" * 50)
    print("CORRELATION MATRIX")
    print("=" * 50)
    print(correlation_matrix)
    print()
    
    print("=" * 50)
    print("EDA FINDINGS")
    print("=" * 50)
    print("1. Descriptive statistics show the central tendency and spread of each variable.")
    print("2. Box plots help identify potential outliers in the dataset.")
    print("3. The correlation heatmap reveals relationships between variables.")
    
    return fig1, fig2


# Example data
df = pd.DataFrame({
    'A': np.random.rand(50),
    'B': np.random.rand(50) * 10,
    'C': np.random.rand(50) * 100
})
perform_eda(df)
