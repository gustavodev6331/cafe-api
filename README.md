# Cafe API

A RESTful API that allows users to manage and discover cafes with useful information such as Wi-Fi availability, power sockets, seating capacity, coffee prices, and more.

This project was built to practice REST API development using Flask and SQLAlchemy.

## Home Page
<img width="1461" height="837" alt="Screenshot 2026-07-25 at 12 37 18 PM" src="https://github.com/user-attachments/assets/f4d58a3d-fda2-4712-9743-3a358ffcc050" />

## All Cafes

Displays every cafe currently stored in the database.

<img width="1467" height="843" alt="Screenshot 2026-07-25 at 12 37 29 PM" src="https://github.com/user-attachments/assets/d9a3356a-be7d-4038-96fa-79c150954a35" />

## Random Cafe

Returns a randomly selected cafe.

<img width="1470" height="841" alt="Screenshot 2026-07-25 at 12 38 04 PM" src="https://github.com/user-attachments/assets/89b23cc6-4179-4f8a-85ea-f196c96bf9ec" />

## API Documentation

View the complete Postman documentation [here](https://documenter.getpostman.com/view/55360170/2sBXwntXXm).

## Postman Page
<img width="1470" height="841" alt="Screenshot 2026-07-25 at 12 39 04 PM" src="https://github.com/user-attachments/assets/571e1aeb-d497-41b5-8899-73bf54438149" />
<img width="1464" height="833" alt="Screenshot 2026-07-25 at 12 39 34 PM" src="https://github.com/user-attachments/assets/990a9b66-afee-476a-a12e-0382e04802b7" />

## Features

- Add a new cafe
- Retrieve all cafes
- Get a random cafe
- Search cafes by location
- Update coffee prices
- Delete cafes (API key protected)

## Technologies

- Python
- Flask
- SQLAlchemy
- SQLite
- REST API
- Postman
- CRUD Operations
- HTTP methods (GET, POST, PATCH, DELETE)

## Installation

1. Clone the repository

```bash
git clone https://github.com/gustavodev6331/cafe-api.git
```
2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. Run the application

```bash
python main.py
```

4. Open your browser and visit:

```bash
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint             | Description              |
| ------ | -------------------- | ------------------------ |
| GET    | `/random`            | Returns a random cafe    |
| GET    | `/all`               | Returns all cafes        |
| GET    | `/search?loc=`       | Search cafes by location |
| POST   | `/add`               | Add a new cafe           |
| PATCH  | `/update_price/<id>` | Update coffee price      |
| DELETE | `/delete/<id>`       | Delete a cafe            |

## Response Example

```json
{
    "id": 1,
    "name": "Black Sheep",
    "location": "London",
    "has_wifi": true,
    "has_sockets": true,
    "coffee_price": "$3.50"
}
```

## Future Improvements

- Input validation
- JSON request bodies for POST and PATCH
- Environment variables for API keys
- Better error handling
