import streamlit as st
import random
from Codigos.AlgoritmoGeneticoBinario import ejecutar_algoritmo_genetico

def genetic_algorithm_page(change_page_function):
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
                font-family: Georgia, 'Times New Roman', Times, serif;
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
        Este algoritmo crea una población de 6 cromosomas con 10 aptitudes binarias.  
        Ej: población de cromosomas
        """)
        
        # Generar y mostrar cromosomas de ejemplo
        chromosomes = [[random.randint(0, 1) for _ in range(10)] for _ in range(6)]
        col1, col2 = st.columns(2)
        
        with col1:
            for i in range(3):
                st.markdown(f'<div class="chromosome">[{", ".join(map(str, chromosomes[i]))}]</div>', unsafe_allow_html=True)
        
        with col2:
            for i in range(3, 6):
                st.markdown(f'<div class="chromosome">[{", ".join(map(str, chromosomes[i]))}]</div>', unsafe_allow_html=True)
        
        st.markdown("""
        De forma aleatoria compara 4 cromosomas de las cuales toma las 2 mejores y las cruza 
        para crear 2 cromosomas hijos, cada aptitud de los cromosomas hijos tiene una 
        probabilidad del 10% de cambiar. Este proceso se repite 3 veces para conseguir una 
        nueva generación de 6 cromosomas, tras 20 generaciones devuelve el cromosoma con la 
        mejor calidad de aptitudes.
        """)
        
        st.markdown("---")
        
        # Botón para ejecutar el algoritmo
        if st.button("Ejecutar Algoritmo Genético"):
            with st.spinner('Ejecutando algoritmo...'):
                resultado = ejecutar_algoritmo_genetico()
            
            # Mostrar el mejor cromosoma de la 20ª generación
            st.markdown(f'<div class="chromosome">Mejor cromosoma final: [{", ".join(map(str, resultado["mejor_final"]))}]</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="chromosome">Aptitud: {resultado["aptitud_final"]}/10</div>', unsafe_allow_html=True)
            
            # Mostrar progreso de las generaciones
            st.markdown("### Progreso del algoritmo")
            for gen in resultado['historial']:
                porcentaje = (gen['aptitud'] / 10) * 100
                st.markdown(f"Generación {gen['generacion']}:")
                st.markdown(f"""
                <div class="progress-bar">
                    <div class="progress" style="width: {porcentaje}%">{porcentaje:.0f}%</div>
                </div>
                <div class="chromosome">[{", ".join(map(str, gen['mejor_cromosoma']))}]</div>
                """, unsafe_allow_html=True)
        else:
            st.markdown('<div class="chromosome">Presiona "Ejecutar Algoritmo Genético" para ver los resultados</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)