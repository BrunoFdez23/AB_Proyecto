import streamlit as st
import random
from Codigos.hormigas import ejecutar_algoritmo_hormigas

def ants_algorithm_page(change_page_function):
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
    
    # Contenido del algoritmo genético
    with st.container():
        
        st.markdown("## Algoritmo Genético")
        
        st.markdown("""
        Este algoritmo simula 10 hormigas artificiales buscando la ruta más corta entre 10 ciudades. Cada hormiga construye una ruta probabilística, donde la probabilidad de moverse a la siguiente ciudad depende de:

1. La cantidad de feromonas en el camino (atracción química)
2. La distancia inversa entre ciudades (prefiere caminos más cortos)

Las hormigas depositan más feromonas en las rutas más cortas (100/distance), mientras que todas las feromonas se evaporan gradualmente (tasa del 50% por iteración). Este proceso se repite durante 100 generaciones, reforzando progresivamente los mejores caminos. Al finalizar, devuelve la ruta con la distancia total más corta encontrada.
        """)
        
        st.markdown("---")
        
        # Botón para ejecutar el algoritmo
        ejecutar_algoritmo_hormigas()
        
        st.markdown('</div>', unsafe_allow_html=True)