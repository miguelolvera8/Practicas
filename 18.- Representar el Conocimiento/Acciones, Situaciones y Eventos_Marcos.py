# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:55:15 2023

@author: EliteDesk
"""

class MarcoEvento:
    def __init__(self, nombre, participantes, fecha, lugar):
        self.nombre = nombre
        self.participantes = participantes
        self.fecha = fecha
        self.lugar = lugar
    
    def mostrar_informacion(self):
        print(f"Evento: {self.nombre}")
        print(f"Participantes: {', '.join(self.participantes)}")
        print(f"Fecha: {self.fecha}")
        print(f"Lugar: {self.lugar}")
        print("\n")

# Crear instancias de marcos de eventos
evento1 = MarcoEvento("Reunión de Equipo", ["Alice", "Bob", "Charlie"], "2023-11-01", "Sala de Conferencias")
evento2 = MarcoEvento("Concierto", ["Eva", "David", "Emma"], "2023-12-15", "Estadio")

# Mostrar información de los eventos
evento1.mostrar_informacion()
evento2.mostrar_informacion()

class MarcoSituacion:
    def __init__(self, descripcion, personas_involucradas, ubicacion):
        self.descripcion = descripcion
        self.personas_involucradas = personas_involucradas
        self.ubicacion = ubicacion
    
    def mostrar_situacion(self):
        print(f"Situación: {self.descripcion}")
        print(f"Personas involucradas: {', '.join(self.personas_involucradas)}")
        print(f"Ubicación: {self.ubicacion}")
        print("\n")

# Crear instancias de marcos de situaciones
situacion1 = MarcoSituacion("Almuerzo en el Restaurante", ["Alice", "Bob", "Charlie"], "Restaurante XYZ")
situacion2 = MarcoSituacion("Reunión de Emergencia", ["Eva", "David", "Emma"], "Oficina Principal")

# Mostrar información de las situaciones
situacion1.mostrar_situacion()
situacion2.mostrar_situacion()

class MarcoAccion:
    def __init__(self, nombre, actor, objetivo, resultado):
        self.nombre = nombre
        self.actor = actor
        self.objetivo = objetivo
        self.resultado = resultado
    
    def mostrar_accion(self):
        print(f"Acción: {self.nombre}")
        print(f"Actor: {self.actor}")
        print(f"Objetivo: {self.objetivo}")
        print(f"Resultado: {self.resultado}")
        print("\n")

# Crear instancias de marcos de acciones
accion1 = MarcoAccion("Enviar Correo Electrónico", "Alice", "Bob", "Correo enviado con éxito")
accion2 = MarcoAccion("Presentar Informe", "Eva", "Equipo Directivo", "Informe aprobado")

# Mostrar información de las acciones
accion1.mostrar_accion()
accion2.mostrar_accion()
