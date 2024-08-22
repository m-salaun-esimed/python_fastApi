#CREATE DATABASE mydatabase;
#CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';
#GRANT ALL PRIVILEGES ON mydatabase.* TO 'myuser'@'localhost';
#FLUSH PRIVILEGES;


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Remplacez par vos informations de connexion
DATABASE_URL = "mariadb+mariadbconnector://myuser:mypassword@localhost/mydatabase"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()