import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
BMI = (df['weight'] / (df['height']/100)**2)

def change(i):
    if i > 25:
        return 1
    else:
        return 0

df['overweight'] = BMI.apply(change)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
normalized_change = {1:0, 2:1, 3:1}

df['cholesterol'] = df['cholesterol'].map(normalized_change)

df['gluc'] = df['gluc'].map(normalized_change)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = 'cardio', value_vars = (['cholesterol', 'gluc', 'alco', 'active', 'smoke', 'overweight']))


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.DataFrame(df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total'))
    

    # Draw the catplot with 'sns.catplot()'
    sns.catplot(data=df_cat, x="variable", y="total", hue="value", col="cardio", kind="bar", order=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"])

    # Get the figure for the output
    fig = sns.catplot(data=df_cat, x="variable", y="total", hue="value", col="cardio", kind="bar", order=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"]).fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[ 
        (df['ap_lo'] <= df['ap_hi'] ) & 
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) & 
        (df['weight'] >= df['weight'].quantile(0.025)) & 
        (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True



    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, mask=mask, vmax=0.32, vmin = -0.16, square=True, fmt="0.1f", annot=True)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig