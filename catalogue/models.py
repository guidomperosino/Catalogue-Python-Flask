from flask_sqlalchemy import SQLAlchemy
from catalogue import db

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(40), unique=True, nullable=False)
    category_desc = db.Column(db.String(80))
    products = db.relationship("Products", backref="categories", lazy=True)
    #parent_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    #children = db.relationship("Categories")
    
    def __repr__(self):
        return self.category_name

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(40), nullable=False)
    brand = db.Column(db.String(20), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    #category = db.relationship("Categories")
    variants = db.relationship("Variants", backref="products", lazy=True)
    #image = db.Column(db.String(20), nullable=False, default="default_product.jpg")

    def __repr__(self):
        return self.item + " " + self.brand

class Variants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    variant = db.Column(db.String(20), unique=False, nullable=False)
    price = db.Column(db.Float, nullable=False)
    available = db.Column(db.Boolean, nullable=False, default=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    #product = db.relationship("Products")

    def __repr__(self):
        return self.variant + " " + str(self.price)