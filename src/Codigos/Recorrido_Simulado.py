import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def simulated_tour_algorithm_page(change_page_function):
    # Botón para volver atrás
    if st.button("Volver"):
        change_page_function('main')
     # Estilos de la página
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
                background-color: #6b6f2f;
                border-radius: 10px;
            }
            .stButton>button {
                width: 20%;
                border-radius: 20px;
                border: 2px solid black;
                background-color: #b0d48c;
                color: black;
                font-size: 18px;
                padding: 10px;
            }
            .chromosome {
                font-family: monospace;
                font-size: 18px;
                margin: 5px 0;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Título y descripción
    st.markdown("## Algoritmo de Recorrido Simulado")
    st.markdown("""
    <div style="margin-bottom: 20px;">
        Este algoritmo simula el proceso de recocido en metalurgia para encontrar 
        el mínimo global de una función, evitando quedar atrapado en mínimos locales.
    </div>
    """, unsafe_allow_html=True)

    # Función objetivo (puedes cambiarla)
    def objective_function(x):
        return x**2 + 10*np.sin(x) + 5*np.cos(3*x)

    # Algoritmo de Recorrido Simulado
    def run_simulated_annealing(x0, temp, cooling_rate, iterations):
        current_x = x0
        current_val = objective_function(current_x)
        history = []
        
        for i in range(iterations):
            # Generar nuevo punto candidato
            new_x = current_x + np.random.normal(0, 1)
            new_val = objective_function(new_x)
            
            # Calcular diferencia
            delta = new_val - current_val
            
            # Criterio de aceptación
            if delta < 0 or np.random.rand() < np.exp(-delta/temp):
                current_x, current_val = new_x, new_val
            
            # Enfriamiento
            temp *= cooling_rate
            history.append((current_x, current_val, temp))
        
        return current_x, current_val, history

    # Controles en sidebar
    st.sidebar.header("Configuración")
    x0 = st.sidebar.slider("Punto inicial", -10.0, 10.0, 0.0, 0.1)
    initial_temp = st.sidebar.slider("Temperatura inicial", 10.0, 200.0, 100.0)
    cooling_rate = st.sidebar.slider("Tasa de enfriamiento", 0.8, 0.999, 0.95, 0.001)
    iterations = st.sidebar.slider("Iteraciones", 100, 5000, 1000)

    # Ejecución del algoritmo
    if st.button("Ejecutar Simulated Annealing", key="run_sa"):
        with st.spinner('Optimizando...'):
            best_x, best_val, history = run_simulated_annealing(
                x0, initial_temp, cooling_rate, iterations
            )
        
        # Mostrar resultados
        st.markdown(f"""
        <div class="result-box">
            <strong>Mejor solución encontrada:</strong> x = {best_x:.4f}<br>
            <strong>Valor de la función:</strong> f(x) = {best_val:.4f}
        </div>
        """, unsafe_allow_html=True)

        # Visualización
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
        # Gráfico de la función y recorrido
        x_vals = np.linspace(-10, 10, 400)
        y_vals = objective_function(x_vals)
        ax1.plot(x_vals, y_vals, 'b-', label='Función objetivo')
        ax1.scatter(
            [x for x, _, _ in history], 
            [y for _, y, _ in history],
            c=range(len(history)), cmap='viridis', alpha=0.6
        )
        ax1.set_xlabel('x')
        ax1.set_ylabel('f(x)')
        ax1.set_title('Recorrido de la solución')
        ax1.legend()
        
        # Gráfico de convergencia
        ax2.plot([val for _, val, _ in history], 'r-')
        ax2.set_xlabel('Iteración')
        ax2.set_ylabel('Valor de f(x)')
        ax2.set_title('Convergencia del algoritmo')
        ax2.grid(True)
        
        st.pyplot(fig)

        # Mostrar evolución de parámetros
        with st.expander("Ver detalles de la ejecución"):
            st.write(f"Temperatura final: {history[-1][2]:.4f}")
            st.line_chart([temp for _, _, temp in history])