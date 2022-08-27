from flask import Blueprint

ponencia = Blueprint('ponencia', __name__, template_folder='templates')

# Importar routes.py desde el modulo actual para registrar las rutas
from . import routes