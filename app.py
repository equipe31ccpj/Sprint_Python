import random

potencia_por_carregador = 22
potencia_max_posto = 100


carros = [
    ['BYD', 'Dolphin'],
    ['Ford', 'Mustang Mach-E'],
    ['Nissan', 'Leaf'],
    ['GWM', 'Ora 03'],
    ['Volvo', 'EX30'],
    ['BMW', 'i4'],
    ['Renault', 'Kwid E-Tech'],
    ['Chevrolet', 'Bolt EV'],
    ['Porsche', 'Taycan'],
    ['Audi', 'e-tron']
]

def escolher_carro():
    return random.choice(carros)

