import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax = plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create line of best fit
    x2 = np.arange(df["Year"].min(), 2050, 1)
    bestFit = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    ax = plt.plot(x2, bestFit.intercept + bestFit.slope*x2)

    # Add labels and title
    ax = plt.gca()
    ax.set(xlabel = "Year", ylabel = "Sea Level (inches)", title = "Rise in Sea Level")
    # Save plot and return data for testing (DO NOT MODIFY)
        #Tests must be run on a legacy version of pandas, this seems well known according to the community forum.
    plt.savefig('sea_level_plot.png')
    return plt.gca()
