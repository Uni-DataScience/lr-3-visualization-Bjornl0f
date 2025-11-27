import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_1d(data):
    """
    Creates a 1D line plot for a sequence of values.
    
    Parameters:
    data (array-like): A 1D array of values to plot.
    """
    fig, ax = plt.subplots()
    
    ax.plot(data)
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_title('1D Line Plot')
    
    return fig


def plot_2d(x, y):
    """
    Creates a 2D scatter plot to show the relationship between two variables.
    
    Parameters:
    x (array-like): X-axis values.
    y (array-like): Y-axis values.
    """
    fig, ax = plt.subplots()
    
    ax.scatter(x, y)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('2D Scatter Plot')
    
    return fig


def plot_3d(x, y, z):
    """
    Creates a 3D scatter plot to represent three-dimensional data points.
    
    Parameters:
    x (array-like): X-axis values.
    y (array-like): Y-axis values.
    z (array-like): Z-axis values.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(x, y, z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Scatter Plot')
    
    return fig


# Example data
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

plot_1d(x)
plot_2d(x, y)
plot_3d(x, y, z)
