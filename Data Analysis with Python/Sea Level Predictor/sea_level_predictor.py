import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])



    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    res = linregress(x, y)
    x_pred = pd.Series([i for i in range(1880, 2051)])


    # Create second line of best fit
    res2 = linregress(x[x >= 2000], y[x >= 2000])
    x_pred2 = pd.Series([i for i in range(2000, 2051)])


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.plot(x_pred, res.intercept + res.slope*x_pred, 'r', label='fitted line 1')
    plt.plot(x_pred2, res2.intercept + res2.slope*x_pred2, 'g', label='fitted line 2')
    plt.legend(['fitted line 1', 'fitted line 2'])

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()