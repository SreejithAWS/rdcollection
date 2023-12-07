# app.py
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

class ExcelForm:
    def __init__(self):
        self.df = pd.DataFrame(columns=["Name", "Age", "Email"])

    def save_data(self, name, age, email):
        if not name or not age or not email:
            return False

        new_data = {"Name": name, "Age": age, "Email": email}
        self.df = self.df.append(new_data, ignore_index=True)
        self.df.to_excel("data.xlsx", index=False)
        return True

    def get_data(self):
        return self.df

excel_form = ExcelForm()

@app.route('/')
def index():
    return render_template('index.html', data=excel_form.get_data())

@app.route('/save', methods=['POST'])
def save():
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']

    if excel_form.save_data(name, age, email):
        return redirect(url_for('index'))
    else:
        return "Error: All fields must be filled."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

