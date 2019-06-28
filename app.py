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
    print(results)
    # Create a dictionary from the row data and append to a list
    lista_resultado = []
    for Edad, Dato in results:
        lista_dict = {}
        lista_dict["Edad"] = Edad
        lista_dict[Parametro[5:]] = Dato
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

# BAJA CALIFORNIA SUR

@app.route("/BajaCaliforniaSur/Sobrevivientes/Total")
def BCSSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Total","vida.Sobrevivientes"))

@app.route("/BajaCaliforniaSur/Probabilidad_Supervivencia/Total")
def BCSProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Total","vida.Probabilidad_Supervivencia"))

@app.route("/BajaCaliforniaSur/Probabilidad_muerte/Total")
def BCSProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Total","vida.Probabilidad_muerte"))

@app.route("/BajaCaliforniaSur/Muertes_antes_de/Total")
def BCSMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Total","vida.Muertes_antes_de"))

@app.route("/BajaCaliforniaSur/Esperanza_de_vida/Total")
def BCSEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Total","vida.Esperanza_de_vida"))

@app.route("/BajaCaliforniaSur/Sobrevivientes/Comercio")
def BCSSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Comercio","vida.Sobrevivientes"))

@app.route("/BajaCaliforniaSur/Probabilidad_Supervivencia/Comercio")
def BCSProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/BajaCaliforniaSur/Probabilidad_muerte/Comercio")
def BCSProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Comercio","vida.Probabilidad_muerte"))

@app.route("/BajaCaliforniaSur/Muertes_antes_de/Comercio")
def BCSMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Comercio","vida.Muertes_antes_de"))

@app.route("/BajaCaliforniaSur/Esperanza_de_vida/Comercio")
def BCSEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Comercio","vida.Esperanza_de_vida"))


@app.route("/BajaCaliforniaSur/Sobrevivientes/Manufacturas")
def BCSSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Manufacturas","vida.Sobrevivientes"))

@app.route("/BajaCaliforniaSur/Probabilidad_Supervivencia/Manufacturas")
def BCSProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/BajaCaliforniaSur/Probabilidad_muerte/Manufacturas")
def BCSProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/BajaCaliforniaSur/Muertes_antes_de/Manufacturas")
def BCSMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Manufacturas","vida.Muertes_antes_de"))

@app.route("/BajaCaliforniaSur/Esperanza_de_vida/Manufacturas")
def BCSEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/BajaCaliforniaSur/Sobrevivientes/Servicios")
def BCSSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Servicios","vida.Sobrevivientes"))

@app.route("/BajaCaliforniaSur/Probabilidad_Supervivencia/Servicios")
def BCSProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/BajaCaliforniaSur/Probabilidad_muerte/Servicios")
def BCSProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Servicios","vida.Probabilidad_muerte"))

@app.route("/BajaCaliforniaSur/Muertes_antes_de/Servicios")
def BCSMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Servicios","vida.Muertes_antes_de"))

@app.route("/BajaCaliforniaSur/Esperanza_de_vida/Servicios")
def BCSEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Servicios","vida.Esperanza_de_vida"))


@app.route("/BajaCaliforniaSur/Sobrevivientes/Resto")
def BCSSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Resto","vida.Sobrevivientes"))

@app.route("/BajaCaliforniaSur/Probabilidad_Supervivencia/Resto")
def BCSProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/BajaCaliforniaSur/Probabilidad_muerte/Resto")
def BCSProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Resto","vida.Probabilidad_muerte"))

@app.route("/BajaCaliforniaSur/Muertes_antes_de/Resto")
def BCSMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Resto","vida.Muertes_antes_de"))

@app.route("/BajaCaliforniaSur/Esperanza_de_vida/Resto")
def BCSEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("BajaCaliforniaSur","Resto","vida.Esperanza_de_vida"))

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

# CHIAPAS

@app.route("/Chiapas/Sobrevivientes/Total")
def CiaSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Chiapas","Total","vida.Sobrevivientes"))

@app.route("/Chiapas/Probabilidad_Supervivencia/Total")
def CiaProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Chiapas","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Chiapas/Probabilidad_muerte/Total")
def CiaProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Chiapas","Total","vida.Probabilidad_muerte"))

@app.route("/Chiapas/Muertes_antes_de/Total")
def CiaMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Chiapas","Total","vida.Muertes_antes_de"))

@app.route("/Chiapas/Esperanza_de_vida/Total")
def CiaEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Chiapas","Total","vida.Esperanza_de_vida"))

@app.route("/Chiapas/Sobrevivientes/Comercio")
def CiaSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Chiapas","Comercio","vida.Sobrevivientes"))

@app.route("/Chiapas/Probabilidad_Supervivencia/Comercio")
def CiaProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Chiapas","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Chiapas/Probabilidad_muerte/Comercio")
def CiaProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Chiapas","Comercio","vida.Probabilidad_muerte"))

@app.route("/Chiapas/Muertes_antes_de/Comercio")
def CiaMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Chiapas","Comercio","vida.Muertes_antes_de"))

@app.route("/Chiapas/Esperanza_de_vida/Comercio")
def CiaEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Chiapas","Comercio","vida.Esperanza_de_vida"))


@app.route("/Chiapas/Sobrevivientes/Manufacturas")
def CiaSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Chiapas","Manufacturas","vida.Sobrevivientes"))

@app.route("/Chiapas/Probabilidad_Supervivencia/Manufacturas")
def CiaProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Chiapas","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Chiapas/Probabilidad_muerte/Manufacturas")
def CiaProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Chiapas","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Chiapas/Muertes_antes_de/Manufacturas")
def CiaMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Chiapas","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Chiapas/Esperanza_de_vida/Manufacturas")
def CiaEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Chiapas","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Chiapas/Sobrevivientes/Servicios")
def CiaSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Chiapas","Servicios","vida.Sobrevivientes"))

@app.route("/Chiapas/Probabilidad_Supervivencia/Servicios")
def CiaProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Chiapas","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Chiapas/Probabilidad_muerte/Servicios")
def CiaProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Chiapas","Servicios","vida.Probabilidad_muerte"))

@app.route("/Chiapas/Muertes_antes_de/Servicios")
def CiaMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Chiapas","Servicios","vida.Muertes_antes_de"))

@app.route("/Chiapas/Esperanza_de_vida/Servicios")
def CiaEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Chiapas","Servicios","vida.Esperanza_de_vida"))


@app.route("/Chiapas/Sobrevivientes/Resto")
def CiaSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Chiapas","Resto","vida.Sobrevivientes"))

@app.route("/Chiapas/Probabilidad_Supervivencia/Resto")
def CiaProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Chiapas","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Chiapas/Probabilidad_muerte/Resto")
def CiaProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Chiapas","Resto","vida.Probabilidad_muerte"))

@app.route("/Chiapas/Muertes_antes_de/Resto")
def CiaMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Chiapas","Resto","vida.Muertes_antes_de"))

@app.route("/Chiapas/Esperanza_de_vida/Resto")
def CiaEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Chiapas","Resto","vida.Esperanza_de_vida"))

# COAHUILA

@app.route("/Coahuila/Sobrevivientes/Total")
def CoaSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Coahuila","Total","vida.Sobrevivientes"))

@app.route("/Coahuila/Probabilidad_Supervivencia/Total")
def CoaProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Coahuila","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Coahuila/Probabilidad_muerte/Total")
def CoaProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Coahuila","Total","vida.Probabilidad_muerte"))

@app.route("/Coahuila/Muertes_antes_de/Total")
def CoaMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Coahuila","Total","vida.Muertes_antes_de"))

@app.route("/Coahuila/Esperanza_de_vida/Total")
def CoaEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Coahuila","Total","vida.Esperanza_de_vida"))

@app.route("/Coahuila/Sobrevivientes/Comercio")
def CoaSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Coahuila","Comercio","vida.Sobrevivientes"))

@app.route("/Coahuila/Probabilidad_Supervivencia/Comercio")
def CoaProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Coahuila","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Coahuila/Probabilidad_muerte/Comercio")
def CoaProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Coahuila","Comercio","vida.Probabilidad_muerte"))

@app.route("/Coahuila/Muertes_antes_de/Comercio")
def CoaMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Coahuila","Comercio","vida.Muertes_antes_de"))

@app.route("/Coahuila/Esperanza_de_vida/Comercio")
def CoaEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Coahuila","Comercio","vida.Esperanza_de_vida"))


@app.route("/Coahuila/Sobrevivientes/Manufacturas")
def CoaSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Coahuila","Manufacturas","vida.Sobrevivientes"))

@app.route("/Coahuila/Probabilidad_Supervivencia/Manufacturas")
def CoaProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Coahuila","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Coahuila/Probabilidad_muerte/Manufacturas")
def CoaProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Coahuila","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Coahuila/Muertes_antes_de/Manufacturas")
def CoaMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Coahuila","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Coahuila/Esperanza_de_vida/Manufacturas")
def CoaEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Coahuila","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Coahuila/Sobrevivientes/Servicios")
def CoaSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Coahuila","Servicios","vida.Sobrevivientes"))

@app.route("/Coahuila/Probabilidad_Supervivencia/Servicios")
def CoaProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Coahuila","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Coahuila/Probabilidad_muerte/Servicios")
def CoaProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Coahuila","Servicios","vida.Probabilidad_muerte"))

@app.route("/Coahuila/Muertes_antes_de/Servicios")
def CoaMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Coahuila","Servicios","vida.Muertes_antes_de"))

@app.route("/Coahuila/Esperanza_de_vida/Servicios")
def CoaEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Coahuila","Servicios","vida.Esperanza_de_vida"))


@app.route("/Coahuila/Sobrevivientes/Resto")
def CoaSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Coahuila","Resto","vida.Sobrevivientes"))

@app.route("/Coahuila/Probabilidad_Supervivencia/Resto")
def CoaProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Coahuila","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Coahuila/Probabilidad_muerte/Resto")
def CoaProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Coahuila","Resto","vida.Probabilidad_muerte"))

@app.route("/Coahuila/Muertes_antes_de/Resto")
def CoaMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Coahuila","Resto","vida.Muertes_antes_de"))

@app.route("/Coahuila/Esperanza_de_vida/Resto")
def CoaEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Coahuila","Resto","vida.Esperanza_de_vida"))

# COLIMA

@app.route("/Colima/Sobrevivientes/Total")
def ColSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Colima","Total","vida.Sobrevivientes"))

@app.route("/Colima/Probabilidad_Supervivencia/Total")
def ColProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Colima","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Colima/Probabilidad_muerte/Total")
def ColProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Colima","Total","vida.Probabilidad_muerte"))

@app.route("/Colima/Muertes_antes_de/Total")
def ColMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Colima","Total","vida.Muertes_antes_de"))

@app.route("/Colima/Esperanza_de_vida/Total")
def ColEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Colima","Total","vida.Esperanza_de_vida"))

@app.route("/Colima/Sobrevivientes/Comercio")
def ColSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Colima","Comercio","vida.Sobrevivientes"))

@app.route("/Colima/Probabilidad_Supervivencia/Comercio")
def ColProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Colima","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Colima/Probabilidad_muerte/Comercio")
def ColProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Colima","Comercio","vida.Probabilidad_muerte"))

@app.route("/Colima/Muertes_antes_de/Comercio")
def ColMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Colima","Comercio","vida.Muertes_antes_de"))

@app.route("/Colima/Esperanza_de_vida/Comercio")
def ColEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Colima","Comercio","vida.Esperanza_de_vida"))


@app.route("/Colima/Sobrevivientes/Manufacturas")
def ColSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Colima","Manufacturas","vida.Sobrevivientes"))

@app.route("/Colima/Probabilidad_Supervivencia/Manufacturas")
def ColProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Colima","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Colima/Probabilidad_muerte/Manufacturas")
def ColProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Colima","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Colima/Muertes_antes_de/Manufacturas")
def ColMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Colima","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Colima/Esperanza_de_vida/Manufacturas")
def ColEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Colima","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Colima/Sobrevivientes/Servicios")
def ColSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Colima","Servicios","vida.Sobrevivientes"))

