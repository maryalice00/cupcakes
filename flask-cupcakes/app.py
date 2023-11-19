"""Flask app for Cupcakes"""

# app.py
from flask import Flask, jsonify, request, render_template
from models import db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cupcakes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

# Routes for Cupcakes
@app.route('/api/cupcakes', methods=['GET'])
def get_all_cupcakes():
    cupcakes = Cupcake.query.all()
    cupcakes_data = [{'id': c.id, 'flavor': c.flavor, 'size': c.size, 'rating': c.rating, 'image': c.image} for c in cupcakes]
    return jsonify(cupcakes=cupcakes_data)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['GET'])
def get_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake_data = {'id': cupcake.id, 'flavor': cupcake.flavor, 'size': cupcake.size, 'rating': cupcake.rating, 'image': cupcake.image}
    return jsonify(cupcake=cupcake_data)

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    data = request.json
    new_cupcake = Cupcake(flavor=data['flavor'], size=data['size'], rating=data['rating'], image=data.get('image', 'https://tinyurl.com/demo-cupcake'))
    db.session.add(new_cupcake)
    db.session.commit()
    return jsonify(cupcake={'id': new_cupcake.id, 'flavor': new_cupcake.flavor, 'size': new_cupcake.size, 'rating': new_cupcake.rating, 'image': new_cupcake.image})

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    data = request.json

    cupcake.flavor = data['flavor']
    cupcake.size = data['size']
    cupcake.rating = data['rating']
    cupcake.image = data.get('image', cupcake.image)

    db.session.commit()

    updated_cupcake = {'id': cupcake.id, 'flavor': cupcake.flavor, 'size': cupcake.size, 'rating': cupcake.rating, 'image': cupcake.image}
    return jsonify(cupcake=updated_cupcake)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")

# Frontend Route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
