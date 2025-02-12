import matplotlib.pyplot as plt
import networkx as nx

def plot_network(servidores, conexiones):
    G = nx.DiGraph()
    for c in conexiones:
        G.add_edge(c[0], c[1])
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='black', width=2)
    plt.title("📡 Red de Servidores")
    return plt

def plot_feromonas(feromonas_evolucion):
    plt.figure(figsize=(8, 4))
    for i, feromonas in enumerate(feromonas_evolucion):
        valores = [v for v in feromonas.values()]
        plt.plot(range(len(valores)), valores, label=f'Iteración {i+1}')

    plt.xlabel('Conexiones')
    plt.ylabel('Nivel de Feromonas')
    plt.legend()
    plt.title("📊 Evolución de Feromonas")
    return plt

def plot_latencies(latencias):
    plt.figure(figsize=(6, 4))
    plt.scatter(range(len(latencias)), latencias, color='red')
    plt.xlabel('Hormiga')
    plt.ylabel('Latencia (ms)')
    plt.title("📈 Latencias de las Hormigas")
    return plt

def plot_best_route(mejor_ruta, conexiones):
    G = nx.DiGraph()
    for c in conexiones:
        G.add_edge(c[0], c[1])
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='black', width=2)
    
    edges = [(mejor_ruta[i], mejor_ruta[i+1]) for i in range(len(mejor_ruta) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2)
    plt.title("🛤️ Mejor Ruta Encontrada")
    return plt

def plot_ant_paths(rutas, conexiones, origen, destino):
    G = nx.DiGraph()
    for c in conexiones:
        G.add_edge(c[0], c[1])
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='black', width=2)

    for ruta in rutas:
        edges = [(ruta[i], ruta[i+1]) for i in range(len(ruta) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='green', width=1, alpha=0.5)

    plt.title("🐜 Caminos Explorados por las Hormigas")
    return plt

def plot_scatter(latencias):
    plt.figure(figsize=(6, 4))
    plt.scatter(range(len(latencias)), latencias, color='red')
    plt.xlabel('Hormiga')
    plt.ylabel('Latencia (ms)')
    plt.title('📈 Latencias de las Hormigas')
    return plt