@app.route("/Colima/Probabilidad_Supervivencia/Servicios")
def ColProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Colima","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Colima/Probabilidad_muerte/Servicios")
def ColProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Colima","Servicios","vida.Probabilidad_muerte"))

@app.route("/Colima/Muertes_antes_de/Servicios")
def ColMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Colima","Servicios","vida.Muertes_antes_de"))

@app.route("/Colima/Esperanza_de_vida/Servicios")
def ColEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Colima","Servicios","vida.Esperanza_de_vida"))


@app.route("/Colima/Sobrevivientes/Resto")
def ColSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Colima","Resto","vida.Sobrevivientes"))

@app.route("/Colima/Probabilidad_Supervivencia/Resto")
def ColProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Colima","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Colima/Probabilidad_muerte/Resto")
def ColProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Colima","Resto","vida.Probabilidad_muerte"))

@app.route("/Colima/Muertes_antes_de/Resto")
def ColMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Colima","Resto","vida.Muertes_antes_de"))

@app.route("/Colima/Esperanza_de_vida/Resto")
def ColEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Colima","Resto","vida.Esperanza_de_vida"))

# Durango

@app.route("/Durango/Sobrevivientes/Total")
def DurSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Durango","Total","vida.Sobrevivientes"))

@app.route("/Durango/Probabilidad_Supervivencia/Total")
def DurProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Durango","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Durango/Probabilidad_muerte/Total")
def DurProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Durango","Total","vida.Probabilidad_muerte"))

@app.route("/Durango/Muertes_antes_de/Total")
def DurMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Durango","Total","vida.Muertes_antes_de"))

@app.route("/Durango/Esperanza_de_vida/Total")
def DurEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Durango","Total","vida.Esperanza_de_vida"))

@app.route("/Durango/Sobrevivientes/Comercio")
def DurSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Durango","Comercio","vida.Sobrevivientes"))

@app.route("/Durango/Probabilidad_Supervivencia/Comercio")
def DurProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Durango","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Durango/Probabilidad_muerte/Comercio")
def DurProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Durango","Comercio","vida.Probabilidad_muerte"))

@app.route("/Durango/Muertes_antes_de/Comercio")
def DurMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Durango","Comercio","vida.Muertes_antes_de"))

@app.route("/Durango/Esperanza_de_vida/Comercio")
def DurEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Durango","Comercio","vida.Esperanza_de_vida"))


@app.route("/Durango/Sobrevivientes/Manufacturas")
def DurSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Durango","Manufacturas","vida.Sobrevivientes"))

@app.route("/Durango/Probabilidad_Supervivencia/Manufacturas")
def DurProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Durango","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Durango/Probabilidad_muerte/Manufacturas")
def DurProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Durango","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Durango/Muertes_antes_de/Manufacturas")
def DurMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Durango","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Durango/Esperanza_de_vida/Manufacturas")
def DurEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Durango","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Durango/Sobrevivientes/Servicios")
def DurSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Durango","Servicios","vida.Sobrevivientes"))

@app.route("/Durango/Probabilidad_Supervivencia/Servicios")
def DurProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Durango","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Durango/Probabilidad_muerte/Servicios")
def DurProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Durango","Servicios","vida.Probabilidad_muerte"))

@app.route("/Durango/Muertes_antes_de/Servicios")
def DurMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Durango","Servicios","vida.Muertes_antes_de"))

@app.route("/Durango/Esperanza_de_vida/Servicios")
def DurEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Durango","Servicios","vida.Esperanza_de_vida"))


@app.route("/Durango/Sobrevivientes/Resto")
def DurSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Durango","Resto","vida.Sobrevivientes"))

@app.route("/Durango/Probabilidad_Supervivencia/Resto")
def DurProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Durango","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Durango/Probabilidad_muerte/Resto")
def DurProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Durango","Resto","vida.Probabilidad_muerte"))

@app.route("/Durango/Muertes_antes_de/Resto")
def DurMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Durango","Resto","vida.Muertes_antes_de"))

@app.route("/Durango/Esperanza_de_vida/Resto")
def DurEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Durango","Resto","vida.Esperanza_de_vida"))

# Guerrero

@app.route("/Guerrero/Sobrevivientes/Total")
def GueSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Guerrero","Total","vida.Sobrevivientes"))

@app.route("/Guerrero/Probabilidad_Supervivencia/Total")
def GueProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Guerrero","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Guerrero/Probabilidad_muerte/Total")
def GueProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Guerrero","Total","vida.Probabilidad_muerte"))

@app.route("/Guerrero/Muertes_antes_de/Total")
def GueMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Guerrero","Total","vida.Muertes_antes_de"))

@app.route("/Guerrero/Esperanza_de_vida/Total")
def GueEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Guerrero","Total","vida.Esperanza_de_vida"))

@app.route("/Guerrero/Sobrevivientes/Comercio")
def GueSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Guerrero","Comercio","vida.Sobrevivientes"))

@app.route("/Guerrero/Probabilidad_Supervivencia/Comercio")
def GueProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Guerrero","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Guerrero/Probabilidad_muerte/Comercio")
def GueProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Guerrero","Comercio","vida.Probabilidad_muerte"))

@app.route("/Guerrero/Muertes_antes_de/Comercio")
def GueMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Guerrero","Comercio","vida.Muertes_antes_de"))

@app.route("/Guerrero/Esperanza_de_vida/Comercio")
def GueEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Guerrero","Comercio","vida.Esperanza_de_vida"))


@app.route("/Guerrero/Sobrevivientes/Manufacturas")
def GueSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Guerrero","Manufacturas","vida.Sobrevivientes"))

@app.route("/Guerrero/Probabilidad_Supervivencia/Manufacturas")
def GueProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Guerrero","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Guerrero/Probabilidad_muerte/Manufacturas")
def GueProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Guerrero","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Guerrero/Muertes_antes_de/Manufacturas")
def GueMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Guerrero","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Guerrero/Esperanza_de_vida/Manufacturas")
def GueEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Guerrero","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Guerrero/Sobrevivientes/Servicios")
def GueSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Guerrero","Servicios","vida.Sobrevivientes"))

@app.route("/Guerrero/Probabilidad_Supervivencia/Servicios")
def GueProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Guerrero","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Guerrero/Probabilidad_muerte/Servicios")
def GueProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Guerrero","Servicios","vida.Probabilidad_muerte"))

@app.route("/Guerrero/Muertes_antes_de/Servicios")
def GueMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Guerrero","Servicios","vida.Muertes_antes_de"))

@app.route("/Guerrero/Esperanza_de_vida/Servicios")
def GueEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Guerrero","Servicios","vida.Esperanza_de_vida"))


@app.route("/Guerrero/Sobrevivientes/Resto")
def GueSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Guerrero","Resto","vida.Sobrevivientes"))

@app.route("/Guerrero/Probabilidad_Supervivencia/Resto")
def GueProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Guerrero","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Guerrero/Probabilidad_muerte/Resto")
def GueProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Guerrero","Resto","vida.Probabilidad_muerte"))

@app.route("/Guerrero/Muertes_antes_de/Resto")
def GueMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Guerrero","Resto","vida.Muertes_antes_de"))

@app.route("/Guerrero/Esperanza_de_vida/Resto")
def GueEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Guerrero","Resto","vida.Esperanza_de_vida"))

# Guanajuato

@app.route("/Guanajuato/Sobrevivientes/Total")
def GuaSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Guanajuato","Total","vida.Sobrevivientes"))

@app.route("/Guanajuato/Probabilidad_Supervivencia/Total")
def GuaProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Guanajuato","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Guanajuato/Probabilidad_muerte/Total")
def GuaProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Guanajuato","Total","vida.Probabilidad_muerte"))

@app.route("/Guanajuato/Muertes_antes_de/Total")
def GuaMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Guanajuato","Total","vida.Muertes_antes_de"))

@app.route("/Guanajuato/Esperanza_de_vida/Total")
def GuaEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Guanajuato","Total","vida.Esperanza_de_vida"))

@app.route("/Guanajuato/Sobrevivientes/Comercio")
def GuaSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Guanajuato","Comercio","vida.Sobrevivientes"))

@app.route("/Guanajuato/Probabilidad_Supervivencia/Comercio")
def GuaProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Guanajuato","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Guanajuato/Probabilidad_muerte/Comercio")
def GuaProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Guanajuato","Comercio","vida.Probabilidad_muerte"))

@app.route("/Guanajuato/Muertes_antes_de/Comercio")
def GuaMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Guanajuato","Comercio","vida.Muertes_antes_de"))

@app.route("/Guanajuato/Esperanza_de_vida/Comercio")
def GuaEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Guanajuato","Comercio","vida.Esperanza_de_vida"))


@app.route("/Guanajuato/Sobrevivientes/Manufacturas")
def GuaSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Guanajuato","Manufacturas","vida.Sobrevivientes"))

@app.route("/Guanajuato/Probabilidad_Supervivencia/Manufacturas")
def GuaProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Guanajuato","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Guanajuato/Probabilidad_muerte/Manufacturas")
def GuaProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Guanajuato","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Guanajuato/Muertes_antes_de/Manufacturas")
def GuaMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Guanajuato","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Guanajuato/Esperanza_de_vida/Manufacturas")
def GuaEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Guanajuato","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Guanajuato/Sobrevivientes/Servicios")
def GuaSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Guanajuato","Servicios","vida.Sobrevivientes"))

@app.route("/Guanajuato/Probabilidad_Supervivencia/Servicios")
def GuaProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Guanajuato","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Guanajuato/Probabilidad_muerte/Servicios")
def GuaProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Guanajuato","Servicios","vida.Probabilidad_muerte"))

@app.route("/Guanajuato/Muertes_antes_de/Servicios")
def GuaMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Guanajuato","Servicios","vida.Muertes_antes_de"))

@app.route("/Guanajuato/Esperanza_de_vida/Servicios")
def GuaEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Guanajuato","Servicios","vida.Esperanza_de_vida"))


@app.route("/Guanajuato/Sobrevivientes/Resto")
def GuaSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Guanajuato","Resto","vida.Sobrevivientes"))

@app.route("/Guanajuato/Probabilidad_Supervivencia/Resto")
def GuaProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Guanajuato","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Guanajuato/Probabilidad_muerte/Resto")
def GuaProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Guanajuato","Resto","vida.Probabilidad_muerte"))

@app.route("/Guanajuato/Muertes_antes_de/Resto")
def GuaMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Guanajuato","Resto","vida.Muertes_antes_de"))

@app.route("/Guanajuato/Esperanza_de_vida/Resto")
def GuaEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Guanajuato","Resto","vida.Esperanza_de_vida"))

# Hidalgo

@app.route("/Hidalgo/Sobrevivientes/Total")
def HidSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Hidalgo","Total","vida.Sobrevivientes"))

@app.route("/Hidalgo/Probabilidad_Supervivencia/Total")
def HidProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Hidalgo","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Hidalgo/Probabilidad_muerte/Total")
def HidProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Hidalgo","Total","vida.Probabilidad_muerte"))

@app.route("/Hidalgo/Muertes_antes_de/Total")
def HidMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Hidalgo","Total","vida.Muertes_antes_de"))

@app.route("/Hidalgo/Esperanza_de_vida/Total")
def HidEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Hidalgo","Total","vida.Esperanza_de_vida"))

@app.route("/Hidalgo/Sobrevivientes/Comercio")
def HidSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Hidalgo","Comercio","vida.Sobrevivientes"))

@app.route("/Hidalgo/Probabilidad_Supervivencia/Comercio")
def HidProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Hidalgo","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Hidalgo/Probabilidad_muerte/Comercio")
def HidProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Hidalgo","Comercio","vida.Probabilidad_muerte"))

