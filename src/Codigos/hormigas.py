import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io

def ejecutar_algoritmo_hormigas():
    # Parámetros configurables
    NUM_ANTS = st.sidebar.slider("Número de hormigas", 5, 50, 10)
    NUM_NODES = st.sidebar.slider("Número de ciudades", 5, 20, 10)
    ITERATIONS = st.sidebar.slider("Iteraciones", 10, 200, 50)
    EVAPORATION_RATE = st.sidebar.slider("Tasa de evaporación", 0.1, 0.9, 0.5)

    # Inicialización
    np.random.seed(42)
    nodes = np.random.rand(NUM_NODES, 2) * 500
    distances = np.zeros((NUM_NODES, NUM_NODES))
    pheromones = np.ones((NUM_NODES, NUM_NODES))

    # Calcular distancias
    for i in range(NUM_NODES):
        for j in range(NUM_NODES):
            if i != j:
                distances[i][j] = np.linalg.norm(nodes[i] - nodes[j])

    # Algoritmo ACO
    def ant_colony_optimization():
        nonlocal pheromones
        best_route = None
        best_distance = float("inf")
        historial = []

        for iteration in range(ITERATIONS):
            all_routes = []
            all_distances = []

            for _ in range(NUM_ANTS):
                route = [np.random.randint(NUM_NODES)]
                while len(route) < NUM_NODES:
                    i = route[-1]
                    probs = []
                    for j in range(NUM_NODES):
                        if j not in route:
                            prob = (pheromones[i][j] ** 1.0) * ((1 / distances[i][j]) ** 2.0)
                            probs.append(prob)
                        else:
                            probs.append(0)
                    
                    probs = np.array(probs)
                    probs /= probs.sum()
                    next_node = np.random.choice(range(NUM_NODES), p=probs)
                    route.append(next_node)
                
                distance = sum(distances[route[i]][route[i+1]] for i in range(len(route)-1))
                all_routes.append(route)
                all_distances.append(distance)

                if distance < best_distance:
                    best_distance = distance
                    best_route = route

            # Actualización de feromonas
            pheromones *= (1 - EVAPORATION_RATE)
            for i, route in enumerate(all_routes):
                for j in range(len(route)-1):
                    pheromones[route[j]][route[j+1]] += 100 / all_distances[i]
            
            historial.append({
                'iteracion': iteration + 1,
                'mejor_distancia': best_distance,
                'mejor_ruta': best_route.copy() if best_route else None
            })

        return best_route, best_distance, historial

    # Interfaz Streamlit
    st.title("Simulación de Colonia de Hormigas")

    if st.button("Iniciar Simulación"):
        with st.spinner('Optimizando rutas...'):
            best_path, best_distance, historial = ant_colony_optimization()

        # Mostrar resultados
        st.success(f"Mejor ruta encontrada: {best_path}")
        st.success(f"Distancia total: {best_distance:.2f}")

        # Visualización con Matplotlib
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Dibujar nodos
        ax.scatter(nodes[:, 0], nodes[:, 1], c='blue', s=100)
        for i, (x, y) in enumerate(nodes):
            ax.text(x + 10, y + 10, str(i), fontsize=12)

        # Dibujar mejor ruta
        for i in range(len(best_path)-1):
            start = nodes[best_path[i]]
            end = nodes[best_path[i+1]]
            ax.plot([start[0], end[0]], [start[1], end[1]], 'r-', linewidth=2)

        ax.set_title("Mejor Ruta Encontrada")
        st.pyplot(fig)

        # Gráfico de convergencia
        st.subheader("Progreso del Algoritmo")
        distancias = [h['mejor_distancia'] for h in historial]
        st.line_chart(distancias)

        # Detalles por iteración
        with st.expander("Ver detalles por iteración"):
            for h in historial[::5]:  # Mostrar cada 5 iteraciones
                st.write(f"Iteración {h['iteracion']}: Distancia = {h['mejor_distancia']:.2f}")

def ant_colony_page(change_page_function):
    # Botón para volver
    if st.button("← Volver al menú principal"):
        change_page_function('main')
    
    # Ejecutar la simulación
    ejecutar_algoritmo_hormigas()