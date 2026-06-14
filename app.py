import random

qnt_carros_no_posto = 0
carros_no_posto = []
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

def adicionar_carro():
    global carros_no_posto
    global qnt_carros_no_posto
    marca, modelo = escolher_carro()
    carro = f"{marca} {modelo}"
    carros_no_posto.append(carro)
    qnt_carros_no_posto += 1

    return carros_no_posto, qnt_carros_no_posto

def calcular_potencia_por_carro(qnt_carros_no_posto):
    global potencia_max_posto
    global potencia_por_carregador
    potencia_desejada = qnt_carros_no_posto * potencia_por_carregador
    if potencia_desejada <= potencia_max_posto:
        potencia_por_carro = potencia_por_carregador
    else:
        potencia_por_carro = potencia_max_posto / qnt_carros_no_posto

    return potencia_por_carro
    