@app.route("/Hidalgo/Muertes_antes_de/Comercio")
def HidMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Hidalgo","Comercio","vida.Muertes_antes_de"))

@app.route("/Hidalgo/Esperanza_de_vida/Comercio")
def HidEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Hidalgo","Comercio","vida.Esperanza_de_vida"))


@app.route("/Hidalgo/Sobrevivientes/Manufacturas")
def HidSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Hidalgo","Manufacturas","vida.Sobrevivientes"))

@app.route("/Hidalgo/Probabilidad_Supervivencia/Manufacturas")
def HidProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Hidalgo","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Hidalgo/Probabilidad_muerte/Manufacturas")
def HidProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Hidalgo","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Hidalgo/Muertes_antes_de/Manufacturas")
def HidMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Hidalgo","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Hidalgo/Esperanza_de_vida/Manufacturas")
def HidEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Hidalgo","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Hidalgo/Sobrevivientes/Servicios")
def HidSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Hidalgo","Servicios","vida.Sobrevivientes"))

@app.route("/Hidalgo/Probabilidad_Supervivencia/Servicios")
def HidProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Hidalgo","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Hidalgo/Probabilidad_muerte/Servicios")
def HidProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Hidalgo","Servicios","vida.Probabilidad_muerte"))

@app.route("/Hidalgo/Muertes_antes_de/Servicios")
def HidMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Hidalgo","Servicios","vida.Muertes_antes_de"))

@app.route("/Hidalgo/Esperanza_de_vida/Servicios")
def HidEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Hidalgo","Servicios","vida.Esperanza_de_vida"))


@app.route("/Hidalgo/Sobrevivientes/Resto")
def HidSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Hidalgo","Resto","vida.Sobrevivientes"))

@app.route("/Hidalgo/Probabilidad_Supervivencia/Resto")
def HidProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Hidalgo","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Hidalgo/Probabilidad_muerte/Resto")
def HidProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Hidalgo","Resto","vida.Probabilidad_muerte"))

@app.route("/Hidalgo/Muertes_antes_de/Resto")
def HidMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Hidalgo","Resto","vida.Muertes_antes_de"))

@app.route("/Hidalgo/Esperanza_de_vida/Resto")
def HidEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Hidalgo","Resto","vida.Esperanza_de_vida"))

# Jalisco

@app.route("/Jalisco/Sobrevivientes/Total")
def JalSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Jalisco","Total","vida.Sobrevivientes"))

@app.route("/Jalisco/Probabilidad_Supervivencia/Total")
def JalProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Jalisco","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Jalisco/Probabilidad_muerte/Total")
def JalProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Jalisco","Total","vida.Probabilidad_muerte"))

@app.route("/Jalisco/Muertes_antes_de/Total")
def JalMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Jalisco","Total","vida.Muertes_antes_de"))

@app.route("/Jalisco/Esperanza_de_vida/Total")
def JalEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Jalisco","Total","vida.Esperanza_de_vida"))

@app.route("/Jalisco/Sobrevivientes/Comercio")
def JalSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Jalisco","Comercio","vida.Sobrevivientes"))

@app.route("/Jalisco/Probabilidad_Supervivencia/Comercio")
def JalProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Jalisco","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Jalisco/Probabilidad_muerte/Comercio")
def JalProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Jalisco","Comercio","vida.Probabilidad_muerte"))

@app.route("/Jalisco/Muertes_antes_de/Comercio")
def JalMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Jalisco","Comercio","vida.Muertes_antes_de"))

@app.route("/Jalisco/Esperanza_de_vida/Comercio")
def JalEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Jalisco","Comercio","vida.Esperanza_de_vida"))


@app.route("/Jalisco/Sobrevivientes/Manufacturas")
def JalSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Jalisco","Manufacturas","vida.Sobrevivientes"))

@app.route("/Jalisco/Probabilidad_Supervivencia/Manufacturas")
def JalProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Jalisco","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Jalisco/Probabilidad_muerte/Manufacturas")
def JalProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Jalisco","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Jalisco/Muertes_antes_de/Manufacturas")
def JalMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Jalisco","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Jalisco/Esperanza_de_vida/Manufacturas")
def JalEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Jalisco","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Jalisco/Sobrevivientes/Servicios")
def JalSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Jalisco","Servicios","vida.Sobrevivientes"))

@app.route("/Jalisco/Probabilidad_Supervivencia/Servicios")
def JalProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Jalisco","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Jalisco/Probabilidad_muerte/Servicios")
def JalProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Jalisco","Servicios","vida.Probabilidad_muerte"))

@app.route("/Jalisco/Muertes_antes_de/Servicios")
def JalMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Jalisco","Servicios","vida.Muertes_antes_de"))

@app.route("/Jalisco/Esperanza_de_vida/Servicios")
def JalEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Jalisco","Servicios","vida.Esperanza_de_vida"))


@app.route("/Jalisco/Sobrevivientes/Resto")
def JalSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Jalisco","Resto","vida.Sobrevivientes"))

@app.route("/Jalisco/Probabilidad_Supervivencia/Resto")
def JalProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Jalisco","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Jalisco/Probabilidad_muerte/Resto")
def JalProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Jalisco","Resto","vida.Probabilidad_muerte"))

@app.route("/Jalisco/Muertes_antes_de/Resto")
def JalMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Jalisco","Resto","vida.Muertes_antes_de"))

@app.route("/Jalisco/Esperanza_de_vida/Resto")
def JalEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Jalisco","Resto","vida.Esperanza_de_vida"))

# Estado De Mexico

@app.route("/EstadoDeMexico/Sobrevivientes/Total")
def EdoSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("EstadoDeMexico","Total","vida.Sobrevivientes"))

@app.route("/EstadoDeMexico/Probabilidad_Supervivencia/Total")
def EdoProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("EstadoDeMexico","Total","vida.Probabilidad_Supervivencia"))

@app.route("/EstadoDeMexico/Probabilidad_muerte/Total")
def EdoProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("EstadoDeMexico","Total","vida.Probabilidad_muerte"))

@app.route("/EstadoDeMexico/Muertes_antes_de/Total")
def EdoMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("EstadoDeMexico","Total","vida.Muertes_antes_de"))

@app.route("/EstadoDeMexico/Esperanza_de_vida/Total")
def EdoEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("EstadoDeMexico","Total","vida.Esperanza_de_vida"))

@app.route("/EstadoDeMexico/Sobrevivientes/Comercio")
def EdoSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("EstadoDeMexico","Comercio","vida.Sobrevivientes"))

@app.route("/EstadoDeMexico/Probabilidad_Supervivencia/Comercio")
def EdoProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("EstadoDeMexico","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/EstadoDeMexico/Probabilidad_muerte/Comercio")
def EdoProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("EstadoDeMexico","Comercio","vida.Probabilidad_muerte"))

@app.route("/EstadoDeMexico/Muertes_antes_de/Comercio")
def EdoMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("EstadoDeMexico","Comercio","vida.Muertes_antes_de"))

@app.route("/EstadoDeMexico/Esperanza_de_vida/Comercio")
def EdoEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("EstadoDeMexico","Comercio","vida.Esperanza_de_vida"))


@app.route("/EstadoDeMexico/Sobrevivientes/Manufacturas")
def EdoSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("EstadoDeMexico","Manufacturas","vida.Sobrevivientes"))

@app.route("/EstadoDeMexico/Probabilidad_Supervivencia/Manufacturas")
def EdoProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("EstadoDeMexico","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/EstadoDeMexico/Probabilidad_muerte/Manufacturas")
def EdoProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("EstadoDeMexico","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/EstadoDeMexico/Muertes_antes_de/Manufacturas")
def EdoMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("EstadoDeMexico","Manufacturas","vida.Muertes_antes_de"))

@app.route("/EstadoDeMexico/Esperanza_de_vida/Manufacturas")
def EdoEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("EstadoDeMexico","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/EstadoDeMexico/Sobrevivientes/Servicios")
def EdoSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("EstadoDeMexico","Servicios","vida.Sobrevivientes"))

@app.route("/EstadoDeMexico/Probabilidad_Supervivencia/Servicios")
def EdoProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("EstadoDeMexico","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/EstadoDeMexico/Probabilidad_muerte/Servicios")
def EdoProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("EstadoDeMexico","Servicios","vida.Probabilidad_muerte"))

@app.route("/EstadoDeMexico/Muertes_antes_de/Servicios")
def EdoMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("EstadoDeMexico","Servicios","vida.Muertes_antes_de"))

@app.route("/EstadoDeMexico/Esperanza_de_vida/Servicios")
def EdoEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("EstadoDeMexico","Servicios","vida.Esperanza_de_vida"))


@app.route("/EstadoDeMexico/Sobrevivientes/Resto")
def EdoSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("EstadoDeMexico","Resto","vida.Sobrevivientes"))

@app.route("/EstadoDeMexico/Probabilidad_Supervivencia/Resto")
def EdoProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("EstadoDeMexico","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/EstadoDeMexico/Probabilidad_muerte/Resto")
def EdoProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("EstadoDeMexico","Resto","vida.Probabilidad_muerte"))

@app.route("/EstadoDeMexico/Muertes_antes_de/Resto")
def EdoMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("EstadoDeMexico","Resto","vida.Muertes_antes_de"))

@app.route("/EstadoDeMexico/Esperanza_de_vida/Resto")
def EdoEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("EstadoDeMexico","Resto","vida.Esperanza_de_vida"))

# Michoacan

@app.route("/Michoacan/Sobrevivientes/Total")
def MchSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Michoacan","Total","vida.Sobrevivientes"))

@app.route("/Michoacan/Probabilidad_Supervivencia/Total")
def MchProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Michoacan","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Michoacan/Probabilidad_muerte/Total")
def MchProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Michoacan","Total","vida.Probabilidad_muerte"))

@app.route("/Michoacan/Muertes_antes_de/Total")
def MchMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Michoacan","Total","vida.Muertes_antes_de"))

@app.route("/Michoacan/Esperanza_de_vida/Total")
def MchEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Michoacan","Total","vida.Esperanza_de_vida"))

@app.route("/Michoacan/Sobrevivientes/Comercio")
def MchSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Michoacan","Comercio","vida.Sobrevivientes"))

@app.route("/Michoacan/Probabilidad_Supervivencia/Comercio")
def MchProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Michoacan","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Michoacan/Probabilidad_muerte/Comercio")
def MchProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Michoacan","Comercio","vida.Probabilidad_muerte"))

@app.route("/Michoacan/Muertes_antes_de/Comercio")
def MchMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Michoacan","Comercio","vida.Muertes_antes_de"))

@app.route("/Michoacan/Esperanza_de_vida/Comercio")
def MchEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Michoacan","Comercio","vida.Esperanza_de_vida"))


@app.route("/Michoacan/Sobrevivientes/Manufacturas")
def MchSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Michoacan","Manufacturas","vida.Sobrevivientes"))

@app.route("/Michoacan/Probabilidad_Supervivencia/Manufacturas")
def MchProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Michoacan","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Michoacan/Probabilidad_muerte/Manufacturas")
def MchProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Michoacan","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Michoacan/Muertes_antes_de/Manufacturas")
def MchMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Michoacan","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Michoacan/Esperanza_de_vida/Manufacturas")
def MchEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Michoacan","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Michoacan/Sobrevivientes/Servicios")
def MchSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Michoacan","Servicios","vida.Sobrevivientes"))

@app.route("/Michoacan/Probabilidad_Supervivencia/Servicios")
def MchProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Michoacan","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Michoacan/Probabilidad_muerte/Servicios")
def MchProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Michoacan","Servicios","vida.Probabilidad_muerte"))

@app.route("/Michoacan/Muertes_antes_de/Servicios")
def MchMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Michoacan","Servicios","vida.Muertes_antes_de"))

