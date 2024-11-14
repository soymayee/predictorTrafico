# route_calculation.py
import networkx as nx
import requests
from map_config import G, nodes, locations

api_key = 'YOUR_GOOGLE_API_KEY'  # Reemplaza con tu clave

def calcular_rutas(origen, destino):
    ruta_corta = nx.shortest_path(G, source=nodes[origen], target=nodes[destino], weight="length")
    ruta_larga = nx.shortest_path(G, source=nodes[origen], target=nodes[destino], weight="length")
    return ruta_corta, ruta_larga

def calcular_ruta(origen, destino):
    origen_coords = locations[origen][1]
    destino_coords = locations[destino][1]
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origen_coords[0]},{origen_coords[1]}&destination={destino_coords[0]},{destino_coords[1]}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "OK":
        tiempo_estimado = data["routes"][0]["legs"][0]["duration"]["text"]
        distancia = data["routes"][0]["legs"][0]["distance"]["text"]
        return tiempo_estimado, distancia
    else:
        return None, None
