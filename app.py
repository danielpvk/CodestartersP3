import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# The database URI
#************************
# ***********************DATABASE LOCAL
#************************
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@localhost:3306/vida_empresas"

#************************
# ***********************DATABASE HEROKU
#************************
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@localhost:3306/vida_empresas"

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

def resultadoQuery (Estado,Sectores,Parametro):
    results = db.session.query(vida.Edad, Parametro).filter(vida.Entidad == Estado,vida.Sector == Sectores)

    # Create a dictionary from the row data and append to a list
    lista_resultado = []
    for Edad, Dato in results:
        lista_dict = {}
        lista_dict["Edad"] = Edad
        lista_dict[Sectores] = Dato
        lista_resultado.append(lista_dict)

    return lista_resultado

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

# AGUASCALIENTESW

@app.route("/Aguascalientes/Sobrevivientes/Total")
def AgsSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Aguascalientes","Total","vida.Sobrevivientes"))

@app.route("/Aguascalientes/Probabilidad_Supervivencia/Total")
def AgsProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Aguascalientes","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Aguascalientes/Probabilidad_muerte/Total")
def AgsProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Aguascalientes","Total","vida.Probabilidad_muerte"))

@app.route("/Aguascalientes/Muertes_antes_de/Total")
def AgsMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Aguascalientes","Total","vida.Muertes_antes_de"))

@app.route("/Aguascalientes/Esperanza_de_vida/Total")
def AgsEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Aguascalientes","Total","vida.Esperanza_de_vida"))

@app.route("/Aguascalientes/Sobrevivientes/Comercio")
def AgsSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Aguascalientes","Comercio","vida.Sobrevivientes"))

@app.route("/Aguascalientes/Probabilidad_Supervivencia/Comercio")
def AgsProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Aguascalientes","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Aguascalientes/Probabilidad_muerte/Comercio")
def AgsProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Aguascalientes","Comercio","vida.Probabilidad_muerte"))

@app.route("/Aguascalientes/Muertes_antes_de/Comercio")
def AgsMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Aguascalientes","Comercio","vida.Muertes_antes_de"))

@app.route("/Aguascalientes/Esperanza_de_vida/Comercio")
def AgsEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Aguascalientes","Comercio","vida.Esperanza_de_vida"))


@app.route("/Aguascalientes/Sobrevivientes/Manufacturas")
def AgsSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Aguascalientes","Manufacturas","vida.Sobrevivientes"))

@app.route("/Aguascalientes/Probabilidad_Supervivencia/Manufacturas")
def AgsProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Aguascalientes","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Aguascalientes/Probabilidad_muerte/Manufacturas")
def AgsProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Aguascalientes","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Aguascalientes/Muertes_antes_de/Manufacturas")
def AgsMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Aguascalientes","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Aguascalientes/Esperanza_de_vida/Manufacturas")
def AgsEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Aguascalientes","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Aguascalientes/Sobrevivientes/Servicios")
def AgsSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Aguascalientes","Servicios","vida.Sobrevivientes"))

@app.route("/Aguascalientes/Probabilidad_Supervivencia/Servicios")
def AgsProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Aguascalientes","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Aguascalientes/Probabilidad_muerte/Servicios")
def AgsProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Aguascalientes","Servicios","vida.Probabilidad_muerte"))

@app.route("/Aguascalientes/Muertes_antes_de/Servicios")
def AgsMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Aguascalientes","Servicios","vida.Muertes_antes_de"))

@app.route("/Aguascalientes/Esperanza_de_vida/Servicios")
def AgsEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Aguascalientes","Servicios","vida.Esperanza_de_vida"))


@app.route("/Aguascalientes/Sobrevivientes/Resto")
def AgsSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Aguascalientes","Resto","vida.Sobrevivientes"))

@app.route("/Aguascalientes/Probabilidad_Supervivencia/Resto")
def AgsProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Aguascalientes","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Aguascalientes/Probabilidad_muerte/Resto")
def AgsProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Aguascalientes","Resto","vida.Probabilidad_muerte"))

@app.route("/Aguascalientes/Muertes_antes_de/Resto")
def AgsMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Aguascalientes","Resto","vida.Muertes_antes_de"))

@app.route("/Aguascalientes/Esperanza_de_vida/Resto")
def AgsEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Aguascalientes","Resto","vida.Esperanza_de_vida"))


# BAJA CALIFORNIA

@app.route("/BajaCalifornia/Sobrevivientes/Total")
def BajSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("BajaCalifornia","Total","vida.Sobrevivientes"))