@app.route("/Michoacan/Esperanza_de_vida/Servicios")
def MchEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Michoacan","Servicios","vida.Esperanza_de_vida"))


@app.route("/Michoacan/Sobrevivientes/Resto")
def MchSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Michoacan","Resto","vida.Sobrevivientes"))

@app.route("/Michoacan/Probabilidad_Supervivencia/Resto")
def MchProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Michoacan","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Michoacan/Probabilidad_muerte/Resto")
def MchProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Michoacan","Resto","vida.Probabilidad_muerte"))

@app.route("/Michoacan/Muertes_antes_de/Resto")
def MchMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Michoacan","Resto","vida.Muertes_antes_de"))

@app.route("/Michoacan/Esperanza_de_vida/Resto")
def MchEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Michoacan","Resto","vida.Esperanza_de_vida"))

# Morelos

@app.route("/Morelos/Sobrevivientes/Total")
def MorSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Morelos","Total","vida.Sobrevivientes"))

@app.route("/Morelos/Probabilidad_Supervivencia/Total")
def MorProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Morelos","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Morelos/Probabilidad_muerte/Total")
def MorProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Morelos","Total","vida.Probabilidad_muerte"))

@app.route("/Morelos/Muertes_antes_de/Total")
def MorMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Morelos","Total","vida.Muertes_antes_de"))

@app.route("/Morelos/Esperanza_de_vida/Total")
def MorEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Morelos","Total","vida.Esperanza_de_vida"))

@app.route("/Morelos/Sobrevivientes/Comercio")
def MorSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Morelos","Comercio","vida.Sobrevivientes"))

@app.route("/Morelos/Probabilidad_Supervivencia/Comercio")
def MorProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Morelos","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Morelos/Probabilidad_muerte/Comercio")
def MorProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Morelos","Comercio","vida.Probabilidad_muerte"))

@app.route("/Morelos/Muertes_antes_de/Comercio")
def MorMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Morelos","Comercio","vida.Muertes_antes_de"))

@app.route("/Morelos/Esperanza_de_vida/Comercio")
def MorEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Morelos","Comercio","vida.Esperanza_de_vida"))


@app.route("/Morelos/Sobrevivientes/Manufacturas")
def MorSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Morelos","Manufacturas","vida.Sobrevivientes"))

@app.route("/Morelos/Probabilidad_Supervivencia/Manufacturas")
def MorProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Morelos","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Morelos/Probabilidad_muerte/Manufacturas")
def MorProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Morelos","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Morelos/Muertes_antes_de/Manufacturas")
def MorMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Morelos","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Morelos/Esperanza_de_vida/Manufacturas")
def MorEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Morelos","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Morelos/Sobrevivientes/Servicios")
def MorSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Morelos","Servicios","vida.Sobrevivientes"))

@app.route("/Morelos/Probabilidad_Supervivencia/Servicios")
def MorProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Morelos","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Morelos/Probabilidad_muerte/Servicios")
def MorProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Morelos","Servicios","vida.Probabilidad_muerte"))

@app.route("/Morelos/Muertes_antes_de/Servicios")
def MorMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Morelos","Servicios","vida.Muertes_antes_de"))

@app.route("/Morelos/Esperanza_de_vida/Servicios")
def MorEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Morelos","Servicios","vida.Esperanza_de_vida"))


@app.route("/Morelos/Sobrevivientes/Resto")
def MorSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Morelos","Resto","vida.Sobrevivientes"))

@app.route("/Morelos/Probabilidad_Supervivencia/Resto")
def MorProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Morelos","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Morelos/Probabilidad_muerte/Resto")
def MorProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Morelos","Resto","vida.Probabilidad_muerte"))

@app.route("/Morelos/Muertes_antes_de/Resto")
def MorMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Morelos","Resto","vida.Muertes_antes_de"))

@app.route("/Morelos/Esperanza_de_vida/Resto")
def MorEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Morelos","Resto","vida.Esperanza_de_vida"))

# Nacional

@app.route("/Nacional/Sobrevivientes/Total")
def NacSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Nacional","Total","vida.Sobrevivientes"))

@app.route("/Nacional/Probabilidad_Supervivencia/Total")
def NacProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Nacional","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Nacional/Probabilidad_muerte/Total")
def NacProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Nacional","Total","vida.Probabilidad_muerte"))

@app.route("/Nacional/Muertes_antes_de/Total")
def NacMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Nacional","Total","vida.Muertes_antes_de"))

@app.route("/Nacional/Esperanza_de_vida/Total")
def NacEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Nacional","Total","vida.Esperanza_de_vida"))

@app.route("/Nacional/Sobrevivientes/Comercio")
def NacSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Nacional","Comercio","vida.Sobrevivientes"))

@app.route("/Nacional/Probabilidad_Supervivencia/Comercio")
def NacProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Nacional","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Nacional/Probabilidad_muerte/Comercio")
def NacProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Nacional","Comercio","vida.Probabilidad_muerte"))

@app.route("/Nacional/Muertes_antes_de/Comercio")
def NacMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Nacional","Comercio","vida.Muertes_antes_de"))

@app.route("/Nacional/Esperanza_de_vida/Comercio")
def NacEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Nacional","Comercio","vida.Esperanza_de_vida"))


@app.route("/Nacional/Sobrevivientes/Manufacturas")
def NacSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Nacional","Manufacturas","vida.Sobrevivientes"))

@app.route("/Nacional/Probabilidad_Supervivencia/Manufacturas")
def NacProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Nacional","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Nacional/Probabilidad_muerte/Manufacturas")
def NacProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Nacional","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Nacional/Muertes_antes_de/Manufacturas")
def NacMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Nacional","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Nacional/Esperanza_de_vida/Manufacturas")
def NacEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Nacional","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Nacional/Sobrevivientes/Servicios")
def NacSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Nacional","Servicios","vida.Sobrevivientes"))

@app.route("/Nacional/Probabilidad_Supervivencia/Servicios")
def NacProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Nacional","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Nacional/Probabilidad_muerte/Servicios")
def NacProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Nacional","Servicios","vida.Probabilidad_muerte"))

@app.route("/Nacional/Muertes_antes_de/Servicios")
def NacMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Nacional","Servicios","vida.Muertes_antes_de"))

@app.route("/Nacional/Esperanza_de_vida/Servicios")
def NacEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Nacional","Servicios","vida.Esperanza_de_vida"))

@app.route("/Nacional/Sobrevivientes/Resto")
def NacSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Nacional","Resto","vida.Sobrevivientes"))

@app.route("/Nacional/Probabilidad_Supervivencia/Resto")
def NacProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Nacional","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Nacional/Probabilidad_muerte/Resto")
def NacProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Nacional","Resto","vida.Probabilidad_muerte"))

@app.route("/Nacional/Muertes_antes_de/Resto")
def NacMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Nacional","Resto","vida.Muertes_antes_de"))

@app.route("/Nacional/Esperanza_de_vida/Resto")
def NacEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Nacional","Resto","vida.Esperanza_de_vida"))


# Nayarit

@app.route("/Nayarit/Sobrevivientes/Total")
def NaySobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Nayarit","Total","vida.Sobrevivientes"))

@app.route("/Nayarit/Probabilidad_Supervivencia/Total")
def NayProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Nayarit","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Nayarit/Probabilidad_muerte/Total")
def NayProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Nayarit","Total","vida.Probabilidad_muerte"))

@app.route("/Nayarit/Muertes_antes_de/Total")
def NayMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Nayarit","Total","vida.Muertes_antes_de"))

@app.route("/Nayarit/Esperanza_de_vida/Total")
def NayEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Nayarit","Total","vida.Esperanza_de_vida"))

@app.route("/Nayarit/Sobrevivientes/Comercio")
def NaySobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Nayarit","Comercio","vida.Sobrevivientes"))

@app.route("/Nayarit/Probabilidad_Supervivencia/Comercio")
def NayProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Nayarit","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Nayarit/Probabilidad_muerte/Comercio")
def NayProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Nayarit","Comercio","vida.Probabilidad_muerte"))

@app.route("/Nayarit/Muertes_antes_de/Comercio")
def NayMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Nayarit","Comercio","vida.Muertes_antes_de"))

@app.route("/Nayarit/Esperanza_de_vida/Comercio")
def NayEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Nayarit","Comercio","vida.Esperanza_de_vida"))


@app.route("/Nayarit/Sobrevivientes/Manufacturas")
def NaySobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Nayarit","Manufacturas","vida.Sobrevivientes"))

@app.route("/Nayarit/Probabilidad_Supervivencia/Manufacturas")
def NayProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Nayarit","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Nayarit/Probabilidad_muerte/Manufacturas")
def NayProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Nayarit","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Nayarit/Muertes_antes_de/Manufacturas")
def NayMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Nayarit","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Nayarit/Esperanza_de_vida/Manufacturas")
def NayEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Nayarit","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Nayarit/Sobrevivientes/Servicios")
def NaySobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Nayarit","Servicios","vida.Sobrevivientes"))

@app.route("/Nayarit/Probabilidad_Supervivencia/Servicios")
def NayProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Nayarit","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Nayarit/Probabilidad_muerte/Servicios")
def NayProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Nayarit","Servicios","vida.Probabilidad_muerte"))

@app.route("/Nayarit/Muertes_antes_de/Servicios")
def NayMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Nayarit","Servicios","vida.Muertes_antes_de"))

@app.route("/Nayarit/Esperanza_de_vida/Servicios")
def NayEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Nayarit","Servicios","vida.Esperanza_de_vida"))

@app.route("/Nayarit/Sobrevivientes/Resto")
def NaySobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Nayarit","Resto","vida.Sobrevivientes"))

@app.route("/Nayarit/Probabilidad_Supervivencia/Resto")
def NayProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Nayarit","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Nayarit/Probabilidad_muerte/Resto")
def NayProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Nayarit","Resto","vida.Probabilidad_muerte"))

@app.route("/Nayarit/Muertes_antes_de/Resto")
def NayMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Nayarit","Resto","vida.Muertes_antes_de"))

@app.route("/Nayarit/Esperanza_de_vida/Resto")
def NayEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Nayarit","Resto","vida.Esperanza_de_vida"))

# Nuevo Leon

@app.route("/NuevoLeon/Sobrevivientes/Total")
def NueSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("NuevoLeon","Total","vida.Sobrevivientes"))

@app.route("/NuevoLeon/Probabilidad_Supervivencia/Total")
def NueProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("NuevoLeon","Total","vida.Probabilidad_Supervivencia"))

@app.route("/NuevoLeon/Probabilidad_muerte/Total")
def NueProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("NuevoLeon","Total","vida.Probabilidad_muerte"))

@app.route("/NuevoLeon/Muertes_antes_de/Total")
def NueMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("NuevoLeon","Total","vida.Muertes_antes_de"))

@app.route("/NuevoLeon/Esperanza_de_vida/Total")
def NueEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("NuevoLeon","Total","vida.Esperanza_de_vida"))

@app.route("/NuevoLeon/Sobrevivientes/Comercio")
def NueSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("NuevoLeon","Comercio","vida.Sobrevivientes"))

@app.route("/NuevoLeon/Probabilidad_Supervivencia/Comercio")
def NueProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("NuevoLeon","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/NuevoLeon/Probabilidad_muerte/Comercio")
def NueProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("NuevoLeon","Comercio","vida.Probabilidad_muerte"))

@app.route("/NuevoLeon/Muertes_antes_de/Comercio")
def NueMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("NuevoLeon","Comercio","vida.Muertes_antes_de"))

@app.route("/NuevoLeon/Esperanza_de_vida/Comercio")
def NueEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("NuevoLeon","Comercio","vida.Esperanza_de_vida"))


@app.route("/NuevoLeon/Sobrevivientes/Manufacturas")
def NueSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("NuevoLeon","Manufacturas","vida.Sobrevivientes"))

