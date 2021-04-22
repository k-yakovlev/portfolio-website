import datetime
import os

from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('APP_SECRET_KEY')

current_year = datetime.date.today().year


@app.route('/')
def home():
    return render_template('index.html', current_year=current_year)


if __name__ == '__main__':
    app.run(debug=True)
