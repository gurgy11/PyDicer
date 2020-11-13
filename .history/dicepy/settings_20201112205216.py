import os

# Secret Key
SECRET_KEY = os.getenv('SECRET_KEY')

# Database Connection Credentials
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
