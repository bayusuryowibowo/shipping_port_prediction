# Shipping Port Prediction

This repository contains a machine learning model and a Django backend for predicting shipping port ETA (Estimated Time of Arrival). 

## Disclaimer

The machine learning model in this project was developed by [AldityaPras](https://github.com/AldityaPras). The Django backend was created by [bayusuryowibowo](https://github.com/bayusuryowibowo).

## Project Structure

- `machine_learning/`: Contains the Flask application for training and predicting with the machine learning model.
- `app/`: Contains the Django application for interacting with the machine learning model.

## Setup Instructions

### Prerequisites

- Python 3.12 or later
- Django
- Flask
- Required Python packages (listed in `requirements.txt`)

### 1. Install Dependencies

#### For Flask (Machine Learning)

Navigate to the `machine_learning/` directory and install the required packages:

```bash
cd machine_learning
pip install -r requirements.txt
```

#### For Django (Backend)

Navigate to the `app/` directory and install the required packages:

```bash
cd app
pip install -r requirements.txt
```

### 2. Configure Django

#### Migrate Database

Ensure you have PostgreSQL installed and running. Update the DATABASES settings in app/settings.py to match your PostgreSQL setup.

Run the following commands to apply migrations and set up the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Run Flask Application

Navigate to the `machine_learning/` directory and start the Flask server:

```bash
cd machine_learning
python machine_learning.py
```

### 4. Run Django Application

Navigate to the root directory and start the Django server:

```bash
python manage.py runserver
```


## Usage

#### Training the Model

To train the model, send a POST request to the /train endpoint of the Flask server. You can use curl or any HTTP client to do this.

Example curl command:
```bash
curl -X POST http://localhost:8000/train
```

#### Making Predictions

Once the model is trained, you can use the Django backend to make predictions. Send a POST request to the /predict endpoint of the Django server with the data you want to predict.

Example curl commands:
```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"product_type": "Cosmetics", "origin": "Kolkata", "inspection_results": "Pending", "routes": "Route B", "defect_rates": 1.907665734}'
```
```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"product_type": "Haircare", "origin": "Delhi", "inspection_results": "Fail", "routes": "Route C", "defect_rates": 0.500123456}'
```
```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"product_type": "Skincare", "origin": "Mumbai", "inspection_results": "Pass", "routes": "Route A", "defect_rates": 1.23456789}'
```

## Notes

- Ensure that both Flask and Django applications are running simultaneously for the backend to function correctly.
- Adjust the ports and paths if they differ from the defaults.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
Feel free to customize this README according to your preferences and project specifics.