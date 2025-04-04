import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def simulated_annealing(distances, initial_temp, cooling_rate, iterations):
    num_cities = len(distances)
    
    # Ruta inicial aleatoria
    current_solution = np.random.permutation(num_cities)
    current_distance = total_distance(current_solution, distances)

    best_solution = np.copy(current_solution)
    best_distance = current_distance

    temp = initial_temp
    historial = []

    for iteration in range(iterations):
        # Generar un nuevo estado intercambiando dos ciudades
        new_solution = np.copy(current_solution)
        i, j = np.random.choice(num_cities, 2, replace=False)
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]

        new_distance = total_distance(new_solution, distances)
        
        # Aceptar la nueva solución si es mejor o con probabilidad e^(-ΔE/T)
        delta = new_distance - current_distance
        if delta < 0 or np.exp(-delta / temp) > np.random.rand():
            current_solution, current_distance = new_solution, new_distance

            # Si es la mejor encontrada, actualizar
            if current_distance < best_distance:
                best_solution, best_distance = np.copy(current_solution), current_distance
        
        # Reducir la temperatura
        temp *= cooling_rate

        # Guardar datos para visualizar el progreso
        historial.append(best_distance)

    return best_solution, best_distance, historial

def total_distance(route, distances):
    """Calcula la distancia total de una ruta dada"""
    return sum(distances[route[i], route[i+1]] for i in range(len(route)-1)) + distances[route[-1], route[0]]

def ejecutar_recocido_simulado():
    st.markdown(
        """
        <style>
            .main-container {
                background-color: white;
                border-radius: 10px;
                padding: 20px;
                margin-top: 20px;
            }
            /* Segunda columna */
            div[data-testid="stHorizontalBlock"] > div:nth-child(2) {
                background-color: #515d7e;
                border-radius: 10px;
            }
            .stButton>button {
                width: 20%;
                border-radius: 20px;
                border: 2px solid black;
                background-color: #182957;
                color: black;
                font-size: 18px;
                padding: 10px;
            }
            .chromosome {
                font-family:Georgia, 'Times New Roman', Times, serif;
                font-size: 18px;
                margin: 5px 0;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Contenido del algoritmo de recorrido simulado
    with st.container():
        st.markdown("## Algoritmo de Recorrido Simulado")
        
        st.markdown("""
        Este algoritmo simula el proceso físico de recocido en metalurgia para encontrar una solución aproximada al problema del viajante (TSP). 

El algoritmo comienza con una solución aleatoria y una temperatura alta. En cada iteración:
1. Genera una solución vecina intercambiando dos ciudades
2. Acepta la nueva solución si es mejor
3. Con cierta probabilidad, acepta soluciones peores (dependiendo de la temperatura actual)
4. Reduce gradualmente la temperatura según la tasa de enfriamiento

A medida que la temperatura disminuye, el algoritmo se vuelve más selectivo, convergiendo hacia una solución óptima local. Los parámetros ajustables (temperatura inicial, tasa de enfriamiento e iteraciones) controlan el comportamiento de la búsqueda.
        """)
        
        st.markdown("---")
        
        # Parámetros configurables
        NUM_CITIES = st.sidebar.slider("Número de ciudades", 5, 20, 10)
        INITIAL_TEMP = st.sidebar.slider("Temperatura inicial", 10.0, 1000.0, 100.0)
        COOLING_RATE = st.sidebar.slider("Tasa de enfriamiento", 0.90, 0.999, 0.95)
        ITERATIONS = st.sidebar.slider("Iteraciones", 100, 5000, 1000)

        # Generar ciudades aleatorias
        np.random.seed(42)
        cities = np.random.rand(NUM_CITIES, 2) * 500
        distances = np.zeros((NUM_CITIES, NUM_CITIES))

        for i in range(NUM_CITIES):
            for j in range(NUM_CITIES):
                if i != j:
                    distances[i][j] = np.linalg.norm(cities[i] - cities[j])

        if st.button("Iniciar Optimización"):
            with st.spinner('Optimizando ruta...'):
                best_route, best_distance, historial = simulated_annealing(distances, INITIAL_TEMP, COOLING_RATE, ITERATIONS)

            # Mostrar resultados
            st.success(f"Mejor ruta encontrada: {best_route.tolist()}")
            st.success(f"Distancia total: {best_distance:.2f}")

            # Visualizar resultado
            fig, ax = plt.subplots(figsize=(10, 6))

            # Dibujar ciudades
            ax.scatter(cities[:, 0], cities[:, 1], c='blue', s=100)
            
            for i, (x, y) in enumerate(cities):
                ax.text(x + 10, y + 10, str(i), fontsize=12)

            # Dibujar mejor ruta
            for i in range(len(best_route)-1):
                start = cities[best_route[i]]
                end = cities[best_route[i+1]]
                ax.plot([start[0], end[0]], [start[1], end[1]], 'r-', linewidth=2)
            
            # Conectar el último punto con el primero
            ax.plot([cities[best_route[-1]][0], cities[best_route[0]][0]], 
                    [cities[best_route[-1]][1], cities[best_route[0]][1]], 'r-', linewidth=2)

            ax.set_title("Mejor Ruta Encontrada")
            st.pyplot(fig)

            # Gráfico de convergencia
            st.subheader("Progreso del Algoritmo")
            st.line_chart(historial)

def simulated_annealing_page(change_page_function):
    # Botón para volver
    if st.button("← Volver al menú principal"):
        change_page_function('main')

    # Ejecutar la simulación
    ejecutar_recocido_simulado()