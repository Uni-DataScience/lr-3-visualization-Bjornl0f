import matplotlib.pyplot as plt
import numpy as np
import collections


def plot_distribution(data):
    """
    Plots the distribution of data using a bar chart.

    Parameters:
    data (array-like): An array of categorical data items.
    """
    fig, ax = plt.subplots()
    
    # Count the frequency of each category
    counter = collections.Counter(data)
    categories = list(counter.keys())
    frequencies = list(counter.values())
    
    # Create bar chart with distinct colors
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6']
    bars = ax.bar(categories, frequencies, color=colors[:len(categories)])
    
    # Add labels and title
    ax.set_xlabel('Category')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency Distribution of Categories')
    
    return fig


# Example data
data = np.random.choice(['A', 'B', 'C'], size=100)
plot_distribution(data)