@app.route("/NuevoLeon/Probabilidad_Supervivencia/Manufacturas")
def NueProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("NuevoLeon","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/NuevoLeon/Probabilidad_muerte/Manufacturas")
def NueProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("NuevoLeon","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/NuevoLeon/Muertes_antes_de/Manufacturas")
def NueMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("NuevoLeon","Manufacturas","vida.Muertes_antes_de"))

@app.route("/NuevoLeon/Esperanza_de_vida/Manufacturas")
def NueEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("NuevoLeon","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/NuevoLeon/Sobrevivientes/Servicios")
def NueSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("NuevoLeon","Servicios","vida.Sobrevivientes"))

@app.route("/NuevoLeon/Probabilidad_Supervivencia/Servicios")
def NueProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("NuevoLeon","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/NuevoLeon/Probabilidad_muerte/Servicios")
def NueProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("NuevoLeon","Servicios","vida.Probabilidad_muerte"))

@app.route("/NuevoLeon/Muertes_antes_de/Servicios")
def NueMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("NuevoLeon","Servicios","vida.Muertes_antes_de"))

@app.route("/NuevoLeon/Esperanza_de_vida/Servicios")
def NueEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("NuevoLeon","Servicios","vida.Esperanza_de_vida"))

@app.route("/NuevoLeon/Sobrevivientes/Resto")
def NueSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("NuevoLeon","Resto","vida.Sobrevivientes"))

@app.route("/NuevoLeon/Probabilidad_Supervivencia/Resto")
def NueProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("NuevoLeon","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/NuevoLeon/Probabilidad_muerte/Resto")
def NueProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("NuevoLeon","Resto","vida.Probabilidad_muerte"))

@app.route("/NuevoLeon/Muertes_antes_de/Resto")
def NueMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("NuevoLeon","Resto","vida.Muertes_antes_de"))

@app.route("/NuevoLeon/Esperanza_de_vida/Resto")
def NueEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("NuevoLeon","Resto","vida.Esperanza_de_vida"))

# Oaxaca

@app.route("/Oaxaca/Sobrevivientes/Total")
def OaxSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Oaxaca","Total","vida.Sobrevivientes"))

@app.route("/Oaxaca/Probabilidad_Supervivencia/Total")
def OaxProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Oaxaca","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Oaxaca/Probabilidad_muerte/Total")
def OaxProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Oaxaca","Total","vida.Probabilidad_muerte"))

@app.route("/Oaxaca/Muertes_antes_de/Total")
def OaxMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Oaxaca","Total","vida.Muertes_antes_de"))

@app.route("/Oaxaca/Esperanza_de_vida/Total")
def OaxEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Oaxaca","Total","vida.Esperanza_de_vida"))

@app.route("/Oaxaca/Sobrevivientes/Comercio")
def OaxSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Oaxaca","Comercio","vida.Sobrevivientes"))

@app.route("/Oaxaca/Probabilidad_Supervivencia/Comercio")
def OaxProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Oaxaca","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Oaxaca/Probabilidad_muerte/Comercio")
def OaxProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Oaxaca","Comercio","vida.Probabilidad_muerte"))

@app.route("/Oaxaca/Muertes_antes_de/Comercio")
def OaxMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Oaxaca","Comercio","vida.Muertes_antes_de"))

@app.route("/Oaxaca/Esperanza_de_vida/Comercio")
def OaxEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Oaxaca","Comercio","vida.Esperanza_de_vida"))


@app.route("/Oaxaca/Sobrevivientes/Manufacturas")
def OaxSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Oaxaca","Manufacturas","vida.Sobrevivientes"))

@app.route("/Oaxaca/Probabilidad_Supervivencia/Manufacturas")
def OaxProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Oaxaca","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Oaxaca/Probabilidad_muerte/Manufacturas")
def OaxProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Oaxaca","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Oaxaca/Muertes_antes_de/Manufacturas")
def OaxMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Oaxaca","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Oaxaca/Esperanza_de_vida/Manufacturas")
def OaxEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Oaxaca","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Oaxaca/Sobrevivientes/Servicios")
def OaxSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Oaxaca","Servicios","vida.Sobrevivientes"))

@app.route("/Oaxaca/Probabilidad_Supervivencia/Servicios")
def OaxProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Oaxaca","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Oaxaca/Probabilidad_muerte/Servicios")
def OaxProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Oaxaca","Servicios","vida.Probabilidad_muerte"))

@app.route("/Oaxaca/Muertes_antes_de/Servicios")
def OaxMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Oaxaca","Servicios","vida.Muertes_antes_de"))

@app.route("/Oaxaca/Esperanza_de_vida/Servicios")
def OaxEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Oaxaca","Servicios","vida.Esperanza_de_vida"))

@app.route("/Oaxaca/Sobrevivientes/Resto")
def OaxSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Oaxaca","Resto","vida.Sobrevivientes"))

@app.route("/Oaxaca/Probabilidad_Supervivencia/Resto")
def OaxProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Oaxaca","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Oaxaca/Probabilidad_muerte/Resto")
def OaxProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Oaxaca","Resto","vida.Probabilidad_muerte"))

@app.route("/Oaxaca/Muertes_antes_de/Resto")
def OaxMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Oaxaca","Resto","vida.Muertes_antes_de"))

@app.route("/Oaxaca/Esperanza_de_vida/Resto")
def OaxEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Oaxaca","Resto","vida.Esperanza_de_vida"))

# Puebla

@app.route("/Puebla/Sobrevivientes/Total")
def PueSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Puebla","Total","vida.Sobrevivientes"))

@app.route("/Puebla/Probabilidad_Supervivencia/Total")
def PueProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Puebla","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Puebla/Probabilidad_muerte/Total")
def PueProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Puebla","Total","vida.Probabilidad_muerte"))

@app.route("/Puebla/Muertes_antes_de/Total")
def PueMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Puebla","Total","vida.Muertes_antes_de"))

@app.route("/Puebla/Esperanza_de_vida/Total")
def PueEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Puebla","Total","vida.Esperanza_de_vida"))

@app.route("/Puebla/Sobrevivientes/Comercio")
def PueSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Puebla","Comercio","vida.Sobrevivientes"))

@app.route("/Puebla/Probabilidad_Supervivencia/Comercio")
def PueProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Puebla","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Puebla/Probabilidad_muerte/Comercio")
def PueProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Puebla","Comercio","vida.Probabilidad_muerte"))

@app.route("/Puebla/Muertes_antes_de/Comercio")
def PueMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Puebla","Comercio","vida.Muertes_antes_de"))

@app.route("/Puebla/Esperanza_de_vida/Comercio")
def PueEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Puebla","Comercio","vida.Esperanza_de_vida"))


@app.route("/Puebla/Sobrevivientes/Manufacturas")
def PueSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Puebla","Manufacturas","vida.Sobrevivientes"))

@app.route("/Puebla/Probabilidad_Supervivencia/Manufacturas")
def PueProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Puebla","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Puebla/Probabilidad_muerte/Manufacturas")
def PueProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Puebla","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Puebla/Muertes_antes_de/Manufacturas")
def PueMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Puebla","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Puebla/Esperanza_de_vida/Manufacturas")
def PueEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Puebla","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Puebla/Sobrevivientes/Servicios")
def PueSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Puebla","Servicios","vida.Sobrevivientes"))

@app.route("/Puebla/Probabilidad_Supervivencia/Servicios")
def PueProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Puebla","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Puebla/Probabilidad_muerte/Servicios")
def PueProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Puebla","Servicios","vida.Probabilidad_muerte"))

@app.route("/Puebla/Muertes_antes_de/Servicios")
def PueMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Puebla","Servicios","vida.Muertes_antes_de"))

@app.route("/Puebla/Esperanza_de_vida/Servicios")
def PueEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Puebla","Servicios","vida.Esperanza_de_vida"))

@app.route("/Puebla/Sobrevivientes/Resto")
def PueSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Puebla","Resto","vida.Sobrevivientes"))

@app.route("/Puebla/Probabilidad_Supervivencia/Resto")
def PueProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Puebla","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Puebla/Probabilidad_muerte/Resto")
def PueProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Puebla","Resto","vida.Probabilidad_muerte"))

@app.route("/Puebla/Muertes_antes_de/Resto")
def PueMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Puebla","Resto","vida.Muertes_antes_de"))

@app.route("/Puebla/Esperanza_de_vida/Resto")
def PueEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Puebla","Resto","vida.Esperanza_de_vida"))

# Queretaro

@app.route("/Queretaro/Sobrevivientes/Total")
def QueSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Queretaro","Total","vida.Sobrevivientes"))

@app.route("/Queretaro/Probabilidad_Supervivencia/Total")
def QueProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Queretaro","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Queretaro/Probabilidad_muerte/Total")
def QueProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Queretaro","Total","vida.Probabilidad_muerte"))

@app.route("/Queretaro/Muertes_antes_de/Total")
def QueMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Queretaro","Total","vida.Muertes_antes_de"))

@app.route("/Queretaro/Esperanza_de_vida/Total")
def QueEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Queretaro","Total","vida.Esperanza_de_vida"))

@app.route("/Queretaro/Sobrevivientes/Comercio")
def QueSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Queretaro","Comercio","vida.Sobrevivientes"))

@app.route("/Queretaro/Probabilidad_Supervivencia/Comercio")
def QueProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Queretaro","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Queretaro/Probabilidad_muerte/Comercio")
def QueProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Queretaro","Comercio","vida.Probabilidad_muerte"))

@app.route("/Queretaro/Muertes_antes_de/Comercio")
def QueMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Queretaro","Comercio","vida.Muertes_antes_de"))

@app.route("/Queretaro/Esperanza_de_vida/Comercio")
def QueEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Queretaro","Comercio","vida.Esperanza_de_vida"))


@app.route("/Queretaro/Sobrevivientes/Manufacturas")
def QueSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Queretaro","Manufacturas","vida.Sobrevivientes"))

@app.route("/Queretaro/Probabilidad_Supervivencia/Manufacturas")
def QueProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Queretaro","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Queretaro/Probabilidad_muerte/Manufacturas")
def QueProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Queretaro","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Queretaro/Muertes_antes_de/Manufacturas")
def QueMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Queretaro","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Queretaro/Esperanza_de_vida/Manufacturas")
def QueEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Queretaro","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Queretaro/Sobrevivientes/Servicios")
def QueSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Queretaro","Servicios","vida.Sobrevivientes"))

@app.route("/Queretaro/Probabilidad_Supervivencia/Servicios")
def QueProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Queretaro","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Queretaro/Probabilidad_muerte/Servicios")
def QueProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Queretaro","Servicios","vida.Probabilidad_muerte"))

@app.route("/Queretaro/Muertes_antes_de/Servicios")
def QueMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Queretaro","Servicios","vida.Muertes_antes_de"))

@app.route("/Queretaro/Esperanza_de_vida/Servicios")
def QueEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Queretaro","Servicios","vida.Esperanza_de_vida"))

@app.route("/Queretaro/Sobrevivientes/Resto")
def QueSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Queretaro","Resto","vida.Sobrevivientes"))

@app.route("/Queretaro/Probabilidad_Supervivencia/Resto")
def QueProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Queretaro","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Queretaro/Probabilidad_muerte/Resto")
def QueProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Queretaro","Resto","vida.Probabilidad_muerte"))

@app.route("/Queretaro/Muertes_antes_de/Resto")
def QueMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Queretaro","Resto","vida.Muertes_antes_de"))

@app.route("/Queretaro/Esperanza_de_vida/Resto")
def QueEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Queretaro","Resto","vida.Esperanza_de_vida"))

# Quintana Roo

@app.route("/QuintanaRoo/Sobrevivientes/Total")
def QuiSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("QuintanaRoo","Total","vida.Sobrevivientes"))

@app.route("/QuintanaRoo/Probabilidad_Supervivencia/Total")
def QuiProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("QuintanaRoo","Total","vida.Probabilidad_Supervivencia"))

