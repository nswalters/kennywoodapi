# Kennywood Scheduling API

## Setup

1. Clone this repository and change to the directory in the terminal.
1. Run `pipenv shell`
1. Run `pipenv install`
1. Run the migrations and seed the database with: `./seed_data.sh`

Now that the database is setup, you can run the following command to start the server:

```sh
python manage.py runserver
```

This will start a server running on `localhost:8000`.

## Kennywood ERD

Open the [Kennywood database diagram](https://dbdiagram.io/d/602b19f280d742080a3aa23f) to view the tables and relationships for the database.