# Let's Learn WebGL
An interactive tutorial website for learning WebGL.
# Deploy
1. Setup the environment: `source env.example` (bash only)
2. Install dependencies: `pip install -r requirements.txt`
3. Setup the database
    1. Install postgres
    2. Create database:
    ```sql
    $ psql
    # create database tutorials_dev;
    CREATE DATABASE
    #\q
    ```
    3. Migrate database: `python manage.py db upgrade`
4. Run the server: `python manage.py runserver`
