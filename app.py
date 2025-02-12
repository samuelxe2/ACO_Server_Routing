import streamlit as st
import numpy as np
from utils.ant_colony import AntColony
from utils.visualization import plot_network, plot_feromonas, plot_latencies, plot_best_route, plot_ant_paths

# Definir servidores y conexiones
SERVIDORES = ['EU', 'ASIA', 'USA', 'CDN1', 'CDN2']
CONECCIONES = [
    ('EU', 'USA', 50), 
    ('EU', 'ASIA', 200), 
    ('USA', 'ASIA', 100), 
    ('USA', 'CDN1', 30), 
    ('ASIA', 'CDN2', 80), 
    ('CDN1', 'EU', 40), 
    ('CDN2', 'USA', 70)
]

# Inicializar la colonia de hormigas
colonia = AntColony(SERVIDORES, CONECCIONES)

# Interfaz Streamlit
st.title('🔎 Simulación de Enrutamiento con ACO')
st.write("""
Este sistema muestra cómo las **hormigas virtuales** encuentran la mejor ruta en una red de servidores.
Las **feromonas** afectan las decisiones, haciendo que los caminos más rápidos se vuelvan más atractivos con el tiempo.
""")

origen = st.selectbox('🟢 Servidor de origen', SERVIDORES)
destino = st.selectbox('🔴 Servidor de destino', SERVIDORES)

if st.button('🚀 Iniciar Simulación'):
    mejor_ruta, mejor_latencia, rutas, latencias, feromonas_evolucion = colonia.simular(origen, destino)

    st.write("### 🏆 Mejor Ruta Encontrada")
    st.write(f"🛤️ Ruta: {' -> '.join(mejor_ruta)}")
    st.write(f"⏱️ Latencia Total: {mejor_latencia:.2f} ms")

    st.pyplot(plot_network(SERVIDORES, CONECCIONES))
    st.pyplot(plot_feromonas(feromonas_evolucion))
    st.pyplot(plot_latencies(latencias))
    st.pyplot(plot_best_route(mejor_ruta, CONECCIONES))
    st.pyplot(plot_ant_paths(rutas, CONECCIONES, origen, destino))
