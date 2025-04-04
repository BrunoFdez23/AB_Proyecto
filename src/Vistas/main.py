import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Vistas.ABGenetico import genetic_algorithm_page

import streamlit as st
from Vistas.ABGenetico import genetic_algorithm_page
from Vistas.ABSInmune import immune_algorithm_page
from Vistas.ABHormigas import ants_algorithm_page
from Vistas.ABRecorrido_Simulado import simulated_annealing_page


# Configurar la página
st.set_page_config(page_title="Algoritmos Bioinspirados", page_icon="🧬", layout="centered")

# Estilos de la página
st.markdown( 
    """
    <style>
        body {
            background-color: #515d7e;
          
        }
        .stApp {
            background-color: #515d7e;
            color: black;
        }
        /* Segunda columna */
        div[data-testid="stHorizontalBlock"] > div:nth-child(2) {
            background-color: #70778b ;
            border-radius: 5px;
            color:black;
        }
        .stButton>button {
            width: 80%;
            border-radius: 10px;
            border: 2px solid  #515d7e;
            background-color: #182957;
            color: black;
            font-size: 18px;
            padding: 10px;
        }

        .selected-button {
            background-color: #182957 !important;
            color: white !important;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Inicializar estado de la sesión
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'main'

# Función para cambiar de página
def change_page(page_name):
    st.session_state.current_page = page_name

# Página principal
def main_page():
    # Espaciado y diseño con columnas para centrar los botones
    _, colTittle, _ = st.columns([1.5, 7, 1.5])

    with colTittle:
        st.markdown("<h1 style='text-align: center;border: 0%; color: #515d7e; '>Algoritmos Bioinspirados</h1>", unsafe_allow_html=True)

        _, colButtons, _ = st.columns([1.5, 3, 1])
        with colButtons:
            st.button("Genético", 
                     on_click=change_page, args=('genetic',),
                     key="genetico")
            st.button("Recorrido Simulado", 
                     on_click=change_page, args=('simulated',),
                     key="recocido")
            st.button("Colonia de Hormigas", 
                     on_click=change_page, args=('ants',),
                     key="hormigas")
            st.button("Sistemas Inmunes", 
                     on_click=change_page, args=('immune',),
                     key="inmunes")
            st.write("")
            st.write("")

# Mostrar la página correspondiente
if st.session_state.current_page == 'main':
    main_page()
elif st.session_state.current_page == 'genetic':
    genetic_algorithm_page(change_page)
elif st.session_state.current_page == 'immune':
    immune_algorithm_page(change_page)
elif st.session_state.current_page == 'ants':
    ants_algorithm_page(change_page)
elif st.session_state.current_page == 'simulated':
    simulated_annealing_page(change_page)