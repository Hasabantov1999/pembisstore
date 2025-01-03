import os
from dotenv import load_dotenv

# .env dosyasını yükleme
load_dotenv()

class Config:
    APP_TYPE = os.getenv('APP_TYPE', 'Prod')  # Varsayılan olarak Prod
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')  # Varsayılan olarak boş bırakılır
    DB_NAME = os.getenv('DB_NAME')
    VERSION = os.getenv('VERSION')

    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @classmethod
    def is_dev(cls):
        return cls.APP_TYPE.lower() == 'dev'