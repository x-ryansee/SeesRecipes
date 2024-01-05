from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    imageUrl = db.Column(db.String(255))
    mealTypes = db.Column(db.String(255))  # A string to store meal types, separated by commas
    diets = db.Column(db.String(255))      # A string to store diets, separated by commas
    cuisine = db.Column(db.String(100))    # A string to store a single cuisine

    def __repr__(self):
        return f'<Recipe {self.title}>'

