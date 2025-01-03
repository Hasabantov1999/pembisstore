from sqlalchemy import create_engine, inspect
from utils.dummy_db import DummyDB
from models.base_model import db
from models.user_model import User
from models.product_model import Product
from utils.config import Config

def init_db():
    """Veritabanını oluştur ve dummy data ekle."""
    from app import app  # Döngüsel importu önlemek için burada import ediyoruz
    with app.app_context():
        DummyDB.setup_database()

def reset_db():
    """Veritabanını sıfırla."""
    from app import app  # Döngüsel importu önlemek için burada import ediyoruz
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Veritabanı sıfırlandı.")

def add_dummy_data():
    """Dummy data ekle."""
    from app import app  # Döngüsel importu önlemek için burada import ediyoruz
    with app.app_context():
        DummyDB.add_all_dummy_data()

def list_tables():
    """Veritabanındaki tabloları listeler."""
    engine = create_engine(
        f"mysql+mysqlconnector://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"
    )
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    if tables:
        print("Veritabanındaki tablolar:")
        for table in tables:
            print(f"- {table}")
    else:
        print("Veritabanında hiç tablo bulunmuyor.")

def show_table_columns(table_name):
    """Belirtilen tablonun sütunlarını listeler."""
    engine = create_engine(
        f"mysql+mysqlconnector://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"
    )
    inspector = inspect(engine)
    columns = inspector.get_columns(table_name)

    if columns:
        print(f"'{table_name}' tablosunun sütunları:")
        for column in columns:
            print(f"- {column['name']} ({column['type']})")
    else:
        print(f"'{table_name}' tablosunda sütun bulunmuyor.")

def show_dummy_data():
    """Dummy verileri görüntüler."""
    from app import app
    with app.app_context():
        print("\nUsers Tablosundaki Veriler:")
        users = User.query.all()
        for user in users:
            print(f"- ID: {user.id}, Name: {user.name}, Email: {user.email}")

        print("\nProducts Tablosundaki Veriler:")
        products = Product.query.all()
        for product in products:
            print(f"- ID: {product.id}, Name: {product.name}, Price: {product.price}")

if __name__ == '__main__':
    from app import app  # Döngüsel importu önlemek için burada import ediyoruz
    with app.app_context():
        print("Komut Seçenekleri:")
        print("1. Veritabanını oluştur ve dummy data ekle")
        print("2. Veritabanını sıfırla")
        print("3. Dummy data ekle")
        print("4. Veritabanındaki tabloları listele")
        print("5. Bir tablonun sütunlarını listele")
        print("6. Dummy verileri göster")  # Yeni seçenek

        choice = input("Seçiminizi yapın (1/2/3/4/5/6): ")
        if choice == '1':
            init_db()  # Veritabanını oluştur ve dummy data ekle
        elif choice == '2':
            reset_db()  # Veritabanını sıfırla
        elif choice == '3':
            add_dummy_data()  # Dummy data ekle
        elif choice == '4':
            list_tables()  # Tabloları listele
        elif choice == '5':
            table_name = input("Tablo adını girin: ")
            show_table_columns(table_name)  # Belirtilen tablonun sütunlarını listele
        elif choice == '6':
            show_dummy_data()  # Dummy verileri göster
        else:
            print("Geçersiz seçim!")