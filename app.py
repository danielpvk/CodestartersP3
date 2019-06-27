import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@localhost:3306/vida_empresas"

db = SQLAlchemy(app)


# Create our database model
class vida(db.Model):
    __tablename__ = 'vida'

    Index = db.Column(db.Integer, primary_key=True)
    Entidad = db.Column(db.String)
    Sector = db.Column(db.String)
    Edad = db.Column(db.Integer)
    Sobrevivientes = db.Column(db.Integer)
    Probabilidad_Supervivencia = db.Column(db.Float)
    Probabilidad_muerte = db.Column(db.Float)
    Muertes_antes_de = db.Column(db.Float)
    Esperanza_de_vida = db.Column(db.Float)


    def __repr__(self):
        return '<vida %r>' % (self.name)


# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()


@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")


@app.route("/Aguascalientes/Sobrevivientes")
def sobrevivientes():
    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = db.session.query(vida.Edad, vida.Sobrevivientes).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_sobrevivientes = []
    for Edad, Sobrevivientes in results:
        passenger_dict = {}
        passenger_dict["Edad"] = Edad
        passenger_dict["Sobrevivientes"] = Sobrevivientes
        all_sobrevivientes.append(passenger_dict)

    return jsonify(all_sobrevivientes)



if __name__ == '__main__':
    app.run(debug=True)
