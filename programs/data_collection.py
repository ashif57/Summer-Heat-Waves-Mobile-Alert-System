import pandas as pd
import numpy as np

def generate_synthetic_data():
    np.random.seed(42)
    dates = pd.date_range(start='2023-06-01', end='2023-08-31', freq='H')
    temperatures = 30 + np.random.normal(loc=0, scale=3, size=len(dates))

    # Introduce synthetic heat wave patterns
    for i in range(5):
        start = np.random.randint(0, len(temperatures) - 48)
        temperatures[start:start + 48] += np.random.randint(5, 10)

    df = pd.DataFrame({'date': dates, 'temperature': temperatures})
    return df

# Generate and save the data
data = generate_synthetic_data()
data.to_csv('synthetic_weather_data.csv', index=False)

print("Synthetic data generated and saved to 'synthetic_weather_data.csv'")
