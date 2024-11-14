# map_config.py
import osmnx as ox

location_point = (4.336, -74.369)
G = ox.graph_from_point(location_point, dist=3000, network_type="drive")

locations = {
    1: ("Parque Principal", (4.3434, -74.3627)),
    2: ("Hospital San Rafael", (4.3378, -74.3692)),
    3: ("Centro Comercial Manila", (4.3410, -74.3655)),
    4: ("Estadio Fernando Mazuera", (4.3319, -74.3706)),
    5: ("Terminal de Transporte Bogotá", (4.6473, -74.0780))
}

nodes = {key: ox.nearest_nodes(G, loc[1][1], loc[1][0]) for key, loc in locations.items()}
