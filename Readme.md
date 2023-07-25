# Flask and MySQL Car Management App

This is a simple web application built with Flask (Python web framework) and MySQL to manage car records. The app allows you to add new cars, view the existing cars, update car information, and assign unique plate numbers to each car.

## Setup and Installation

1. **Clone the Repository**

```bash
git clone https://github.com/ShayCohenn/flask_mysql_example.git
```
```bash
cd flask_mysql_example
```
## Install Dependencies
### Make sure you have Python installed. Create a virtual environment and install the required packages:
```bash
python -m virtualenv env
```
```
env/script/activate
```
```
pip install -r requirements.txt
```
    
## Configure the MySQL Database
### Install and set up MySQL on your machine if you haven't already.
### Create a new database named cars.

### Edit the Flask app (app.py) to set your MySQL credentials in the db connection:
```python
    db = mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password",
        database="cars"
    )
```
## Run the App
Start the Flask development server:
```bash
python app.py
```

# Endpoints
The following endpoints are available in the app:

## GET /cars: Fetch all car records from the database.
## POST /cars/add: Add a new car to the database. Provide JSON data with attributes: make, model, year, and color.
## PATCH /cars/update/<int:id>: Update attributes of a specific car (identified by id). Provide JSON data with the attributes you want to change (e.g., {"model": "Camry", "color": "Black"}).

# Contributing
## Contributions are welcome! If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request.