@app.route("/QuintanaRoo/Probabilidad_muerte/Total")
def QuiProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("QuintanaRoo","Total","vida.Probabilidad_muerte"))

@app.route("/QuintanaRoo/Muertes_antes_de/Total")
def QuiMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("QuintanaRoo","Total","vida.Muertes_antes_de"))

@app.route("/QuintanaRoo/Esperanza_de_vida/Total")
def QuiEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("QuintanaRoo","Total","vida.Esperanza_de_vida"))

@app.route("/QuintanaRoo/Sobrevivientes/Comercio")
def QuiSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("QuintanaRoo","Comercio","vida.Sobrevivientes"))

@app.route("/QuintanaRoo/Probabilidad_Supervivencia/Comercio")
def QuiProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("QuintanaRoo","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/QuintanaRoo/Probabilidad_muerte/Comercio")
def QuiProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("QuintanaRoo","Comercio","vida.Probabilidad_muerte"))

@app.route("/QuintanaRoo/Muertes_antes_de/Comercio")
def QuiMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("QuintanaRoo","Comercio","vida.Muertes_antes_de"))

@app.route("/QuintanaRoo/Esperanza_de_vida/Comercio")
def QuiEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("QuintanaRoo","Comercio","vida.Esperanza_de_vida"))


@app.route("/QuintanaRoo/Sobrevivientes/Manufacturas")
def QuiSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("QuintanaRoo","Manufacturas","vida.Sobrevivientes"))

@app.route("/QuintanaRoo/Probabilidad_Supervivencia/Manufacturas")
def QuiProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("QuintanaRoo","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/QuintanaRoo/Probabilidad_muerte/Manufacturas")
def QuiProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("QuintanaRoo","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/QuintanaRoo/Muertes_antes_de/Manufacturas")
def QuiMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("QuintanaRoo","Manufacturas","vida.Muertes_antes_de"))

@app.route("/QuintanaRoo/Esperanza_de_vida/Manufacturas")
def QuiEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("QuintanaRoo","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/QuintanaRoo/Sobrevivientes/Servicios")
def QuiSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("QuintanaRoo","Servicios","vida.Sobrevivientes"))

@app.route("/QuintanaRoo/Probabilidad_Supervivencia/Servicios")
def QuiProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("QuintanaRoo","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/QuintanaRoo/Probabilidad_muerte/Servicios")
def QuiProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("QuintanaRoo","Servicios","vida.Probabilidad_muerte"))

@app.route("/QuintanaRoo/Muertes_antes_de/Servicios")
def QuiMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("QuintanaRoo","Servicios","vida.Muertes_antes_de"))

@app.route("/QuintanaRoo/Esperanza_de_vida/Servicios")
def QuiEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("QuintanaRoo","Servicios","vida.Esperanza_de_vida"))

@app.route("/QuintanaRoo/Sobrevivientes/Resto")
def QuiSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("QuintanaRoo","Resto","vida.Sobrevivientes"))

@app.route("/QuintanaRoo/Probabilidad_Supervivencia/Resto")
def QuiProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("QuintanaRoo","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/QuintanaRoo/Probabilidad_muerte/Resto")
def QuiProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("QuintanaRoo","Resto","vida.Probabilidad_muerte"))

@app.route("/QuintanaRoo/Muertes_antes_de/Resto")
def QuiMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("QuintanaRoo","Resto","vida.Muertes_antes_de"))

@app.route("/QuintanaRoo/Esperanza_de_vida/Resto")
def QuiEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("QuintanaRoo","Resto","vida.Esperanza_de_vida"))


# Sinaloa

@app.route("/Sinaloa/Sobrevivientes/Total")
def SinSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Sinaloa","Total","vida.Sobrevivientes"))

@app.route("/Sinaloa/Probabilidad_Supervivencia/Total")
def SinProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Sinaloa","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Sinaloa/Probabilidad_muerte/Total")
def SinProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Sinaloa","Total","vida.Probabilidad_muerte"))

@app.route("/Sinaloa/Muertes_antes_de/Total")
def SinMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Sinaloa","Total","vida.Muertes_antes_de"))

@app.route("/Sinaloa/Esperanza_de_vida/Total")
def SinEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Sinaloa","Total","vida.Esperanza_de_vida"))

@app.route("/Sinaloa/Sobrevivientes/Comercio")
def SinSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Sinaloa","Comercio","vida.Sobrevivientes"))

@app.route("/Sinaloa/Probabilidad_Supervivencia/Comercio")
def SinProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Sinaloa","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Sinaloa/Probabilidad_muerte/Comercio")
def SinProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Sinaloa","Comercio","vida.Probabilidad_muerte"))

@app.route("/Sinaloa/Muertes_antes_de/Comercio")
def SinMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Sinaloa","Comercio","vida.Muertes_antes_de"))

@app.route("/Sinaloa/Esperanza_de_vida/Comercio")
def SinEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Sinaloa","Comercio","vida.Esperanza_de_vida"))


@app.route("/Sinaloa/Sobrevivientes/Manufacturas")
def SinSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Sinaloa","Manufacturas","vida.Sobrevivientes"))

@app.route("/Sinaloa/Probabilidad_Supervivencia/Manufacturas")
def SinProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Sinaloa","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Sinaloa/Probabilidad_muerte/Manufacturas")
def SinProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Sinaloa","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Sinaloa/Muertes_antes_de/Manufacturas")
def SinMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Sinaloa","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Sinaloa/Esperanza_de_vida/Manufacturas")
def SinEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Sinaloa","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Sinaloa/Sobrevivientes/Servicios")
def SinSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Sinaloa","Servicios","vida.Sobrevivientes"))

@app.route("/Sinaloa/Probabilidad_Supervivencia/Servicios")
def SinProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Sinaloa","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Sinaloa/Probabilidad_muerte/Servicios")
def SinProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Sinaloa","Servicios","vida.Probabilidad_muerte"))

@app.route("/Sinaloa/Muertes_antes_de/Servicios")
def SinMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Sinaloa","Servicios","vida.Muertes_antes_de"))

@app.route("/Sinaloa/Esperanza_de_vida/Servicios")
def SinEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Sinaloa","Servicios","vida.Esperanza_de_vida"))

@app.route("/Sinaloa/Sobrevivientes/Resto")
def SinSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Sinaloa","Resto","vida.Sobrevivientes"))

@app.route("/Sinaloa/Probabilidad_Supervivencia/Resto")
def SinProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Sinaloa","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Sinaloa/Probabilidad_muerte/Resto")
def SinProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Sinaloa","Resto","vida.Probabilidad_muerte"))

@app.route("/Sinaloa/Muertes_antes_de/Resto")
def SinMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Sinaloa","Resto","vida.Muertes_antes_de"))

@app.route("/Sinaloa/Esperanza_de_vida/Resto")
def SinEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Sinaloa","Resto","vida.Esperanza_de_vida"))


# San Luis Potosi

@app.route("/SanLuisPotosi/Sobrevivientes/Total")
def SanSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("SanLuisPotosi","Total","vida.Sobrevivientes"))

@app.route("/SanLuisPotosi/Probabilidad_Supervivencia/Total")
def SanProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("SanLuisPotosi","Total","vida.Probabilidad_Supervivencia"))

@app.route("/SanLuisPotosi/Probabilidad_muerte/Total")
def SanProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("SanLuisPotosi","Total","vida.Probabilidad_muerte"))

@app.route("/SanLuisPotosi/Muertes_antes_de/Total")
def SanMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("SanLuisPotosi","Total","vida.Muertes_antes_de"))

@app.route("/SanLuisPotosi/Esperanza_de_vida/Total")
def SanEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("SanLuisPotosi","Total","vida.Esperanza_de_vida"))

@app.route("/SanLuisPotosi/Sobrevivientes/Comercio")
def SanSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("SanLuisPotosi","Comercio","vida.Sobrevivientes"))

@app.route("/SanLuisPotosi/Probabilidad_Supervivencia/Comercio")
def SanProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("SanLuisPotosi","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/SanLuisPotosi/Probabilidad_muerte/Comercio")
def SanProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("SanLuisPotosi","Comercio","vida.Probabilidad_muerte"))

@app.route("/SanLuisPotosi/Muertes_antes_de/Comercio")
def SanMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("SanLuisPotosi","Comercio","vida.Muertes_antes_de"))

@app.route("/SanLuisPotosi/Esperanza_de_vida/Comercio")
def SanEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("SanLuisPotosi","Comercio","vida.Esperanza_de_vida"))


@app.route("/SanLuisPotosi/Sobrevivientes/Manufacturas")
def SanSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("SanLuisPotosi","Manufacturas","vida.Sobrevivientes"))

@app.route("/SanLuisPotosi/Probabilidad_Supervivencia/Manufacturas")
def SanProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("SanLuisPotosi","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/SanLuisPotosi/Probabilidad_muerte/Manufacturas")
def SanProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("SanLuisPotosi","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/SanLuisPotosi/Muertes_antes_de/Manufacturas")
def SanMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("SanLuisPotosi","Manufacturas","vida.Muertes_antes_de"))

@app.route("/SanLuisPotosi/Esperanza_de_vida/Manufacturas")
def SanEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("SanLuisPotosi","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/SanLuisPotosi/Sobrevivientes/Servicios")
def SanSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("SanLuisPotosi","Servicios","vida.Sobrevivientes"))

@app.route("/SanLuisPotosi/Probabilidad_Supervivencia/Servicios")
def SanProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("SanLuisPotosi","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/SanLuisPotosi/Probabilidad_muerte/Servicios")
def SanProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("SanLuisPotosi","Servicios","vida.Probabilidad_muerte"))

@app.route("/SanLuisPotosi/Muertes_antes_de/Servicios")
def SanMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("SanLuisPotosi","Servicios","vida.Muertes_antes_de"))

@app.route("/SanLuisPotosi/Esperanza_de_vida/Servicios")
def SanEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("SanLuisPotosi","Servicios","vida.Esperanza_de_vida"))

@app.route("/SanLuisPotosi/Sobrevivientes/Resto")
def SanSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("SanLuisPotosi","Resto","vida.Sobrevivientes"))

@app.route("/SanLuisPotosi/Probabilidad_Supervivencia/Resto")
def SanProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("SanLuisPotosi","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/SanLuisPotosi/Probabilidad_muerte/Resto")
def SanProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("SanLuisPotosi","Resto","vida.Probabilidad_muerte"))

@app.route("/SanLuisPotosi/Muertes_antes_de/Resto")
def SanMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("SanLuisPotosi","Resto","vida.Muertes_antes_de"))

@app.route("/SanLuisPotosi/Esperanza_de_vida/Resto")
def SanEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("SanLuisPotosi","Resto","vida.Esperanza_de_vida"))

# Sonora

@app.route("/Sonora/Sobrevivientes/Total")
def SonSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Sonora","Total","vida.Sobrevivientes"))

@app.route("/Sonora/Probabilidad_Supervivencia/Total")
def SonProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Sonora","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Sonora/Probabilidad_muerte/Total")
def SonProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Sonora","Total","vida.Probabilidad_muerte"))

@app.route("/Sonora/Muertes_antes_de/Total")
def SonMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Sonora","Total","vida.Muertes_antes_de"))

@app.route("/Sonora/Esperanza_de_vida/Total")
def SonEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Sonora","Total","vida.Esperanza_de_vida"))

@app.route("/Sonora/Sobrevivientes/Comercio")
def SonSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Sonora","Comercio","vida.Sobrevivientes"))

@app.route("/Sonora/Probabilidad_Supervivencia/Comercio")
def SonProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Sonora","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Sonora/Probabilidad_muerte/Comercio")
def SonProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Sonora","Comercio","vida.Probabilidad_muerte"))

@app.route("/Sonora/Muertes_antes_de/Comercio")
def SonMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Sonora","Comercio","vida.Muertes_antes_de"))

