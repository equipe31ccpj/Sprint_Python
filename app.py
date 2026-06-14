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

def remover_carro():
    global carros_no_posto
    global qnt_carros_no_posto
    
    if not carros_no_posto:
        print("O posto já está vazio!")
        return
    
    for indice, carro in enumerate(carros_no_posto):
        print(f'Vaga {indice + 1} -- {carro}')
    print('-' * 20)
    
    selecionar_veiculo = False
    while not selecionar_veiculo:
        try:
            vaga_escolhida = int(input('Digita a vaga do carro a sair: '))
            if 1 <= vaga_escolhida <= len(carros_no_posto):
                indice_remover = vaga_escolhida - 1
                carros_no_posto.pop(indice_remover)
                qnt_carros_no_posto -= 1
                selecionar_veiculo = True
            else:
                print('Vaga inválida! Selecione uma vaga ocupada da lista.')
        except ValueError:
            print('Por favor, digite um número válido.')
    print('Carro removido.')