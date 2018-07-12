# Seabattle
Simple sea battle API
## Getting started
Clone the project, create new virtual env for the project, after go to project directory and run 
```
pip install -r requirements.txt
```
Configure DB

.. code-block:: bash
```
$ sudo su - postgres
$ createdb seabattle
$ psql
$ CREATE USER seabattle;
$ ALTER USER seabattle PASSWORD 'root';
$ ALTER USER seabattle CREATEDB;
```

## Start game

Run 
```
python manage.py migrate
python manage.py runserver
```

Do POST request to ```http://127.0.0.1:8000/start-game/``` url and it will create new game, get id from response and you can start the game.
After do POST request to ```http://127.0.0.1:8000/game/shot/``` 
with ``` horizontal_cord, vertical_cord, game_id``` params and you will get response if you missed or not
