from flask_sqlalchemy import SQLAlchemy
from catalogue import db


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(40), unique=True, nullable=False)
    brand = db.Column(db.String(20), unique=True, nullable=False)
    image = db.Column(db.String(20), nullable=False,
                      default="default_product.jpg")

    def __repr__(self):
        return self.item + " " + self.brand
