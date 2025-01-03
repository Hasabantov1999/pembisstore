from models.user_model import User
from models.product_model import Product
from models.base_model import db
from utils.config import Config  # Config sınıfı .env dosyasını kullanıyor
from sqlalchemy import create_engine, text

class DummyDB:
    @staticmethod
    def create_database():
        """Veritabanını oluşturur."""
        db_name = Config.DB_NAME
        engine = create_engine(
            f"mysql+mysqlconnector://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}"
        )

        with engine.connect() as conn:
            # SQL sorgusunu text() ile sarmalayın
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
            print(f"'{db_name}' veritabanı oluşturuldu veya zaten mevcut.")

    @staticmethod
    def add_all_dummy_data():
        """Dummy data eklemek için metod."""
        User.add_dummy_data()
        Product.add_dummy_data()
        print("Dummy data eklendi.")

    @staticmethod
    def setup_database():
        """Veritabanını sıfırla ve dummy data ekle."""
        DummyDB.create_database()  # Veritabanını oluştur
        print("Dev ortamı: Veritabanı sıfırlanıyor...")
        db.drop_all()  # Tüm tabloları sil
        db.create_all()  # Tabloları yeniden oluştur
        DummyDB.add_all_dummy_data()  # Dummy data ekle