# Problema de Monty Hall

Simulação computacional do **Problema de Monty Hall**, utilizando Python e geração de resultados aleatórios.

O programa simula **1000 partidas** do problema, sorteando aleatoriamente a posição do carro, a porta escolhida inicialmente e a decisão do jogador de trocar ou não de porta.

---

## Sobre o problema

O Problema de Monty Hall é um problema clássico de probabilidade baseado em um jogo com **3 portas**.

Em cada partida:

1. Existe um carro atrás de uma das três portas.
2. O jogador escolhe uma porta.
3. O apresentador abre uma das outras portas, sabendo onde está o carro.
4. O jogador pode decidir se deseja trocar de porta ou permanecer com sua escolha inicial.
5. O resultado é registrado como vitória ou derrota.

Neste projeto, as escolhas são realizadas automaticamente utilizando números aleatórios.

---

## Tecnologias utilizadas

* **Python 3**
* Biblioteca `random`

A biblioteca `random` é utilizada para realizar os sorteios das portas.

---

## Funcionamento do programa

### 1. Sorteio do carro

A posição do carro é definida aleatoriamente entre as portas 1, 2 e 3:

```python
carro = random.randint(1, 3)
```

---

### 2. Escolha inicial

A escolha inicial do jogador também é realizada automaticamente:

```python
escolha = random.randint(1, 3)
```

Dessa forma, não é necessário digitar a escolha manualmente durante a simulação.

---

### 3. Escolha do apresentador

A função `escolha_apresentador()` verifica quais portas podem ser abertas pelo apresentador.

A porta escolhida pelo jogador e a porta onde está o carro não podem ser selecionadas.

```python
def escolha_apresentador():
    for porta in portas:
        if porta != escolha and porta != carro:
            portas_escolhida.append(porta)

    porta_selecionada = random.choice(portas_escolhida)

    return portas_escolhida, porta_selecionada
```

A função retorna:

* As portas que poderiam ser selecionadas;
* A porta selecionada aleatoriamente pelo apresentador.

---

### 4. Descoberta da porta para troca

A função `segunda_escolha()` cria uma cópia das três portas e remove:

* A porta escolhida inicialmente pelo jogador;
* A porta aberta pelo apresentador.

A porta restante é a opção disponível para troca.

```python
def segunda_escolha():
    portas_copia = [1, 2, 3]

    portas_copia.remove(porta_selecionada)
    portas_copia.remove(escolha)

    trocar_porta = portas_copia[0]

    return trocar_porta
```

---

### 5. Decisão de trocar ou permanecer

A decisão entre trocar ou permanecer é realizada aleatoriamente:

```python
escolha_final = random.choice(["s", "n"])
```

Onde:

* `"s"` = trocar de porta;
* `"n"` = permanecer na porta escolhida inicialmente.

A função `porta_final()` determina qual será a porta utilizada no resultado final:

```python
def porta_final():
    if escolha_final == "s":
        ultima_porta = trocar_porta

    elif escolha_final == "n":
        ultima_porta = escolha

    return ultima_porta
```

---

### 6. Verificação da vitória

A função `verificar_vitoria()` compara a porta final escolhida com a porta onde está o carro.

Se forem iguais, uma vitória é contabilizada. Caso contrário, uma derrota é contabilizada.

```python
def verificar_vitoria():
    global contagem_vitoria
    global contagem_derrota

    if ultima_porta == carro:
        contagem_vitoria += 1
    else:
        contagem_derrota += 1
```

---

## Simulação de 1000 partidas

O programa utiliza um `for` para repetir todo o processo 1000 vezes:

```python
for i in range(1000):
```

A cada rodada são novamente definidos:

* A posição do carro;
* As portas disponíveis;
* A escolha inicial;
* A porta selecionada pelo apresentador;
* A porta disponível para troca;
* A decisão de trocar ou permanecer;
* O resultado da partida.

---

## Resultado

Após as 1000 partidas, o programa exibe a quantidade total de derrotas e vitórias:

```python
print("Derrotas: ", contagem_derrota)
print("Vitorias: ", contagem_vitoria)
```

Um resultado possível seria:

```text
Derrotas:  497
Vitorias:  503
```

Os valores podem mudar a cada execução, pois as escolhas são realizadas aleatoriamente.

---

## Estrutura do projeto

```text
Problema-de-Monty-Hall/
│
└── main.py
```

O arquivo `main.py` contém toda a implementação da simulação.

---

##  Como executar

Certifique-se de ter o Python instalado.

No terminal, entre na pasta do projeto e execute:

```bash
python main.py
```

O programa realizará automaticamente as 1000 partidas e exibirá o número de vitórias e derrotas ao final.

---

## Objetivo do projeto

O objetivo é utilizar programação e geração de números aleatórios para simular o Problema de Monty Hall e observar os resultados obtidos após várias partidas.

A simulação permite analisar, por meio dos resultados, o comportamento do problema de probabilidade em diferentes decisões de troca de porta.

---

## Observação

As funções `escolha_usuario()` e `decisao_usuario()` foram mantidas comentadas no código original.

Elas representam uma versão em que o usuário poderia realizar as escolhas manualmente. Na versão atual da simulação, essas escolhas foram substituídas por valores aleatórios para permitir a execução automática das 1000 partidas.
