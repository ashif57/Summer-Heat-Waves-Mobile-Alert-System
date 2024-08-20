import pandas as pd

def preprocess_data(file_path):
    df = pd.read_csv(file_path)

    # Handle missing values
    df = df.fillna(method='ffill')

    # Extract date features
    df['date'] = pd.to_datetime(df['date'])
    df['day_of_year'] = df['date'].dt.dayofyear
    df['hour_of_day'] = df['date'].dt.hour

    # Convert temperatures to Fahrenheit (if required)
    df['temperature_f'] = df['temperature'] * 9/5 + 32

    return df

# Preprocess the synthetic data
df_preprocessed = preprocess_data('synthetic_weather_data.csv')
df_preprocessed.to_csv('preprocessed_weather_data.csv', index=False)

print("Data preprocessed and saved to 'preprocessed_weather_data.csv'")