@app.route("/Sonora/Esperanza_de_vida/Comercio")
def SonEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Sonora","Comercio","vida.Esperanza_de_vida"))


@app.route("/Sonora/Sobrevivientes/Manufacturas")
def SonSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Sonora","Manufacturas","vida.Sobrevivientes"))

@app.route("/Sonora/Probabilidad_Supervivencia/Manufacturas")
def SonProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Sonora","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Sonora/Probabilidad_muerte/Manufacturas")
def SonProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Sonora","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Sonora/Muertes_antes_de/Manufacturas")
def SonMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Sonora","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Sonora/Esperanza_de_vida/Manufacturas")
def SonEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Sonora","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Sonora/Sobrevivientes/Servicios")
def SonSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Sonora","Servicios","vida.Sobrevivientes"))

@app.route("/Sonora/Probabilidad_Supervivencia/Servicios")
def SonProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Sonora","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Sonora/Probabilidad_muerte/Servicios")
def SonProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Sonora","Servicios","vida.Probabilidad_muerte"))

@app.route("/Sonora/Muertes_antes_de/Servicios")
def SonMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Sonora","Servicios","vida.Muertes_antes_de"))

@app.route("/Sonora/Esperanza_de_vida/Servicios")
def SonEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Sonora","Servicios","vida.Esperanza_de_vida"))

@app.route("/Sonora/Sobrevivientes/Resto")
def SonSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Sonora","Resto","vida.Sobrevivientes"))

@app.route("/Sonora/Probabilidad_Supervivencia/Resto")
def SonProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Sonora","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Sonora/Probabilidad_muerte/Resto")
def SonProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Sonora","Resto","vida.Probabilidad_muerte"))

@app.route("/Sonora/Muertes_antes_de/Resto")
def SonMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Sonora","Resto","vida.Muertes_antes_de"))

@app.route("/Sonora/Esperanza_de_vida/Resto")
def SonEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Sonora","Resto","vida.Esperanza_de_vida"))


# Tabasco

@app.route("/Tabasco/Sobrevivientes/Total")
def TabSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Tabasco","Total","vida.Sobrevivientes"))

@app.route("/Tabasco/Probabilidad_Supervivencia/Total")
def TabProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Tabasco","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Tabasco/Probabilidad_muerte/Total")
def TabProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Tabasco","Total","vida.Probabilidad_muerte"))

@app.route("/Tabasco/Muertes_antes_de/Total")
def TabMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Tabasco","Total","vida.Muertes_antes_de"))

@app.route("/Tabasco/Esperanza_de_vida/Total")
def TabEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Tabasco","Total","vida.Esperanza_de_vida"))

@app.route("/Tabasco/Sobrevivientes/Comercio")
def TabSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Tabasco","Comercio","vida.Sobrevivientes"))

@app.route("/Tabasco/Probabilidad_Supervivencia/Comercio")
def TabProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Tabasco","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Tabasco/Probabilidad_muerte/Comercio")
def TabProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Tabasco","Comercio","vida.Probabilidad_muerte"))

@app.route("/Tabasco/Muertes_antes_de/Comercio")
def TabMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Tabasco","Comercio","vida.Muertes_antes_de"))

@app.route("/Tabasco/Esperanza_de_vida/Comercio")
def TabEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Tabasco","Comercio","vida.Esperanza_de_vida"))


@app.route("/Tabasco/Sobrevivientes/Manufacturas")
def TabSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Tabasco","Manufacturas","vida.Sobrevivientes"))

@app.route("/Tabasco/Probabilidad_Supervivencia/Manufacturas")
def TabProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Tabasco","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Tabasco/Probabilidad_muerte/Manufacturas")
def TabProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Tabasco","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Tabasco/Muertes_antes_de/Manufacturas")
def TabMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Tabasco","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Tabasco/Esperanza_de_vida/Manufacturas")
def TabEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Tabasco","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Tabasco/Sobrevivientes/Servicios")
def TabSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Tabasco","Servicios","vida.Sobrevivientes"))

@app.route("/Tabasco/Probabilidad_Supervivencia/Servicios")
def TabProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Tabasco","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Tabasco/Probabilidad_muerte/Servicios")
def TabProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Tabasco","Servicios","vida.Probabilidad_muerte"))

@app.route("/Tabasco/Muertes_antes_de/Servicios")
def TabMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Tabasco","Servicios","vida.Muertes_antes_de"))

@app.route("/Tabasco/Esperanza_de_vida/Servicios")
def TabEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Tabasco","Servicios","vida.Esperanza_de_vida"))

@app.route("/Tabasco/Sobrevivientes/Resto")
def TabSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Tabasco","Resto","vida.Sobrevivientes"))

@app.route("/Tabasco/Probabilidad_Supervivencia/Resto")
def TabProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Tabasco","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Tabasco/Probabilidad_muerte/Resto")
def TabProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Tabasco","Resto","vida.Probabilidad_muerte"))

@app.route("/Tabasco/Muertes_antes_de/Resto")
def TabMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Tabasco","Resto","vida.Muertes_antes_de"))

@app.route("/Tabasco/Esperanza_de_vida/Resto")
def TabEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Tabasco","Resto","vida.Esperanza_de_vida"))


# Tamaulipas

@app.route("/Tamaulipas/Sobrevivientes/Total")
def TamSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Tamaulipas","Total","vida.Sobrevivientes"))

@app.route("/Tamaulipas/Probabilidad_Supervivencia/Total")
def TamProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Tamaulipas","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Tamaulipas/Probabilidad_muerte/Total")
def TamProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Tamaulipas","Total","vida.Probabilidad_muerte"))

@app.route("/Tamaulipas/Muertes_antes_de/Total")
def TamMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Tamaulipas","Total","vida.Muertes_antes_de"))

@app.route("/Tamaulipas/Esperanza_de_vida/Total")
def TamEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Tamaulipas","Total","vida.Esperanza_de_vida"))

@app.route("/Tamaulipas/Sobrevivientes/Comercio")
def TamSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Tamaulipas","Comercio","vida.Sobrevivientes"))

@app.route("/Tamaulipas/Probabilidad_Supervivencia/Comercio")
def TamProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Tamaulipas","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Tamaulipas/Probabilidad_muerte/Comercio")
def TamProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Tamaulipas","Comercio","vida.Probabilidad_muerte"))

@app.route("/Tamaulipas/Muertes_antes_de/Comercio")
def TamMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Tamaulipas","Comercio","vida.Muertes_antes_de"))

@app.route("/Tamaulipas/Esperanza_de_vida/Comercio")
def TamEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Tamaulipas","Comercio","vida.Esperanza_de_vida"))


@app.route("/Tamaulipas/Sobrevivientes/Manufacturas")
def TamSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Tamaulipas","Manufacturas","vida.Sobrevivientes"))

@app.route("/Tamaulipas/Probabilidad_Supervivencia/Manufacturas")
def TamProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Tamaulipas","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Tamaulipas/Probabilidad_muerte/Manufacturas")
def TamProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Tamaulipas","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Tamaulipas/Muertes_antes_de/Manufacturas")
def TamMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Tamaulipas","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Tamaulipas/Esperanza_de_vida/Manufacturas")
def TamEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Tamaulipas","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Tamaulipas/Sobrevivientes/Servicios")
def TamSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Tamaulipas","Servicios","vida.Sobrevivientes"))

@app.route("/Tamaulipas/Probabilidad_Supervivencia/Servicios")
def TamProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Tamaulipas","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Tamaulipas/Probabilidad_muerte/Servicios")
def TamProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Tamaulipas","Servicios","vida.Probabilidad_muerte"))

@app.route("/Tamaulipas/Muertes_antes_de/Servicios")
def TamMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Tamaulipas","Servicios","vida.Muertes_antes_de"))

@app.route("/Tamaulipas/Esperanza_de_vida/Servicios")
def TamEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Tamaulipas","Servicios","vida.Esperanza_de_vida"))

@app.route("/Tamaulipas/Sobrevivientes/Resto")
def TamSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Tamaulipas","Resto","vida.Sobrevivientes"))

@app.route("/Tamaulipas/Probabilidad_Supervivencia/Resto")
def TamProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Tamaulipas","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Tamaulipas/Probabilidad_muerte/Resto")
def TamProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Tamaulipas","Resto","vida.Probabilidad_muerte"))

@app.route("/Tamaulipas/Muertes_antes_de/Resto")
def TamMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Tamaulipas","Resto","vida.Muertes_antes_de"))

@app.route("/Tamaulipas/Esperanza_de_vida/Resto")
def TamEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Tamaulipas","Resto","vida.Esperanza_de_vida"))


# Tlaxcala

@app.route("/Tlaxcala/Sobrevivientes/Total")
def TlaSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Tlaxcala","Total","vida.Sobrevivientes"))

@app.route("/Tlaxcala/Probabilidad_Supervivencia/Total")
def TlaProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Tlaxcala","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Tlaxcala/Probabilidad_muerte/Total")
def TlaProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Tlaxcala","Total","vida.Probabilidad_muerte"))

@app.route("/Tlaxcala/Muertes_antes_de/Total")
def TlaMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Tlaxcala","Total","vida.Muertes_antes_de"))

@app.route("/Tlaxcala/Esperanza_de_vida/Total")
def TlaEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Tlaxcala","Total","vida.Esperanza_de_vida"))

@app.route("/Tlaxcala/Sobrevivientes/Comercio")
def TlaSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Tlaxcala","Comercio","vida.Sobrevivientes"))

@app.route("/Tlaxcala/Probabilidad_Supervivencia/Comercio")
def TlaProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Tlaxcala","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Tlaxcala/Probabilidad_muerte/Comercio")
def TlaProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Tlaxcala","Comercio","vida.Probabilidad_muerte"))

@app.route("/Tlaxcala/Muertes_antes_de/Comercio")
def TlaMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Tlaxcala","Comercio","vida.Muertes_antes_de"))

@app.route("/Tlaxcala/Esperanza_de_vida/Comercio")
def TlaEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Tlaxcala","Comercio","vida.Esperanza_de_vida"))


@app.route("/Tlaxcala/Sobrevivientes/Manufacturas")
def TlaSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Tlaxcala","Manufacturas","vida.Sobrevivientes"))

@app.route("/Tlaxcala/Probabilidad_Supervivencia/Manufacturas")
def TlaProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Tlaxcala","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Tlaxcala/Probabilidad_muerte/Manufacturas")
def TlaProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Tlaxcala","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Tlaxcala/Muertes_antes_de/Manufacturas")
def TlaMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Tlaxcala","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Tlaxcala/Esperanza_de_vida/Manufacturas")
def TlaEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Tlaxcala","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Tlaxcala/Sobrevivientes/Servicios")
def TlaSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Tlaxcala","Servicios","vida.Sobrevivientes"))

@app.route("/Tlaxcala/Probabilidad_Supervivencia/Servicios")
def TlaProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Tlaxcala","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Tlaxcala/Probabilidad_muerte/Servicios")
def TlaProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Tlaxcala","Servicios","vida.Probabilidad_muerte"))

@app.route("/Tlaxcala/Muertes_antes_de/Servicios")
def TlaMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Tlaxcala","Servicios","vida.Muertes_antes_de"))

@app.route("/Tlaxcala/Esperanza_de_vida/Servicios")
def TlaEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Tlaxcala","Servicios","vida.Esperanza_de_vida"))

@app.route("/Tlaxcala/Sobrevivientes/Resto")
def TlaSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Tlaxcala","Resto","vida.Sobrevivientes"))

@app.route("/Tlaxcala/Probabilidad_Supervivencia/Resto")
def TlaProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Tlaxcala","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Tlaxcala/Probabilidad_muerte/Resto")
def TlaProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Tlaxcala","Resto","vida.Probabilidad_muerte"))

@app.route("/Tlaxcala/Muertes_antes_de/Resto")
def TlaMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Tlaxcala","Resto","vida.Muertes_antes_de"))

