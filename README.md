# PROJECT1_House_Price_Prediction
# House Price Prediction Project

This project aims to predict house prices using various machine learning models, including neural networks.

## Project Structure
- `data/`: Contains training and test datasets.
- `notebooks/`: Jupyter notebooks for data analysis and model development.
- `models/`: Trained models saved in `.keras` format.
- `app.py`: Flask application for deploying the model to predict house prices.
- `requirements.txt`: Lists dependencies for running the project.
- `Procfile`: Required for Heroku deployment.

## Setup Instructions
1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Flask app:
    ```bash
    python app.py
    ```

## Model
The main model used for predictions is a neural network, trained on features such as lot size, number of rooms, neighborhood, etc.

## Deployment
The application can be deployed to Heroku using the provided `Procfile`.