@app.route("/BajaCalifornia/Probabilidad_Supervivencia/Total")
def BajProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("BajaCalifornia","Total","vida.Probabilidad_Supervivencia"))

@app.route("/BajaCalifornia/Probabilidad_muerte/Total")
def BajProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("BajaCalifornia","Total","vida.Probabilidad_muerte"))

@app.route("/BajaCalifornia/Muertes_antes_de/Total")
def BajMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("BajaCalifornia","Total","vida.Muertes_antes_de"))

@app.route("/BajaCalifornia/Esperanza_de_vida/Total")
def BajEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("BajaCalifornia","Total","vida.Esperanza_de_vida"))

@app.route("/BajaCalifornia/Sobrevivientes/Comercio")
def BajSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("BajaCalifornia","Comercio","vida.Sobrevivientes"))

@app.route("/BajaCalifornia/Probabilidad_Supervivencia/Comercio")
def BajProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("BajaCalifornia","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/BajaCalifornia/Probabilidad_muerte/Comercio")
def BajProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("BajaCalifornia","Comercio","vida.Probabilidad_muerte"))

@app.route("/BajaCalifornia/Muertes_antes_de/Comercio")
def BajMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("BajaCalifornia","Comercio","vida.Muertes_antes_de"))

@app.route("/BajaCalifornia/Esperanza_de_vida/Comercio")
def BajEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("BajaCalifornia","Comercio","vida.Esperanza_de_vida"))


@app.route("/BajaCalifornia/Sobrevivientes/Manufacturas")
def BajSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("BajaCalifornia","Manufacturas","vida.Sobrevivientes"))

@app.route("/BajaCalifornia/Probabilidad_Supervivencia/Manufacturas")
def BajProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("BajaCalifornia","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/BajaCalifornia/Probabilidad_muerte/Manufacturas")
def BajProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("BajaCalifornia","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/BajaCalifornia/Muertes_antes_de/Manufacturas")
def BajMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("BajaCalifornia","Manufacturas","vida.Muertes_antes_de"))

@app.route("/BajaCalifornia/Esperanza_de_vida/Manufacturas")
def BajEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("BajaCalifornia","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/BajaCalifornia/Sobrevivientes/Servicios")
def BajSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("BajaCalifornia","Servicios","vida.Sobrevivientes"))

@app.route("/BajaCalifornia/Probabilidad_Supervivencia/Servicios")
def BajProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("BajaCalifornia","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/BajaCalifornia/Probabilidad_muerte/Servicios")
def BajProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("BajaCalifornia","Servicios","vida.Probabilidad_muerte"))

@app.route("/BajaCalifornia/Muertes_antes_de/Servicios")
def BajMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("BajaCalifornia","Servicios","vida.Muertes_antes_de"))

@app.route("/BajaCalifornia/Esperanza_de_vida/Servicios")
def BajEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("BajaCalifornia","Servicios","vida.Esperanza_de_vida"))


@app.route("/BajaCalifornia/Sobrevivientes/Resto")
def BajSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("BajaCalifornia","Resto","vida.Sobrevivientes"))

@app.route("/BajaCalifornia/Probabilidad_Supervivencia/Resto")
def BajProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("BajaCalifornia","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/BajaCalifornia/Probabilidad_muerte/Resto")
def BajProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("BajaCalifornia","Resto","vida.Probabilidad_muerte"))

@app.route("/BajaCalifornia/Muertes_antes_de/Resto")
def BajMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("BajaCalifornia","Resto","vida.Muertes_antes_de"))

@app.route("/BajaCalifornia/Esperanza_de_vida/Resto")
def BajEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("BajaCalifornia","Resto","vida.Esperanza_de_vida"))

# CAMPECHE

@app.route("/Campeche/Sobrevivientes/Total")
def CmpSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Campeche","Total","vida.Sobrevivientes"))

@app.route("/Campeche/Probabilidad_Supervivencia/Total")
def CmpProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Campeche","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Campeche/Probabilidad_muerte/Total")
def CmpProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Campeche","Total","vida.Probabilidad_muerte"))

@app.route("/Campeche/Muertes_antes_de/Total")
def CmpMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Campeche","Total","vida.Muertes_antes_de"))

@app.route("/Campeche/Esperanza_de_vida/Total")
def CmpEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Campeche","Total","vida.Esperanza_de_vida"))

@app.route("/Campeche/Sobrevivientes/Comercio")
def CmpSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Campeche","Comercio","vida.Sobrevivientes"))

@app.route("/Campeche/Probabilidad_Supervivencia/Comercio")
def CmpProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Campeche","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Campeche/Probabilidad_muerte/Comercio")
def CmpProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Campeche","Comercio","vida.Probabilidad_muerte"))

