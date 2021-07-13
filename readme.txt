prereqs:
    - XAMPP

setup:
    1. install and activate pipenv
    2. install pipenv packages via "pipenv install"
    4. open XAMPP and start apache and mysql
    5. open mysql admin
    6. setup .env environment variables
        - ask for the vars
        - in the SQLALCHEMY_DATABASE_URI, replace username, pw, and db name with your own mysql configs
    7. import mysql data
    8. execute "run.py" in pipenv

