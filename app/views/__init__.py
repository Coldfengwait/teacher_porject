from app import app
from .index import index
app.register_blueprint(index, url_prefix='/index')