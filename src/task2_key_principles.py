import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


def create_scatter_plot(data):
    """
    Creates a scatter plot using Seaborn.

    Parameters:
    data (DataFrame): A DataFrame containing 'x' and 'y' columns.
    """
    fig, ax = plt.subplots()
    
    # Create scatter plot using Seaborn
    sns.scatterplot(data=data, x='x', y='y', ax=ax)
    
    # Add gridlines for clarity
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Add axis labels and title
    ax.set_xlabel('X Variable')
    ax.set_ylabel('Y Variable')
    ax.set_title('Scatter Plot: Relationship Between X and Y')
    
    return fig


# Example data
data = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50)
})
create_scatter_plot(data)
