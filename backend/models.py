from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image_filename = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Recipe {self.name}>'
