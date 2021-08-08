import csv
from catalogue.models import Products
from catalogue import db

def upload_db(f):
    products= []
    
    #Read products from uploaded file
    with open(f, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            products.append(Products(item = row['item'], brand = row['brand']))
    #Clear db table products
    db.session.query(Products).delete()
    db.session.commit()

    #Load new products on db products
    for product in products:
        db.session.add(product)
    db.session.commit()
    
    return