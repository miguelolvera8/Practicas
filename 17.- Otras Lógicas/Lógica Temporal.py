#La l�gica temporal es una herramienta importante en la inteligencia artificial, especialmente en la representaci�n del conocimiento y la planificaci�n
# de agentes racionales que interact�an con un entorno a lo largo del tiempo
#Primero, debes instalar la biblioteca "pddlpy" utilizando pip:
#pip install pddlpy



#Supongamos que queremos planificar un viaje en coche desde una ciudad A a una ciudad B. El viaje debe incluir cargar combustible en una gasolinera 
#(G) en alg�n momento antes de llegar a B. Definiremos esta tarea como un problema de planificaci�n en l�gica temporal.


from pddlpy import DomainProblem, state_from_fact, Action, Domain

# Define el dominio
domain = Domain((
    # Predicados
    ('at', 'car', '?from', '?to'),
    ('at', 'gas_station', '?loc'),
    ('has_fuel', 'car'),
    ('route', '?from', '?to'),

    # Acciones
    Action('drive', parameters=(('?from', 'loc'), ('?to', 'loc')),
           condition=(('at', 'car', '?from'), ('route', '?from', '?to'), ('has_fuel', 'car')),
           effect=(('at', 'car', '?to'), ('not', ('at', 'car', '?from')))),

    Action('refuel', parameters=(('?loc', 'loc')),
           condition=(('at', 'car', '?loc'), ('at', 'gas_station', '?loc')),
           effect=(('has_fuel', 'car'),)),
))

# Define el problema
problem = domain.problem(
    "car_problem",
    objects=('car', 'gas_station', 'cityA', 'cityB'),
    initial=(
        ('at', 'car', 'cityA'),
        ('at', 'gas_station', 'cityA'),
        ('route', 'cityA', 'cityB'),
    ),
    goal=(
        ('at', 'car', 'cityB'),
        ('has_fuel', 'car'),
    )
)

# Encuentra un plan
plan = problem.happenings(50)  # Encuentra un plan con un l�mite de 50 pasos

if plan:
    print("Plan encontrado:")
    for action, args in plan:
        print(f"- {action}({', '.join(args)})")
else:
    print("No se encontr� un plan.")

#Este ejemplo utiliza l�gica temporal para planificar un viaje en coche, asegurando que el coche tenga suficiente combustible para llegar a su destino.
# El planificador encuentra una secuencia de acciones que satisfacen los objetivos definidos en el problema.