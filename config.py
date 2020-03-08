import os

user_db = os.environ['MYSQL_USERNAME']
password_db = os.environ['MYSQL_PASSWORD']

class DevConfiguration:
    # flask config
    DEBUG = True
    RESTPLUS_VALIDATE = True

    # sql_alchemy
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{user_db}:{password_db}@localhost:3306/viagens_flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfigurarion:
    #flask config
    RESTPLUS_VALIDATE = True

    # sql_alchemy
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{user_db}:{password_db}@localhost:3306/viagens_flask_test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


