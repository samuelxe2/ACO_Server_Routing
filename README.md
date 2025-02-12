# 🐜 Algoritmo de Colonia de Hormigas (ACO) para Optimización de Rutas en Redes  

Este repositorio contiene la implementación del **Algoritmo de Colonia de Hormigas (ACO)** para optimizar rutas en una red, modelando el comportamiento de las hormigas en la búsqueda de caminos eficientes.

## 📌 Descripción  

El algoritmo simula el movimiento de hormigas virtuales sobre una red de nodos, donde la selección de rutas se basa en **feromonas** y **heurísticas de distancia**. A medida que las hormigas exploran la red, actualizan la cantidad de feromonas en los caminos más eficientes, favoreciendo su selección en futuras iteraciones.  

## 🚀 Características Principales  

✔ Implementación de la **regla de transición de estados** para la toma de decisiones de las hormigas.  
✔ **Actualización dinámica de feromonas**, considerando la calidad de la ruta encontrada.  
✔ **Visualización gráfica** de la red y evolución de las feromonas en cada iteración.  
✔ **Simulación de múltiples ejecuciones** para evaluar la convergencia del algoritmo.  
✔ **Análisis de rendimiento** comparando distintas configuraciones.  

## 🛠 Requisitos  

Antes de ejecutar el código, asegúrate de tener instaladas las siguientes dependencias:  

```bash
pip install numpy networkx matplotlib streamlit

se recomienda reiniciar vizual luego de descargar las dependecias

```para iniciar proyecto poner en la terminal 
streamlit run app.py
