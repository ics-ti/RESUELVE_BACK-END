from django.shortcuts import render

# Creacion de Vista
from django.http import JsonResponse
import json


#Clase Niveles para indicar niveles que procesara el JSON
class Niveles:
    def __init__(self):
        self.A=5
        self.B=10
        self.C=15
        self.CUAUH=20
        self.GLOBAL=50

#Clase Jugador para abstraer y manipular la informacion de un jugador
class Jugador:
    def __init__(self, jsonBody):
        self.nombre=jsonBody['nombre']
        self.nivel=jsonBody['nivel']
        self.goles=jsonBody['goles']
        self.sueldo=jsonBody['sueldo']
        self.bono=jsonBody['bono']
        self.sueldo_completo=jsonBody['sueldo_completo']
        self.equipo=jsonBody['equipo']

#Clase PRocesa se encarga de la operacion y procesamiento de la informacion
class Procesa:
    def __init__(self, objJson):
        jsonData=objJson
        self.objJugador=Jugador(jsonData)

#Metodo para identificar el nivel a partir de la abstraccion de la clase Niveles
    def nivel(self,strNivel):
        switcher=json.loads(json.dumps(Niveles().__dict__))
        return switcher.get(str(strNivel).upper(),'NIVEL NO VALIDO')

#Metodo que calcula nivel goles por jugador, por equipo y el sueldo total por jugador con base en los datos de niveles, sueldo y bono
    def calculo(self,nivelGlobal=None):
        if nivelGlobal is None:
            return round(float(self.objJugador.goles/self.nivel(self.objJugador.nivel)),3)
        else:
            porcIndividual=round(float(self.objJugador.sueldo_completo),3)
            porcEquipo=round(float(nivelGlobal),3)/round(float(Niveles().GLOBAL),3)
            porcGlobal=round((porcIndividual+porcEquipo)/2,3)
            sueldoTotal=(round(float(self.objJugador.bono),3)*porcGlobal)+round(float(self.objJugador.sueldo),3)
            return sueldoTotal

#Metodo que interpreta las peticiones HTTP, controla petciones GET y POST
#Para el GET se regresa el JSON {"jugadores":["SIN DATOS"]}

'''
Para el POST lee JSON {"jugadores"}

Este metodo controla JSON mal formado

metodo GET y metodo POST
'''
def index(request):
    nivelGlobal=0
    if request.method=='POST':
        try:
            jsonData=json.loads(request.body)
            for idxJson in jsonData['jugadores']:
                objNew=Procesa(idxJson)
                idxJson['nivel']=str(float(objNew.nivel(objNew.objJugador.nivel)))
                idxJson['sueldo_completo']=str(float(objNew.calculo()))
                nivelGlobal+=round(float(idxJson['goles']),3)

            for idxJson1 in jsonData['jugadores']:
                objNew1=Procesa(idxJson1)
                idxJson1['sueldo_completo']=str(objNew1.calculo(nivelGlobal))
            responseData=jsonData
        except Exception as ex:
            responseData={"jugadores":["MAL FORMADO"]}
    else:
        responseData={"jugadores":["SIN DATOS"]}
    return JsonResponse(responseData)