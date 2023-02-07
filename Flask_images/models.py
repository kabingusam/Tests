from Flask_images import db

class image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(255), nullable=False)
    image = image(path="/home/kabingu/Pictures/office.jpg")
    db.session.add(image)
    db.session.commit()
