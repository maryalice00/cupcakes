"""Models for Cupcake app."""
# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cupcake(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String, nullable=False, default="https://tinyurl.com/demo-cupcake")
