from flask import Flask
from utils.config import Config
from models.base_model import db
from routes import api
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
 app.run(debug=Config.is_dev())