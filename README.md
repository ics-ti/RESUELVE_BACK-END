# RESUELVE_BACK-END
SUELDO FIJO					50%
-------------------------------------------------------------------------------------------------------------------------------------------------------
SUELDO VARIABLE				50%

    GOLES INDIVIDUALES		25%
    
            Jugador		Nivel	Goles anotados en el mes/mínimo requerido		% individual de goles		% alcanzado por equipo		% final del bono (PROMEDIO GOLES INDIVIDUALES 25% + GOLES POR   EQUIPO 25%)
    
		Juan                                   A                                                    06/05                      120                                      096                      108.00
    
		Pedro                                  B                                                    07/10                      070                                      096                      83.00
    
		Martín                                 C                                                    16/15                      106.66                                   096                      101.33
    
		Luis 		CUAUH                19/20                                                    095                       096                                             95.50  
    
------------------------------------------------------------------------------------------------------------------------------------------------------- 
      Total									     48/50							096													 

	
	GOLES POR EQUIPO		25%
-------------------------------------------------------------------------------------------------------------------------------------------------------



###############################################

PASOS PARA CREAR INSTANCIA EN PYTHONANYWHERE

###############################################

Una vez entendiendo el problema se determina la factibilidad de uso de python para poder montar la aplicacion en la web con "servicios gratuitos"

Posteriormente se procede a la solución del problema

1. Creacion de directorio myapp, en servidor ics.pythonanywhere.com
python manage.py startapp polls

myapp/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
	
2. Agregar url para ruta de myapp
mysite/urls.py


3. Pruebas y procesamiento de JSON en python

import json

class ClsJugador:
    nombre=None
    nivel=None
    goles=None
    sueldo=None
    bono=None
    sueldo_completo=None
    equipo=None

    def __init__(self, objJson):
        self.nombre=objJson['nombre']
        self.nivel=objJson['nivel']
        self.goles=objJson['goles']
        self.sueldo=objJson['sueldo']
        self.bono=objJson['bono']
        self.sueldo_completo=objJson['sueldo_completo']
        self.equipo=objJson['equipo']


r =
{"jugadores" : [  
      {  
         "nombre":"Juan Perez",
         "nivel":"C",
         "goles":10,
         "sueldo":50000,
         "bono":25000,
         "sueldo_completo":'null',
         "equipo":"rojo"
      },
      {  
         "nombre":"EL Cuauh",
         "nivel":"Cuauh",
         "goles":30,
         "sueldo":100000,
         "bono":30000,
         "sueldo_completo":'null',
         "equipo":"azul"
      },
      {  
         "nombre":"Cosme Fulanito",
         "nivel":"A",
         "goles":7,
         "sueldo":20000,
         "bono":10000,
         "sueldo_completo":'null',
         "equipo":"azul"

      },
      {  
         "nombre":"El Rulo",
         "nivel":"B",
         "goles":9,
         "sueldo":30000,
         "bono":15000,
         "sueldo_completo":'null',
         "equipo":"rojo"

      }]
}
objJson = json.loads(json.dumps(r['jugadores']))

#print(type(objJson))

for item in objJson:
    #for node in item:
    #    #print(node,item[node])
    #print()
    objJugador=ClsJugador(item)
    print(str(objJugador.nombre))
    print(str(objJugador.nivel))
    print(str(objJugador.goles))
    print(str(objJugador.sueldo))
    print(str(objJugador.bono))
    print(str(objJugador.sueldo_completo))
    print(str(objJugador.equipo))
    print()
	
	
4. Creacion de vista para API que procesa JSON y codificacion de funcionalidad
myapp/views.py



5. Generacion de pruebas con entornos en linea. https://www.programiz.com/python-programming/online-compiler/


6. Se generar codificacion de cliente que consume aplicacion, archivo fuente cliente.py


7. Pruebas y confirmación de correcto funciomiento


8. Publicacion y versionado a produccion https://ics.pythonanywhere.com/myapp/




