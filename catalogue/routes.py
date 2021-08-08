from catalogue import app, ALLOWED_EXTENSIONS
import os
from flask import render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename
from catalogue.models import Products
from catalogue.load_database import upload_db

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Pendiente de revisar Flash messages, rutas en produccion
@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
    # check if the post request has the file part
        if 'file' not in request.files:
            #flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            #flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            upload_db(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect("/")
    products = Products.query.all()
    return render_template("home.html", products=products)
