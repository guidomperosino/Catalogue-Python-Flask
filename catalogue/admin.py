from catalogue import app, db
from catalogue.models import Categories, Products, Variants
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

#admin config
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

#views
class CategoriesView(ModelView):
    form_columns = ['category_name', 'category_desc']

class ProductsView(ModelView):
    form_columns = ['categories', 'brand', 'item']

class VariantsView(ModelView):
    form_columns = ['products', 'variant', 'price', 'available']

#admin views
admin = Admin(app, name='catalogo', template_mode='bootstrap3')
admin.add_view(CategoriesView(Categories, db.session))
admin.add_view(ProductsView(Products, db.session))
admin.add_view(VariantsView(Variants, db.session))