# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:22:07 2023

@author: Javier
"""

# Definir la matriz de transición de la cadena de Markov
transition_matrix = {
    "A": {"A": 0.7, "B": 0.3},
    "B": {"A": 0.4, "B": 0.6}
}

# Función para realizar inferencia por eliminación de variables
def variable_elimination_inference(transition_matrix, observed_sequence, unobserved_states):
    # Inicializar un diccionario para almacenar las probabilidades marginales de los estados no observados
    marginal_probabilities = {state: 1.0 for state in unobserved_states}
    
    for i in range(len(observed_sequence) - 1):
        current_state = observed_sequence[i]
        next_state = observed_sequence[i + 1]
        
        for state in unobserved_states:
            probability = transition_matrix[state][current_state]
            marginal_probabilities[state] *= probability
    
    # Normalizar las probabilidades marginales
    total_probability = sum(marginal_probabilities.values())
    normalized_probabilities = {state: prob / total_probability for state, prob in marginal_probabilities.items()}
    
    return normalized_probabilities

# Secuencia de observaciones
observed_sequence = ["A", "A", "B", "B"]

# Estados no observados para calcular sus probabilidades marginales
unobserved_states = ["A", "B"]

# Calcular las probabilidades marginales de los estados no observados
marginal_probabilities = variable_elimination_inference(transition_matrix, observed_sequence, unobserved_states)

for state, probability in marginal_probabilities.items():
    print(f"La probabilidad marginal de estar en el estado '{state}' después de la secuencia es: {probability:.4f}")