import streamlit as st
from Vistas.ABGenetico import genetic_algorithm_page
from Vistas.ABSInmune import immune_algorithm_page

# Configurar la página
st.set_page_config(page_title="Algoritmos Bioinspirados", page_icon="🧬", layout="centered")

# Estilos de la página
st.markdown(
    """
    <style>
        body {
            background-color: #6b6f2f;
            color: black;
        }
        .stApp {
            background-color: #6b6f2f;
        }
        /* Segunda columna */
        div[data-testid="stHorizontalBlock"] > div:nth-child(2) {
            background-color: #ccffcc;
            border-radius: 10px;
        }
        .stButton>button {
            width: 80%;
            border-radius: 20px;
            border: 2px solid black;
            background-color: #b0d48c;
            color: black;
            font-size: 18px;
            padding: 10px;
        }
        .selected-button {
            background-color: #6b8c42 !important;
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
        st.markdown("<h1 style='text-align: center; color: #c1e59d; text-shadow: -2px -2px 0 #000, 1px -1px 0 #000,-1px 1px 0 #000, 1px 1px 0 #000;'>Algoritmos Bioinspirados</h1>", unsafe_allow_html=True)

        _, colButtons, _ = st.columns([1.5, 3, 1])
        with colButtons:
            st.button("Genético", 
                     on_click=change_page, args=('genetic',),
                     key="genetico")
            #st.button("Recocido Simulado", 
            #         on_click=change_page, args=('simulated',),
            #         key="recocido")
            #st.button("Colonia de Hormigas", 
            #         on_click=change_page, args=('ants',),
            #         key="hormigas")
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