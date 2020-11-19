from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/udacity' # connect to db. dialect://username:password@location:port/dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'persons' #sets name of table manually. Otherwise it is lowercase version of class
    id = db.Column(db.Integer, primary_key=True) #sets column 1 with constraints. This sets it as integer and primary key
    name = db.Column(db.String(), nullable=False) #column 2. String, and must have value
    
    def __repr__(self):
        return f'<PERSON ID: {self.id}, name: {self.name}>' #look more up about this. I'ts for debugging
    
db.create_all() #commits and creates

@app.route('/')
def index():
    person = Person.query.first() #sets variable by looking in db for the first person
    return 'Hello ' + person.name #calls variable and column. This oculd also be id

if __name__ == '__main__': #runs if you're doing it via python, so you can just python flask_hello_app.py
  app.run()