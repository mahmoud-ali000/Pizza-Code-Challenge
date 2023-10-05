# Pizza-Code-Challenge

# Pizza Restaurant API
A Flask API for managing a Pizza Restaurant domain.

## Introduction

This Flask API is designed to manage a Pizza Restaurant domain. It allows you to create, read, update, and delete restaurants, pizzas, and their associations. Additionally, it enforces data validations to ensure data integrity

### Prerequisites

- Python 3
- Flask
- SQLAlchemy
- Flask-RESTful 
- Database (e.g., SQLite, PostgreSQL)


## Installation

1. Clone the repository

2. Create a virtual environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate

3. Install the required packages:
pip install -r requirements.txt

## Usage
Running the Server

To start the Flask server, run the following command:
python app.py

The server will start, and you can access the API at https://genevive-restaurant-pizza-api.onrender.com

## Testing Endpoints
Use a tool like Postman or curl to test the API endpoints. 

## Database Models
The API uses three main database models:

Restaurant: Represents a restaurant with a name and an address. Restaurants can offer multiple pizzas.

Pizza: Represents a type of pizza with a name and ingredients. Pizzas can be offered by multiple restaurants.

RestaurantPizza: Connects restaurants and pizzas and includes the price for each pizza at a specific restaurant.

## Validations
RestaurantPizza Model: Price validation enforces that the price is between 1 and 30.

Restaurant Model: Name validation ensures it's less than 50 characters in length and enforces uniqueness.
