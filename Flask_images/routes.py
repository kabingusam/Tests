from Flask_images import app, db

@app.route('/image')
def image_db():
    image = image.query.filter_by(path="/home/kabingu/Pictures/office.jpg").first()