@app.route("/Campeche/Muertes_antes_de/Comercio")
def CmpMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Campeche","Comercio","vida.Muertes_antes_de"))

@app.route("/Campeche/Esperanza_de_vida/Comercio")
def CmpEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Campeche","Comercio","vida.Esperanza_de_vida"))


@app.route("/Campeche/Sobrevivientes/Manufacturas")
def CmpSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Campeche","Manufacturas","vida.Sobrevivientes"))

@app.route("/Campeche/Probabilidad_Supervivencia/Manufacturas")
def CmpProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Campeche","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Campeche/Probabilidad_muerte/Manufacturas")
def CmpProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Campeche","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Campeche/Muertes_antes_de/Manufacturas")
def CmpMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Campeche","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Campeche/Esperanza_de_vida/Manufacturas")
def CmpEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Campeche","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Campeche/Sobrevivientes/Servicios")
def CmpSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Campeche","Servicios","vida.Sobrevivientes"))

@app.route("/Campeche/Probabilidad_Supervivencia/Servicios")
def CmpProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Campeche","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Campeche/Probabilidad_muerte/Servicios")
def CmpProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Campeche","Servicios","vida.Probabilidad_muerte"))

@app.route("/Campeche/Muertes_antes_de/Servicios")
def CmpMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Campeche","Servicios","vida.Muertes_antes_de"))

@app.route("/Campeche/Esperanza_de_vida/Servicios")
def CmpEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Campeche","Servicios","vida.Esperanza_de_vida"))


@app.route("/Campeche/Sobrevivientes/Resto")
def CmpSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Campeche","Resto","vida.Sobrevivientes"))

@app.route("/Campeche/Probabilidad_Supervivencia/Resto")
def CmpProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Campeche","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Campeche/Probabilidad_muerte/Resto")
def CmpProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Campeche","Resto","vida.Probabilidad_muerte"))

@app.route("/Campeche/Muertes_antes_de/Resto")
def CmpMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Campeche","Resto","vida.Muertes_antes_de"))

@app.route("/Campeche/Esperanza_de_vida/Resto")
def CmpEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Campeche","Resto","vida.Esperanza_de_vida"))

# CDMX

@app.route("/CDMX/Sobrevivientes/Total")
def CDMSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("CDMX","Total","vida.Sobrevivientes"))

@app.route("/CDMX/Probabilidad_Supervivencia/Total")
def CDMProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("CDMX","Total","vida.Probabilidad_Supervivencia"))

@app.route("/CDMX/Probabilidad_muerte/Total")
def CDMProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("CDMX","Total","vida.Probabilidad_muerte"))

@app.route("/CDMX/Muertes_antes_de/Total")
def CDMMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("CDMX","Total","vida.Muertes_antes_de"))

@app.route("/CDMX/Esperanza_de_vida/Total")
def CDMEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("CDMX","Total","vida.Esperanza_de_vida"))

@app.route("/CDMX/Sobrevivientes/Comercio")
def CDMSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("CDMX","Comercio","vida.Sobrevivientes"))

@app.route("/CDMX/Probabilidad_Supervivencia/Comercio")
def CDMProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("CDMX","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/CDMX/Probabilidad_muerte/Comercio")
def CDMProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("CDMX","Comercio","vida.Probabilidad_muerte"))

@app.route("/CDMX/Muertes_antes_de/Comercio")
def CDMMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("CDMX","Comercio","vida.Muertes_antes_de"))

@app.route("/CDMX/Esperanza_de_vida/Comercio")
def CDMEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("CDMX","Comercio","vida.Esperanza_de_vida"))


@app.route("/CDMX/Sobrevivientes/Manufacturas")
def CDMSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("CDMX","Manufacturas","vida.Sobrevivientes"))

@app.route("/CDMX/Probabilidad_Supervivencia/Manufacturas")
def CDMProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("CDMX","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/CDMX/Probabilidad_muerte/Manufacturas")
def CDMProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("CDMX","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/CDMX/Muertes_antes_de/Manufacturas")
def CDMMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("CDMX","Manufacturas","vida.Muertes_antes_de"))

@app.route("/CDMX/Esperanza_de_vida/Manufacturas")
def CDMEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("CDMX","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/CDMX/Sobrevivientes/Servicios")
def CDMSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("CDMX","Servicios","vida.Sobrevivientes"))

@app.route("/CDMX/Probabilidad_Supervivencia/Servicios")
def CDMProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("CDMX","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/CDMX/Probabilidad_muerte/Servicios")
def CDMProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("CDMX","Servicios","vida.Probabilidad_muerte"))

