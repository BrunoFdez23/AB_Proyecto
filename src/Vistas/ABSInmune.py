import streamlit as st
import random
from Codigos.AlgoritmoSistemaInmune import ejecutar_algoritmo_sistema_inmune

def immune_algorithm_page(change_page_function):
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
        
        st.markdown("## Algoritmo de Sistemas Inmunes")
        
        st.markdown("""
        Este algoritmo simula un sistema inmune artificial con 10 anticuerpos que representan soluciones en el rango [0,1].
        Cada generación, se selecciona la mitad superior de los anticuerpos con mejor aptitud.
        Estos anticuerpos se clonan, creando copias adicionales de cada uno.
        Luego, cada clon sufre pequeñas mutaciones aleatorias con una probabilidad del 10%, explorando variaciones cercanas.
        Después de evaluar la calidad de los clones, se seleccionan los mejores para formar una nueva población de 10 anticuerpos.
        Este proceso se repite durante 50 generaciones, y al final se devuelve el anticuerpo con la mejor aptitud.
        """)
        
        st.markdown("---")
        
        # Botón para ejecutar el algoritmo
        if st.button("Ejecutar Algoritmo de Sistema Inmune"):
            with st.spinner('Ejecutando algoritmo...'):
                resultado = ejecutar_algoritmo_sistema_inmune()
            
            # Mostrar los resultados
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f'<div class="chromosome">Mejor solución encontrada: {resultado["mejor_final"]:.4f}</div>', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<div class="chromosome">Valor de la función: {resultado["aptitud_final"]:.4f}</div>', unsafe_allow_html=True)
            
            # Mostrar información de la función
            st.markdown(f'<div class="chromosome">Función optimizada: {resultado["funcion_objetivo"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="chromosome">Rango de búsqueda: [{resultado["rango_busqueda"][0]}, {resultado["rango_busqueda"][1]}]</div>', unsafe_allow_html=True)
            
            # Mostrar progreso de las generaciones
            st.markdown("### Evolución del algoritmo")
            
            # Gráfico de convergencia
            st.line_chart(
                data=[gen['aptitud'] for gen in resultado['historial']],
                use_container_width=True
            )
            
            # Añadir anotaciones
            st.markdown("""
            <div style="margin-top: -15px; margin-bottom: 20px;">
                <small>
                    <strong>Eje X:</strong> Número de Generación | 
                    <strong>Eje Y:</strong> Valor de Aptitud<br>
                    <strong>Línea:</strong> Muestra la evolución del mejor valor encontrado en cada generación
                </small>
            </div>
            """, unsafe_allow_html=True)
            
            # Detalles por generación
            with st.expander("Ver detalles por generación"):
                for gen in resultado['historial']:
                    st.markdown(f"**Generación {gen['generacion']}**")
                    st.markdown(f"""
                    <div style="margin-bottom: 10px;">
                        Mejor solución: {gen['mejor_solucion']:.4f}<br>
                        Aptitud: {gen['aptitud']:.4f}
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.markdown('<div class="chromosome">Presiona "Ejecutar Algoritmo de Sistema Inmune" para ver los resultados</div>', unsafe_allow_html=True)
                
        st.markdown('</div>', unsafe_allow_html=True)