@app.route("/Tlaxcala/Esperanza_de_vida/Resto")
def TlaEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Tlaxcala","Resto","vida.Esperanza_de_vida"))

# Veracruz

@app.route("/Veracruz/Sobrevivientes/Total")
def VerSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Veracruz","Total","vida.Sobrevivientes"))

@app.route("/Veracruz/Probabilidad_Supervivencia/Total")
def VerProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Veracruz","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Veracruz/Probabilidad_muerte/Total")
def VerProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Veracruz","Total","vida.Probabilidad_muerte"))

@app.route("/Veracruz/Muertes_antes_de/Total")
def VerMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Veracruz","Total","vida.Muertes_antes_de"))

@app.route("/Veracruz/Esperanza_de_vida/Total")
def VerEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Veracruz","Total","vida.Esperanza_de_vida"))

@app.route("/Veracruz/Sobrevivientes/Comercio")
def VerSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Veracruz","Comercio","vida.Sobrevivientes"))

@app.route("/Veracruz/Probabilidad_Supervivencia/Comercio")
def VerProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Veracruz","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Veracruz/Probabilidad_muerte/Comercio")
def VerProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Veracruz","Comercio","vida.Probabilidad_muerte"))

@app.route("/Veracruz/Muertes_antes_de/Comercio")
def VerMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Veracruz","Comercio","vida.Muertes_antes_de"))

@app.route("/Veracruz/Esperanza_de_vida/Comercio")
def VerEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Veracruz","Comercio","vida.Esperanza_de_vida"))


@app.route("/Veracruz/Sobrevivientes/Manufacturas")
def VerSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Veracruz","Manufacturas","vida.Sobrevivientes"))

@app.route("/Veracruz/Probabilidad_Supervivencia/Manufacturas")
def VerProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Veracruz","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Veracruz/Probabilidad_muerte/Manufacturas")
def VerProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Veracruz","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Veracruz/Muertes_antes_de/Manufacturas")
def VerMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Veracruz","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Veracruz/Esperanza_de_vida/Manufacturas")
def VerEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Veracruz","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Veracruz/Sobrevivientes/Servicios")
def VerSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Veracruz","Servicios","vida.Sobrevivientes"))

@app.route("/Veracruz/Probabilidad_Supervivencia/Servicios")
def VerProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Veracruz","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Veracruz/Probabilidad_muerte/Servicios")
def VerProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Veracruz","Servicios","vida.Probabilidad_muerte"))

@app.route("/Veracruz/Muertes_antes_de/Servicios")
def VerMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Veracruz","Servicios","vida.Muertes_antes_de"))

@app.route("/Veracruz/Esperanza_de_vida/Servicios")
def VerEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Veracruz","Servicios","vida.Esperanza_de_vida"))

@app.route("/Veracruz/Sobrevivientes/Resto")
def VerSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Veracruz","Resto","vida.Sobrevivientes"))

@app.route("/Veracruz/Probabilidad_Supervivencia/Resto")
def VerProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Veracruz","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Veracruz/Probabilidad_muerte/Resto")
def VerProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Veracruz","Resto","vida.Probabilidad_muerte"))

@app.route("/Veracruz/Muertes_antes_de/Resto")
def VerMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Veracruz","Resto","vida.Muertes_antes_de"))

@app.route("/Veracruz/Esperanza_de_vida/Resto")
def VerEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Veracruz","Resto","vida.Esperanza_de_vida"))

# Yucatan

@app.route("/Yucatan/Sobrevivientes/Total")
def YucSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Yucatan","Total","vida.Sobrevivientes"))

@app.route("/Yucatan/Probabilidad_Supervivencia/Total")
def YucProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Yucatan","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Yucatan/Probabilidad_muerte/Total")
def YucProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Yucatan","Total","vida.Probabilidad_muerte"))

@app.route("/Yucatan/Muertes_antes_de/Total")
def YucMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Yucatan","Total","vida.Muertes_antes_de"))

@app.route("/Yucatan/Esperanza_de_vida/Total")
def YucEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Yucatan","Total","vida.Esperanza_de_vida"))

@app.route("/Yucatan/Sobrevivientes/Comercio")
def YucSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Yucatan","Comercio","vida.Sobrevivientes"))

@app.route("/Yucatan/Probabilidad_Supervivencia/Comercio")
def YucProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Yucatan","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Yucatan/Probabilidad_muerte/Comercio")
def YucProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Yucatan","Comercio","vida.Probabilidad_muerte"))

@app.route("/Yucatan/Muertes_antes_de/Comercio")
def YucMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Yucatan","Comercio","vida.Muertes_antes_de"))

@app.route("/Yucatan/Esperanza_de_vida/Comercio")
def YucEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Yucatan","Comercio","vida.Esperanza_de_vida"))


@app.route("/Yucatan/Sobrevivientes/Manufacturas")
def YucSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Yucatan","Manufacturas","vida.Sobrevivientes"))

@app.route("/Yucatan/Probabilidad_Supervivencia/Manufacturas")
def YucProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Yucatan","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Yucatan/Probabilidad_muerte/Manufacturas")
def YucProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Yucatan","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Yucatan/Muertes_antes_de/Manufacturas")
def YucMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Yucatan","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Yucatan/Esperanza_de_vida/Manufacturas")
def YucEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Yucatan","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Yucatan/Sobrevivientes/Servicios")
def YucSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Yucatan","Servicios","vida.Sobrevivientes"))

@app.route("/Yucatan/Probabilidad_Supervivencia/Servicios")
def YucProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Yucatan","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Yucatan/Probabilidad_muerte/Servicios")
def YucProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Yucatan","Servicios","vida.Probabilidad_muerte"))

@app.route("/Yucatan/Muertes_antes_de/Servicios")
def YucMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Yucatan","Servicios","vida.Muertes_antes_de"))

@app.route("/Yucatan/Esperanza_de_vida/Servicios")
def YucEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Yucatan","Servicios","vida.Esperanza_de_vida"))

@app.route("/Yucatan/Sobrevivientes/Resto")
def YucSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Yucatan","Resto","vida.Sobrevivientes"))

@app.route("/Yucatan/Probabilidad_Supervivencia/Resto")
def YucProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Yucatan","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Yucatan/Probabilidad_muerte/Resto")
def YucProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Yucatan","Resto","vida.Probabilidad_muerte"))

@app.route("/Yucatan/Muertes_antes_de/Resto")
def YucMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Yucatan","Resto","vida.Muertes_antes_de"))

@app.route("/Yucatan/Esperanza_de_vida/Resto")
def YucEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Yucatan","Resto","vida.Esperanza_de_vida"))

# Zacatecas

@app.route("/Zacatecas/Sobrevivientes/Total")
def ZacSobrevivientesTotal():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Zacatecas","Total","vida.Sobrevivientes"))

@app.route("/Zacatecas/Probabilidad_Supervivencia/Total")
def ZacProbabilidadSupervivenciaTotal():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Zacatecas","Total","vida.Probabilidad_Supervivencia"))

@app.route("/Zacatecas/Probabilidad_muerte/Total")
def ZacProbabilidadMuerteTotal():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Zacatecas","Total","vida.Probabilidad_muerte"))

@app.route("/Zacatecas/Muertes_antes_de/Total")
def ZacMuertesAntesDeTotal():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Zacatecas","Total","vida.Muertes_antes_de"))

@app.route("/Zacatecas/Esperanza_de_vida/Total")
def ZacEsperanzaDeVidaTotal():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Zacatecas","Total","vida.Esperanza_de_vida"))

@app.route("/Zacatecas/Sobrevivientes/Comercio")
def ZacSobrevivientesComercio():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Zacatecas","Comercio","vida.Sobrevivientes"))

@app.route("/Zacatecas/Probabilidad_Supervivencia/Comercio")
def ZacProbabilidadSupervivenciaComercio():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Zacatecas","Comercio","vida.Probabilidad_Supervivencia"))

@app.route("/Zacatecas/Probabilidad_muerte/Comercio")
def ZacProbabilidadMuerteComercio():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Zacatecas","Comercio","vida.Probabilidad_muerte"))

@app.route("/Zacatecas/Muertes_antes_de/Comercio")
def ZacMuertesAntesDeComercio():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Zacatecas","Comercio","vida.Muertes_antes_de"))

@app.route("/Zacatecas/Esperanza_de_vida/Comercio")
def ZacEsperanzaDeVidaComercio():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Zacatecas","Comercio","vida.Esperanza_de_vida"))


@app.route("/Zacatecas/Sobrevivientes/Manufacturas")
def ZacSobrevivientesManufacturas():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Zacatecas","Manufacturas","vida.Sobrevivientes"))

@app.route("/Zacatecas/Probabilidad_Supervivencia/Manufacturas")
def ZacProbabilidadSupervivenciaManufacturas():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Zacatecas","Manufacturas","vida.Probabilidad_Supervivencia"))

@app.route("/Zacatecas/Probabilidad_muerte/Manufacturas")
def ZacProbabilidadMuerteManufacturas():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Zacatecas","Manufacturas","vida.Probabilidad_muerte"))

@app.route("/Zacatecas/Muertes_antes_de/Manufacturas")
def ZacMuertesAntesDeManufacturas():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Zacatecas","Manufacturas","vida.Muertes_antes_de"))

@app.route("/Zacatecas/Esperanza_de_vida/Manufacturas")
def ZacEsperanzaDeVidaManufacturas():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Zacatecas","Manufacturas","vida.Esperanza_de_vida"))


@app.route("/Zacatecas/Sobrevivientes/Servicios")
def ZacSobrevivientesServicios():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Zacatecas","Servicios","vida.Sobrevivientes"))

@app.route("/Zacatecas/Probabilidad_Supervivencia/Servicios")
def ZacProbabilidadSupervivenciaServicios():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Zacatecas","Servicios","vida.Probabilidad_Supervivencia"))

@app.route("/Zacatecas/Probabilidad_muerte/Servicios")
def ZacProbabilidadMuerteServicios():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Zacatecas","Servicios","vida.Probabilidad_muerte"))

@app.route("/Zacatecas/Muertes_antes_de/Servicios")
def ZacMuertesAntesDeServicios():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Zacatecas","Servicios","vida.Muertes_antes_de"))

@app.route("/Zacatecas/Esperanza_de_vida/Servicios")
def ZacEsperanzaDeVidaServicios():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Zacatecas","Servicios","vida.Esperanza_de_vida"))

@app.route("/Zacatecas/Sobrevivientes/Resto")
def ZacSobrevivientesResto():
    #Regresa la cantidad de empresas sobrevivientes del sector"""
    return jsonify(resultadoQuery("Zacatecas","Resto","vida.Sobrevivientes"))

@app.route("/Zacatecas/Probabilidad_Supervivencia/Resto")
def ZacProbabilidadSupervivenciaResto():
    #Regresa la probabilidad de supervivencia en diferentes años"""
    return jsonify(resultadoQuery("Zacatecas","Resto","vida.Probabilidad_Supervivencia"))

@app.route("/Zacatecas/Probabilidad_muerte/Resto")
def ZacProbabilidadMuerteResto():
    #Regresa la probabilidad de muerte en diferentes años"""
    return jsonify(resultadoQuery("Zacatecas","Resto","vida.Probabilidad_muerte"))

@app.route("/Zacatecas/Muertes_antes_de/Resto")
def ZacMuertesAntesDeResto():
    #Regresa la cantidad de muertes antes de cumplir cierto año"""
    return jsonify(resultadoQuery("Zacatecas","Resto","vida.Muertes_antes_de"))

@app.route("/Zacatecas/Esperanza_de_vida/Resto")
def ZacEsperanzaDeVidaResto():
    #Regresa la esperanza de vida de una empresa en diferentes años"""
    return jsonify(resultadoQuery("Zacatecas","Resto","vida.Esperanza_de_vida"))




if __name__ == '__main__':
    app.run(debug=True)
