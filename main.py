from flask import Flask
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint
import db


api = Api()
app = Flask(__name__)
api.init_app(app)

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db.DB_USER}:{db.DB_PASSWORD}@{db.DB_HOST}:5432/{db.DB_NAME}"
CORS(app)

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

@api.route('/hai')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)