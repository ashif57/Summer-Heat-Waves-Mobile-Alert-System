from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
import pandas as pd
import joblib
def create_labels(df, temperature_threshold=35):
    """
    Create a 'heatwave' label based on a temperature threshold.
    :param df: DataFrame containing the weather data.
    :param temperature_threshold: Temperature above which a day is considered a heatwave.
    :return: DataFrame with an additional 'heatwave' column.
    """
    df['heatwave'] = df['temperature'] >= temperature_threshold
    return df

def optimize_model(file_path):
    df = pd.read_csv(file_path)
    
    # Create labels for heatwave prediction
    df = create_labels(df)
    
    # Prepare features and labels
    X = df[['temperature', 'day_of_year', 'hour_of_day']]
    y = df['heatwave']
    
    # Use SMOTE to balance the dataset
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X, y)
    
    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3, random_state=42)
    
    # Perform Grid Search for hyperparameter tuning
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [10, 20, None],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2],
    }
    grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5, scoring='f1')
    grid_search.fit(X_train, y_train)
    
    # Best model after optimization
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)
    report = classification_report(y_test, y_pred)
    print(report)
    
    return best_model

# Optimize the model
optimized_model = optimize_model('preprocessed_weather_data.csv')
joblib.dump(optimized_model, 'heatwave_model.pkl')
