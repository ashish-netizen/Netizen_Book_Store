#app/catalog/__init.py__

from flask import Blueprint

main= Blueprint('main', __name__ , template_folder= 'templates')

from app.catalog import routes, models