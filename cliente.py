import requests

'''
URL de servicio donde se monto la aplicacion que solventa la necesidad de RESUELVE BACK-END
'''
url = 'https://ics.pythonanywhere.com/myapp/';

'''
Especificacion de contenido que enviara el cliente el la peticion
'''
headers = {'Content-Type': 'application/json'}

'''
Estructura JSON tomada de la tabla https://github.com/resuelve/prueba-ing-backend

Jugador	Nivel	Goles anotados en el mes/mínimo requerido
Juan	A	6/5
Pedro	B	7/10
Martín	C	16/15
Luis	Cuauh	19/20
total		48/50
'''

body = """{
   "jugadores" : [
      {  
         "nombre":"Juan Perez",
         "nivel":"A",
         "goles":6,
         "sueldo":50000,
         "bono":25000,
         "sueldo_completo":null,
         "equipo":"rojo"
      },
      {  
         "nombre":"EL Cuauh",
         "nivel":"Cuauh",
         "goles":19,
         "sueldo":50000,
         "bono":10000,
         "sueldo_completo":null,
         "equipo":"azul"
      },
      {  
         "nombre":"Cosme Fulanito",
         "nivel":"B",
         "goles":7,
         "sueldo":20000,
         "bono":10000,
         "sueldo_completo":null,
         "equipo":"azul"
      },
      {  
         "nombre":"El Rulo",
         "nivel":"C",
         "goles":16,
         "sueldo":30000,
         "bono":15000,
         "sueldo_completo":null,
         "equipo":"rojo"
      }
   ]
}"""

'''
Creacion y envio de la peticion a https://ics.pythonanywhere.com/myapp/
'''
req = requests.post(url, headers=headers, data=body)

print("Estatus de la peticion: "+str(req.status_code))
print()
print("Headers de response: "+str(req.headers))
print()
print("JSON REQUEST: "+str(req.text))