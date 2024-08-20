import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def exploratory_analysis(file_path):
    df = pd.read_csv(file_path)

    # Plot temperature over time
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='date', y='temperature')
    plt.title('Temperature Over Time')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.show()

    # Plot temperature distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(df['temperature'], bins=30, kde=True)
    plt.title('Temperature Distribution')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Frequency')
    plt.show()

# Perform exploratory analysis
exploratory_analysis('preprocessed_weather_data.csv')
