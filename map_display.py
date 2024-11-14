# map_display.py
import folium
from folium.plugins import AntPath
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import webbrowser
from map_config import G, locations

def mostrar_mapa(rutas, archivo_nombre):
    m = folium.Map(location=[4.336, -74.369], zoom_start=14)
    for key, (name, coords) in locations.items():
        folium.Marker(location=coords, popup=name).add_to(m)
    route_coords_corta = [(G.nodes[node]["y"], G.nodes[node]["x"]) for node in rutas[0]]
    AntPath(route_coords_corta, color="green", weight=5, opacity=0.7).add_to(m)
    route_coords_larga = [(G.nodes[node]["y"], G.nodes[node]["x"]) for node in rutas[1]]
    AntPath(route_coords_larga, color="red", weight=5, opacity=0.7).add_to(m)
    m.save(archivo_nombre)
    webbrowser.open(archivo_nombre)

def mostrar_grafo_y_tabla(rutas):
    for i, ruta in enumerate(rutas):
        subgraph = G.subgraph(ruta)
        pos = {node: (G.nodes[node]['x'], G.nodes[node]['y']) for node in ruta}
        etiquetas = {node: f"q{i}" for i, node in enumerate(ruta)}
        plt.figure(figsize=(10, 6))
        nx.draw(subgraph, pos, labels=etiquetas, node_size=300, node_color='red', font_size=8, font_color='white', with_labels=True, edge_color='blue', width=2)
        plt.title(f"Grafo de la Ruta {i + 1}")
        plt.show()
        transitions = [(etiquetas[ruta[i]], etiquetas[ruta[i + 1]]) for i in range(len(ruta) - 1)]
        df_transitions = pd.DataFrame(transitions, columns=["Estado Origen", "Estado Destino"])
        print(f"Tabla de Transición Ruta {i + 1}:\n", df_transitions.to_string(index=False))
