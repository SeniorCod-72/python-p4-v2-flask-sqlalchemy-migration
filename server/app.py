from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Configure flag to disable modification tracking and use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Initialize the Migrate object to manage schema migrations
migrate = Migrate(app, db)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
