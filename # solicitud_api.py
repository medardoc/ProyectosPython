# solicitud_api.py
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    datos = respuesta.json()
    print("Datos de la API:")
    print("Titulo:", datos["title"])
    print("Cuerpo:", datos["body"])

else: 
    print("Error al obtener los datos. Codigo de estado:", respuesta.status_code)
    