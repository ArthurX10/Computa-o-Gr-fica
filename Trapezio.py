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

largura = xmax - xmin + 1
altura = ymax - ymin + 1

def criar_matriz():
    return [["." for _ in range(largura)] for _ in range(altura)]


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

def marcar_origem(matriz):
    col = 0 - xmin
    lin = ymax - 0

    if 0 <= lin < altura and 0 <= col < largura:
        matriz[lin][col] = "O"

def transladar_pontos(pontos, dx, dy):
    novos = []
    for (x, y) in pontos:
        novos.append((x + dx, y + dy))
    return novos

def desenhar_pontos(pontos, matriz):
    for (px, py) in pontos:
        col = px - xmin
        lin = ymax - py
        if 0 <= lin < altura and 0 <= col < largura:
            matriz[lin][col] = "X"

def desenhar_linhas(matriz, ponto, aresta):
    """Desenha as arestas unindo os pontos na matriz"""
    for p1_idx, p2_idx in aresta:
        x1, y1 = ponto[p1_idx]
        x2, y2 = ponto[p2_idx]
        
        # Algoritmo de desenho de linha simples
        passos = max(abs(x2 - x1), abs(y2 - y1))
        if passos == 0: continue
        
        x_inc = (x2 - x1) / passos
        y_inc = (y2 - y1) / passos
        
        curr_x, curr_y = x1, y1
        for _ in range(passos + 1):
            col = round(curr_x) - xmin
            lin = ymax - round(curr_y)
            if 0 <= lin < altura and 0 <= col < largura:
                matriz[lin][col] = 'x'
            curr_x += x_inc
            curr_y += y_inc

def mapear_arestas(pontos, arestas):
    print("\nMAPEAMENTO DE ARESTAS:\n")
    for i, (p1, p2) in enumerate(arestas):
        x1, y1 = pontos[p1]
        x2, y2 = pontos[p2]
        comprimento = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        print(f"E{i}: ({x1},{y1}) -> ({x2},{y2}) | Comprimento = {comprimento:.2f}")

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

# EXECUÇÃO

while True:
    m = criar_matriz()
    
    marcar_origem(m)
    desenhar_linhas(m, pontos, arestas)
    
    imprimir_estrutura(pontos, arestas, faces, m)
    mapear_arestas(pontos, arestas)

    print("\n--- MOVIMENTAR OBJETO ---")
    dx = valida_int("Informe o deslocamento em X (dx): ")
    dy = valida_int("Informe o deslocamento em Y (dy): ")

    novos_pontos = []
    for (px, py) in pontos:
        novos_pontos.append((px + dx, py + dy))
    pontos = novos_pontos
