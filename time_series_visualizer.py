import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df=df.set_index('date')
# Clean data
df = df[(df['value'].quantile(0.975)>df['value'])&(df['value']>df['value'].quantile(0.025))]


def draw_line_plot():
    # Draw line plot
    dfs = df.sort_index()
    fig, ax= plt.subplots(figsize=(10,4))
    line, = ax.plot(df['value'])
    line.set_linewidth(1)
    line.set_linestyle('-')
    line.set_color('red')
    plt.xticks(dfs.index[::240])
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views ')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
   df_bar = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'])
    df_bar.set_index('date', inplace=True)
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    df_bar['month_num'] = df_bar.index.month
    
    df_bar=df_bar.groupby(['year','month','month_num'])['value'].mean().reset_index()
    df_bar=df_bar.sort_values("month_num",ascending=True)
    print(df_bar)

    # Draw bar plot
    fig, ax= plt.subplots(figsize=(10,10))
    ax=sns.barplot(df_bar,x='year',y='value',hue='month')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df=pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'])
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    df_box=df_box.sort_values("month",ascending=True)
    print(df_box)
    # Draw box plots (using Seaborn)
    fig, axes=plt.subplots(1,2,sharex=True,figsize=(10,6))
    sns.boxplot(data=df_box,x='year',y='value',ax=axes[0])

    axes[0].set_title('Year-wise Box Plot (Trend)')
    
    axes[0].set_xticks(['2016','2017','2018','2019'])
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    sns.boxplot(data=df_box,x='month',y='value',ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    
    
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_xticks(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
