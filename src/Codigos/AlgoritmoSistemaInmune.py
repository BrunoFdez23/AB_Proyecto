import numpy as np

def ejecutar_algoritmo_sistema_inmune():
    # Parámetros
    POP_SIZE = 10       # Tamaño de la población (anticuerpos)
    GENS = 50           # Número de generaciones
    MUT_RATE = 0.1      # Tasa de mutación
    CLONE_RATE = 2      # Número de clones por anticuerpo

    # Función a optimizar
    def fitness(x): 
        return x * np.sin(10 * np.pi * x) + 2.0

    # Inicializar población aleatoria en el rango [0,1]
    population = np.random.rand(POP_SIZE)
    historial = []

    for gen in range(GENS):
        # Evaluar fitness de la población
        scores = fitness(population)

        # Seleccionar los mejores anticuerpos
        sorted_idx = np.argsort(scores)[::-1]  # Orden descendente
        best = population[sorted_idx[:POP_SIZE // 2]]  # Mitad superior

        # Clonación: cada mejor anticuerpo se clona varias veces
        clones = np.repeat(best, CLONE_RATE)
        
        # Mutación: pequeños cambios en los clones
        mutations = MUT_RATE * np.random.randn(len(clones))
        clones = np.clip(clones + mutations, 0, 1)  # Asegurar rango [0,1]

        # Evaluar fitness de clones y seleccionar los mejores
        new_population = np.concatenate((best, clones))
        new_scores = fitness(new_population)
        sorted_idx = np.argsort(new_scores)[::-1]
        population = new_population[sorted_idx[:POP_SIZE]]  # Mantener tamaño
        
        # Guardar información de esta generación
        best_idx = np.argmax(scores)
        historial.append({
            'generacion': gen + 1,
            'mejor_solucion': population[best_idx],
            'aptitud': scores[best_idx],
            'poblacion': population.copy(),
            'aptitudes': scores.copy()
        })

    # Mejor solución encontrada
#    best_idx = np.argmax(fitness(population))
    best_solution = population[best_idx]
    best_fitness = fitness(best_solution)

    return {
        'mejor_final': best_solution,
        'aptitud_final': best_fitness,
        'historial': historial,
        'funcion_objetivo': 'f(x) = x * sin(10πx) + 2',
        'rango_busqueda': [0, 1]
    }