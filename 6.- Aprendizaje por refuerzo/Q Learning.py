# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 01:01:59 2023

@author: User
"""

import numpy as np
import gym

# Crear el entorno FrozenLake
env = gym.make('FrozenLake-v1')

# Inicializar la tabla Q con ceros
Q = np.zeros([env.observation_space.n, env.action_space.n])

# Hiperparámetros
learning_rate = 0.8
discount_factor = 0.95
num_episodes = 10000

for episode in range(num_episodes):
    state = env.reset()
    done = False

    while not done:
        # Elige una acción mediante epsilon-greedy
        if np.random.rand() < 0.5:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state, :])

        # Realiza la acción y obtén la nueva recompensa y estado
        new_state, reward, done, _ = env.step(action)

        # Actualiza la tabla Q con la ecuación de Bellman
        Q[state, action] = (1 - learning_rate) * Q[state, action] + learning_rate * (reward + discount_factor * np.max(Q[new_state, :]))

        state = new_state

# Imprime la tabla Q resultante
print(Q)
#laro, puedo proporcionarte un ejemplo básico de código en Python para implementar el algoritmo de Q-Learning. El Q-Learning es un algoritmo de aprendizaje por refuerzo que se utiliza para aprender una política óptima en un entorno basado en recompensas. 
#Este código entrena un agente en el entorno FrozenLake utilizando Q-Learning. Después de un número especificado de episodios, la tabla Q contendrá los valores de calidad aprendidos que representan la política óptima. Ten en cuenta que este es un ejemplo simple y que el rendimiento y la convergencia del algoritmo pueden depender de los hiperparámetros y la complejidad del entorno. Puedes ajustar estos valores según tus necesidades y explorar otros entornos de Gym para experimentar con Q-Learning.




