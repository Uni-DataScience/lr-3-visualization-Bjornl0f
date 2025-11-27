import numpy as np
import pandas as pd
import plotly.express as px


def create_interactive_plotly(df):
    """
    Creates an interactive scatter plot using Plotly.

    Parameters:
    df (DataFrame): A DataFrame containing 'x' and 'y' columns.
    """
    fig = px.scatter(
        df, 
        x='x', 
        y='y',
        title='Interactive Scatter Plot',
        labels={'x': 'X Variable', 'y': 'Y Variable'}
    )
    
    # Update layout for better appearance
    fig.update_layout(
        xaxis_title='X Variable',
        yaxis_title='Y Variable',
        showlegend=True
    )
    
    return fig


# Example data
df = pd.DataFrame({'x': np.random.rand(50), 'y': np.random.rand(50)})
create_interactive_plotly(df)
