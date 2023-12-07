from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # Use SQLite for simplicity
db = SQLAlchemy(app)

class ExcelForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), nullable=False)

@app.route('/')
def index():
    data = ExcelForm.query.all()
    return render_template('index.html', data=data)

@app.route('/save', methods=['POST'])
def save():
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']

    if not name or not age or not email:
        return "Error: All fields must be filled."

    new_data = ExcelForm(name=name, age=age, email=email)
    db.session.add(new_data)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/view_data')
def view_data():
    data = ExcelForm.query.all()
    return render_template('view_data.html', data=data)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables before running the app
    app.run(debug=True, host='0.0.0.0', port=5000)
