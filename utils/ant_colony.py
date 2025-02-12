import numpy as np
import random

class AntColony:
    def __init__(self, servidores, conexiones, n_hormigas=20, evaporacion=0.6, alfa=2, beta=2, iteraciones=10):
        self.servidores = servidores
        self.conexiones = {c[:2]: c[2] for c in conexiones}
        self.feromonas = {c[:2]: 1.0 for c in conexiones}
        self.n_hormigas = n_hormigas
        self.evaporacion = evaporacion
        self.alfa = alfa
        self.beta = beta
        self.iteraciones = iteraciones

    def elegir_ruta(self, inicio):
        rutas = [c for c in self.conexiones if c[0] == inicio]
        if not rutas:
            raise ValueError(f"No hay rutas disponibles desde {inicio}")
        
        probabilidades = [self.feromonas[r] ** self.alfa / (self.conexiones[r] ** self.beta) for r in rutas]
        probabilidades /= np.sum(probabilidades)
        return random.choices(rutas, weights=probabilidades)[0][1]

    def simular(self, origen, destino):
        mejor_ruta, mejor_latencia = None, float('inf')
        rutas, latencias = [], []
        feromonas_evolucion = []

        for _ in range(self.iteraciones):
            for _ in range(self.n_hormigas):
                nodo, ruta, latencia_total = origen, [origen], 0
                while nodo != destino:
                    try:
                        siguiente = self.elegir_ruta(nodo)
                    except ValueError:
                        break
                    latencia_total += self.conexiones[(nodo, siguiente)]
                    nodo = siguiente
                    ruta.append(nodo)

                rutas.append(ruta)
                latencias.append(latencia_total)

                if latencia_total < mejor_latencia:
                    mejor_latencia, mejor_ruta = latencia_total, ruta
            
            self.actualizar_feromonas(rutas, latencias)
            feromonas_evolucion.append(self.feromonas.copy())

        return mejor_ruta, mejor_latencia, rutas, latencias, feromonas_evolucion

    def actualizar_feromonas(self, rutas, latencias):
        for c in self.feromonas:
            self.feromonas[c] *= (1 - self.evaporacion)

        for ruta, latencia in zip(rutas, latencias):
            for i in range(len(ruta) - 1):
                self.feromonas[(ruta[i], ruta[i+1])] += 1 / latencia
