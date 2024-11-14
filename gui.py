# gui.py
import tkinter as tk
from map_display import mostrar_mapa, mostrar_grafo_y_tabla
from route_calculation import calcular_ruta, calcular_rutas
from map_config import locations

def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Guía de Rutas en Fusagasugá")
    ventana.geometry("600x600")

    label_origen = tk.Label(ventana, text="Seleccione el origen (1-5):")
    label_origen.pack()
    entry_origen = tk.Entry(ventana)
    entry_origen.pack()
    label_destino = tk.Label(ventana, text="Seleccione el destino (1-5):")
    label_destino.pack()
    entry_destino = tk.Entry(ventana)
    entry_destino.pack()
    label_instrucciones = tk.Label(ventana, text="1: Parque Principal\n2: Hospital San Rafael\n3: Centro Comercial Manila\n4: Estadio Fernando Mazuera\n5: Terminal de Transporte Bogotá")
    label_instrucciones.pack()
    result_text = tk.StringVar()
    result_label = tk.Label(ventana, textvariable=result_text, fg="blue")
    result_label.pack()

    def obtener_seleccion(event):
        try:
            origen = int(entry_origen.get())
            destino = int(entry_destino.get())
            if origen in locations and destino in locations:
                ruta_corta, ruta_larga = calcular_rutas(origen, destino)
                if ruta_corta and ruta_larga:
                    tiempo, distancia = calcular_ruta(origen, destino)
                    result_text.set(f"Duración: {tiempo}\nDistancia: {distancia}")
                    mostrar_mapa([ruta_corta, ruta_larga], "rutas_fusa.html")
                    mostrar_grafo_y_tabla([ruta_corta, ruta_larga])
            else:
                result_text.set("Por favor ingrese valores válidos.")
        except ValueError:
            result_text.set("Error en la entrada. Asegúrese de ingresar números válidos.")

    ventana.bind('<Return>', obtener_seleccion)
    ventana.mainloop()
