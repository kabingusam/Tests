from Flask_images import app
from Flask_images.models import db
from Flask_images.routes import *

with app.app_context():
    db.create_all()

if __name__ == "main":
    app.run(debug=True)