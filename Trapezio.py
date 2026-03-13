import math

def valida_int(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("Digite apenas valores inteiros!")


xmin = valida_int("Informe o limite inferior de X: ")
xmax = valida_int("Informe o limite superior de X: ")
ymin = valida_int("Informe o limite inferior de Y: ")
ymax = valida_int("Informe o limite superior de Y: ")

if xmin >= xmax or ymin >= ymax:
    print("Os valores mínimos devem ser menores que os máximos.")
    exit()

# Definição do SRU

largura = xmax - xmin + 1
altura = ymax - ymin + 1

def criar_matriz():
    return [["." for _ in range(largura)] for _ in range(altura)]

# Estruturas de dados

#Pontos estruturados via geogebra -> Tem que ser no mínimo 25x30 para visualizar
pontos = [
    (10,3), (2,3), (6,8), (2,8), #Trapézio retângulo
    (15,3), (17,3), (18,8), (13,8), #Trapézio isósceles
    (23,3), (32,3), (30,8), (24,8) #Trapézio escaleno
]

arestas = [
    (0,1), (1,2), (2,3), (3,0),
    (4,5), (5,6), (6,7), (7,4),
    (8,9), (9,10), (10,11), (11,8)
]

faces = [
    (0,1,2,3),
    (4,5,6,7),
    (8,9,10,11)
]

# Operações geométricas

def transladar_pontos(pontos, dx, dy):
    novos = []
    for (x, y) in pontos:
        novos.append((x + dx, y + dy))
    return novos

# Renderização

def desenhar_pontos(pontos, matriz):
    for (px, py) in pontos:
        col = px - xmin
        lin = ymax - py
        if 0 <= lin < altura and 0 <= col < largura:
            matriz[lin][col] = "X"

# Consultas

def mapear_arestas(pontos, arestas):
    print("\nMAPEAMENTO DE ARESTAS:\n")
    for i, (p1, p2) in enumerate(arestas):
        x1, y1 = pontos[p1]
        x2, y2 = pontos[p2]
        comprimento = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        print(f"E{i}: ({x1},{y1}) -> ({x2},{y2}) | Comprimento = {comprimento:.2f}")

# Impressão da estrutura

def imprimir_estrutura(pontos, arestas, faces, matriz):
    print("\n" + "="*50)
    print("ESTRUTURA DO OBJETO - TRÊS TRAPÉZIOS")
    print("="*50)

    print("\nLISTA DE PONTOS:")
    for i, p in enumerate(pontos):
        print(f"P{i}: {p}")

    print("\nLISTA DE ARESTAS:")
    for i, (p1, p2) in enumerate(arestas):
        print(f"E{i}: P{p1} -> P{p2}")

    print("\nLISTA DE FACES:")
    for i, f in enumerate(faces):
        print(f"F{i}: {f}")

    print("\nMATRIZ DO SRU:")
    for linha in matriz:
        print(" ".join(linha))

    print("="*50)

matriz = criar_matriz()
desenhar_pontos(pontos, matriz)
imprimir_estrutura(pontos, arestas, faces, matriz)
mapear_arestas(pontos, arestas)

dx = valida_int("\nInforme o deslocamento em X (dx): ")
dy = valida_int("Informe o deslocamento em Y (dy): ")

pontos = transladar_pontos(pontos, dx, dy) #Criemos uma nova matriz, não mudar antiga

 
matriz = criar_matriz()
desenhar_pontos(pontos, matriz)

print("\nAPÓS TRANSLAÇÃO:")
imprimir_estrutura(pontos, arestas, faces, matriz)
