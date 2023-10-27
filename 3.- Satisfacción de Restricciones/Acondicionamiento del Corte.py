# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 22:56:16 2023

@author: User
"""

def normalize_signal(signal):
    # Calcula el valor máximo y mínimo en la señal
    max_value = max(signal)
    min_value = min(signal)
    
    # Normaliza la señal en un rango de 0 a 1
    normalized_signal = [(x - min_value) / (max_value - min_value) for x in signal]
    
    return normalized_signal

# Ejemplo de uso
input_signal = [10, 20, 30, 40, 50]
normalized_signal = normalize_signal(input_signal)
print(normalized_signal)
#Este código calcula el valor máximo y mínimo en la señal de entrada y luego normaliza los valores para que estén en un rango de 0 a 1. Puedes adaptar este código a tus necesidades específicas de acondicionamiento de señales.

#Si tienes un tipo de señal o acondicionamiento en mente, por favor proporciona más detalles para que pueda ayudarte a crear un código más específico.