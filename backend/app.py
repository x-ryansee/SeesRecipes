from flask import Flask, request, jsonify
from models import db, Recipe
from PIL import Image
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/recipes', methods=['POST'])
def add_recipe():
    data = request.form
    name = data.get('name')
    description = data.get('description')
    
    image = request.files.get('image')
    if image:
        image_filename = f'{name}_{image.filename}'
        image.save(os.path.join('images', image_filename))
    else:
        image_filename = None

    recipe = Recipe(name=name, description=description, image_filename=image_filename)
    db.session.add(recipe)
    db.session.commit()

    return jsonify({'message': 'Recipe added successfully!', 'id': recipe.id}), 201

@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    recipes_data = [{'id': recipe.id, 'name': recipe.name, 'description': recipe.description, 'image_filename': recipe.image_filename} for recipe in recipes]
    return jsonify(recipes_data)

if __name__ == '__main__':
    app.run(debug=True)
