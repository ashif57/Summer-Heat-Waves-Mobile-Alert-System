# Summer Heat Waves Mobile Alert System

This project aims to develop a mobile alert system for detecting and warning against summer heatwaves. The system uses a machine learning model trained on temperature, day of the year, and hour of the day to predict heatwave conditions, providing timely alerts to help mitigate the risks associated with extreme heat.

## Heatwave Detection using Flask API

This project implements a heatwave detection system using Python and Flask. It processes input data to predict the likelihood of a heatwave, making it useful for real-time weather alert systems or public safety applications.

## Features

- Predicts the occurrence of heatwaves based on input parameters like temperature, day of the year, and hour of the day.
- Provides a simple API for integration with other systems or mobile applications.
- Returns predictions in real-time for immediate alert generation.
- Easily extensible to include additional weather features or enhanced prediction models.

## Requirements

- Python 3.8.10
- Flask
- Scikit-learn
- NumPy
- Pandas

## Adjusting Parameters

- **Temperature Sensitivity**: You can modify the threshold values in the model to adjust the sensitivity of the heatwave prediction.
- **Model Retraining**: Update the training data and retrain the model if you want to include additional features or improve accuracy.

## Code Structure

- **app.py**: The main script that runs the Flask API and handles incoming prediction requests.
- **model.pkl**: A serialized machine learning model trained to predict heatwaves.
- **requirements.txt**: Lists the dependencies required to run the project.
- **README.md**: Documentation for the project.

### Explanation of Key Functions:

- **predict()**: Handles the POST request, extracts the input data, and uses the machine learning model to predict whether a heatwave will occur.
- **load_model()**: Loads the pre-trained model from the serialized `.pkl` file.
- **prepare_input(data)**: Processes the input data to ensure it is in the correct format for the model.

## Usage

1. **Run the Flask API**:
    ```bash
    python app.py
    ```

2. **Make a Prediction Request**:
    ```bash
    curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"temperature\": 40, \"day_of_year\": 200, \"hour_of_day\": 14}"
    ```

3. **Response**:
    - The API will return a JSON response indicating whether a heatwave is predicted.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
