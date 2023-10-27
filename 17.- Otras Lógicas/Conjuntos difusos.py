#Los conjuntos difusos son una parte de la teor�a de conjuntos que permiten modelar la incertidumbre y la imprecisi�n en datos y sistemas.
# Puedes implementar conjuntos difusos en diversos lenguajes de programaci�n. Aqu� tienes un ejemplo sencillo en Python utilizando la biblioteca 
# scikit-fuzzy. Aseg�rate de tener esta biblioteca instalada antes de ejecutar el c�digo

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Crear universos de discurso
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')
humedad = ctrl.Antecedent(np.arange(0, 101, 1), 'humedad')
velocidad_ventilador = ctrl.Consequent(np.arange(0, 101, 1), 'velocidad_ventilador')

# Definir conjuntos difusos para temperatura
temperatura['fr�a'] = fuzz.trimf(temperatura.universe, [0, 0, 50])
temperatura['templada'] = fuzz.trimf(temperatura.universe, [25, 50, 75])
temperatura['caliente'] = fuzz.trimf(temperatura.universe, [50, 100, 100])

# Definir conjuntos difusos para humedad
humedad['seca'] = fuzz.trimf(humedad.universe, [0, 0, 50])
humedad['normal'] = fuzz.trimf(humedad.universe, [25, 50, 75])
humedad['h�meda'] = fuzz.trimf(humedad.universe, [50, 100, 100])

# Definir conjuntos difusos para velocidad del ventilador
velocidad_ventilador['baja'] = fuzz.trimf(velocidad_ventilador.universe, [0, 0, 50])
velocidad_ventilador['media'] = fuzz.trimf(velocidad_ventilador.universe, [25, 50, 75])
velocidad_ventilador['alta'] = fuzz.trimf(velocidad_ventilador.universe, [50, 100, 100])

# Definir reglas difusas
regla1 = ctrl.Rule(temperatura['fr�a'] & humedad['seca'], velocidad_ventilador['alta'])
regla2 = ctrl.Rule(temperatura['fr�a'] & humedad['normal'], velocidad_ventilador['media'])
regla3 = ctrl.Rule(temperatura['fr�a'] & humedad['h�meda'], velocidad_ventilador['baja'])

# Crear el sistema de control
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])

# Crear el simulador
simulador = ctrl.ControlSystemSimulation(sistema_control)

# Ingresar valores de temperatura y humedad
simulador.input['temperatura'] = 30
simulador.input['humedad'] = 60

# Realizar la inferencia
simulador.compute()

# Obtener el resultado
print("Velocidad del ventilador:", simulador.output['velocidad_ventilador'])

# Visualizar la salida difusa
velocidad_ventilador.view(sim=simulador)


