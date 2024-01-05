from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, Recipe  # Importing db and Recipe from models.py
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Flask-Migrate with the app
db.init_app(app)
migrate = Migrate(app, db)

# Route to add a new recipe
@app.route('/recipes', methods=['POST'])
def add_recipe():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    imageUrl = data.get('imageUrl')

    recipe = Recipe(title=title, description=description, imageUrl=imageUrl)
    db.session.add(recipe)
    db.session.commit()

    return jsonify({
        'id': recipe.id,
        'title': recipe.title,
        'description': recipe.description,
        'imageUrl': recipe.imageUrl
    }), 201

# Route to get all recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    try:
        recipes = Recipe.query.all()
        recipes_data = [
            {
                'id': recipe.id,
                'title': recipe.title,
                'description': recipe.description,
                'imageUrl': recipe.imageUrl
            } for recipe in recipes
        ]
        return jsonify(recipes_data)
    except Exception as e:
        app.logger.error(f"Error fetching recipes: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
