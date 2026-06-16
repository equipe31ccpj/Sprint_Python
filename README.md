# Posto de Carregamento Inteligente - GoodWe

Este projeto consiste num sistema de simulação para o gerenciamento de carga de veículos elétricos (VE) num posto de carregamento com restrição de potência total. O software gere de forma dinâmica a distribuição de energia elétrica disponível conforme novos veículos entram ou saem do sistema.

## 🔗 Links do Projeto
* **Dataset / Contexto no Kaggle:** [Insira o link do seu notebook ou dataset do Kaggle aqui](https://trello.com/invite/b/6a306ab418c4a232b8bde17d/ATTI88d7fb4ee7d8dbdcc1ca5a3e40e883201496525B/sprint-1-ano-pensamento-computacional-e-automacao-com-python)

---

## 🚀 Funcionalidades

* **Entrada Automatizada de Veículos:** Adiciona veículos elétricos aleatórios de uma lista pré-definida de marcas e modelos populares (BYD, GWM, Volvo, Porsche, etc.).
* **Saída Controlada por Vaga:** Permite remover um veículo libertando a vaga específica informada pelo utilizador.
* **Gerenciamento Dinâmico de Potência (Smart Charging):** Calcula em tempo real a potência disponível para cada veículo, respeitando o limite físico da infraestrutura elétrica do posto.

---

## 📊 Regra de Negócio e Distribuição de Potência

O posto opera com parâmetros fixos simulando limitações reais de uma rede elétrica:
* **Potência Máxima do Posto:** 100 kW
* **Potência Nominal por Carregador:** 22 kW

### Lógica de Divisão de Carga:
O algoritmo analisa a demanda total combinada para evitar a sobrecarga do disjuntor principal:
1. **Até 4 veículos:** Cada veículo recebe a potência máxima do carregador de **22 kW** (Demanda máxima de 88 kW $\le$ 100 kW).
2. **A partir de 5 veículos:** A demanda desejada ultrapassa a capacidade do posto ($5 \times 22 = 110\text{ kW}$). O sistema entra em modo de proteção e **divide igualmente os 100 kW** disponíveis pela quantidade atual de carros conectados.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Biblioteca `random`:** Para simulação da chegada de modelos aleatórios.
* **Biblioteca `sys`:** Para encerramento seguro do terminal.

---

## 💻 Como Executar o Projeto

1. Certifique-se de ter o Python instalado na sua máquina.
2. Clone o repositório ou descarregue o arquivo do script:
   ```bash
   git clone [https://github.com/equipe31ccpj/Sprint_Python.git](https://github.com/equipe31ccpj/Sprint_Python.git)
   ```
3. Navegue até à pasta do arquivo e execute:
   ```bash
   python app.py
   ```

👥 Integrantes do Grupo
Akin — Análise de dados / Kaggle

Maria — Elaboração da ideia e escopo

Pedro — Desenvolvimento do código-fonte