@app.route("/CDMX/Muertes_antes_de/Servicios")
def CDMMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("CDMX","Servicios","vida.Muertes_antes_de"))

@app.route("/CDMX/Esperanza_de_vida/Servicios")
def CDMEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("CDMX","Servicios","vida.Esperanza_de_vida"))


@app.route("/CDMX/Sobrevivientes/Resto")
def CDMSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("CDMX","Resto","vida.Sobrevivientes"))

@app.route("/CDMX/Probabilidad_Supervivencia/Resto")
def CDMProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("CDMX","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/CDMX/Probabilidad_muerte/Resto")
def CDMProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("CDMX","Resto","vida.Probabilidad_muerte"))

@app.route("/CDMX/Muertes_antes_de/Resto")
def CDMMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("CDMX","Resto","vida.Muertes_antes_de"))

@app.route("/CDMX/Esperanza_de_vida/Resto")
def CDMEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("CDMX","Resto","vida.Esperanza_de_vida"))

# CHIHUAHUA

@app.route("/Chihuahua/Sobrevivientes/Total")
def ChiSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Chihuahua","Total","vida.Sobrevivientes"))

@app.route("/Chihuahua/Probabilidad_Supervivencia/Total")
def ChiProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Chihuahua","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Chihuahua/Probabilidad_muerte/Total")
def ChiProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Chihuahua","Total","vida.Probabilidad_muerte"))

@app.route("/Chihuahua/Muertes_antes_de/Total")
def ChiMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Chihuahua","Total","vida.Muertes_antes_de"))

@app.route("/Chihuahua/Esperanza_de_vida/Total")
def ChiEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Chihuahua","Total","vida.Esperanza_de_vida"))

@app.route("/Chihuahua/Sobrevivientes/Comercio")
def ChiSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Chihuahua","Comercio","vida.Sobrevivientes"))

@app.route("/Chihuahua/Probabilidad_Supervivencia/Comercio")
def ChiProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Chihuahua","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Chihuahua/Probabilidad_muerte/Comercio")
def ChiProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Chihuahua","Comercio","vida.Probabilidad_muerte"))

@app.route("/Chihuahua/Muertes_antes_de/Comercio")
def ChiMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Chihuahua","Comercio","vida.Muertes_antes_de"))

@app.route("/Chihuahua/Esperanza_de_vida/Comercio")
def ChiEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Chihuahua","Comercio","vida.Esperanza_de_vida"))


@app.route("/Chihuahua/Sobrevivientes/Manufacturas")
def ChiSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Chihuahua","Manufacturas","vida.Sobrevivientes"))

@app.route("/Chihuahua/Probabilidad_Supervivencia/Manufacturas")
def ChiProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Chihuahua","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Chihuahua/Probabilidad_muerte/Manufacturas")
def ChiProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Chihuahua","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Chihuahua/Muertes_antes_de/Manufacturas")
def ChiMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Chihuahua","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Chihuahua/Esperanza_de_vida/Manufacturas")
def ChiEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Chihuahua","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Chihuahua/Sobrevivientes/Servicios")
def ChiSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Chihuahua","Servicios","vida.Sobrevivientes"))

@app.route("/Chihuahua/Probabilidad_Supervivencia/Servicios")
def ChiProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Chihuahua","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Chihuahua/Probabilidad_muerte/Servicios")
def ChiProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Chihuahua","Servicios","vida.Probabilidad_muerte"))

@app.route("/Chihuahua/Muertes_antes_de/Servicios")
def ChiMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Chihuahua","Servicios","vida.Muertes_antes_de"))

@app.route("/Chihuahua/Esperanza_de_vida/Servicios")
def ChiEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Chihuahua","Servicios","vida.Esperanza_de_vida"))


@app.route("/Chihuahua/Sobrevivientes/Resto")
def ChiSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Chihuahua","Resto","vida.Sobrevivientes"))

@app.route("/Chihuahua/Probabilidad_Supervivencia/Resto")
def ChiProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Chihuahua","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Chihuahua/Probabilidad_muerte/Resto")
def ChiProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Chihuahua","Resto","vida.Probabilidad_muerte"))

@app.route("/Chihuahua/Muertes_antes_de/Resto")
def ChiMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Chihuahua","Resto","vida.Muertes_antes_de"))

@app.route("/Chihuahua/Esperanza_de_vida/Resto")
def ChiEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Chihuahua","Resto","vida.Esperanza_de_vida"))




if __name__ == '__main__':
    app.run(debug=True)
