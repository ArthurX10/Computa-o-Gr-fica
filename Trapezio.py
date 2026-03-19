import math
import numpy as np

def valida_int(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("Digite apenas valores inteiros!")

def refletir_figura(pontos, opcao):

    matrizes = {
        1: [[1, 0], [0, -1]], 
        2: [[-1, 0], [0, 1]], 
        3: [[-1, 0], [0, -1]] 
    }

    if opcao not in matrizes:
        print("Opção de reflexão inválida.")
        return pontos

    matriz = matrizes[opcao]
    novos_pontos = []

    for x, y in pontos:
        novo_x = (matriz[0][0] * x) + (matriz[0][1] * y)
        novo_y = (matriz[1][0] * x) + (matriz[1][1] * y)
        novos_pontos.append((novo_x, novo_y))

    print("Reflexão aplicada")
    return novos_pontos

def cisalhar_figura(pontos, opcao, c):
    novos_pontos = []

    for (px, py) in pontos:

        if opcao == 1:
            x_att = px + c * py
            y_att = py

        elif opcao == 2:
            x_att = px #bug aq
            y_att = py + c * px

        elif opcao == 3:
            x_att = px + c * py #bug aq
            y_att = py + c * px

        else:
            print("Opção inválida!")
            return pontos

        novos_pontos.append((x_att, y_att))

    print("Cisalhamento aplicado")
    return novos_pontos

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

#OBJETO
pontos = [
    (2, 3), (16, 3), (10, 11), (2, 11),  
    (38, 3), (41, 3), (43, 11), (35, 11),  
    (60, 3), (75, 3), (69, 11), (63, 11)  
]

arestas = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (8, 9), (9, 10), (10, 11), (11, 8)
]

faces = [
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (8, 9, 10, 11)
]

pontos_atuais = pontos.copy() 

def desenhar_eixos(matriz):
    lin_zero = ymax - 0
    col_zero = 0 - xmin

    for i in range(altura):
        for j in range(largura):

            if 0 <= lin_zero < altura and i == lin_zero:
                matriz[i][j] = '-'

            if 0 <= col_zero < largura and j == col_zero:
                matriz[i][j] = '|'

    if 0 <= lin_zero < altura and 0 <= col_zero < largura:
        matriz[lin_zero][col_zero] = 'O'



def transladar_pontos(pontos, dx, dy):
    novos = []
    for (x, y) in pontos:
        novos.append((x + dx, y + dy))
    return novos


def desenhar_pontos(pontos, matriz):
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i, (px, py) in enumerate(pontos):
        col = px - xmin
        lin = ymax - py

        if 0 <= lin < altura and 0 <= col < largura:
            if i < len(letras):
                matriz[lin][col] = letras[i]
            else:
                matriz[lin][col] = "*"


def desenhar_linhas(matriz, ponto, aresta):
    """Desenha as arestas unindo os pontos na matriz"""
    for p1_idx, p2_idx in aresta:
        x1, y1 = ponto[p1_idx]
        x2, y2 = ponto[p2_idx]

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


def imprimir_estrutura(pontos, arestas, faces, matriz):
    print("\n" + "=" * 50)
    print("ESTRUTURA DO OBJETO - TRÊS TRAPÉZIOS")
    print("=" * 50)

    
    print("\nMATRIZ DO SRU:")
    for linha in matriz:
        print(" ".join(linha))

    
# EXECUÇÃO

while True:
    m = criar_matriz()

    desenhar_eixos(m)
    desenhar_linhas(m, pontos_atuais, arestas)
    desenhar_pontos(pontos_atuais, m)

    imprimir_estrutura(pontos_atuais , arestas, faces, m)
   

    print("\n" + "=" * 50)
    print("MENU DE TRANSFORMAÇÕES")
    print("1. Movimentar Objeto (Translação)")
    print("2. Espelhar Objeto (Reflexão)")
    print("3. Rotacionar Objeto (Rotação)")
    print("4. Escalonar Objeto (Escala)")
    print("5. Cisalhar Objeto (Cisalhamento)")
    print("6. Imprimir Objeto original")
    print("7. Redefinir Objeto atual")
    print("0. Sair")

    escolha = valida_int("Escolha a transformação desejada: ")

    if escolha == 1:
        print("\n--- MOVIMENTAR OBJETO ---")
        dx = valida_int("Informe o deslocamento em X (dx): ")
        dy = valida_int("Informe o deslocamento em Y (dy): ")
        pontos_atuais = transladar_pontos(pontos_atuais, dx, dy)

    elif escolha == 2:
        print("\n--- OPÇÕES DE REFLEXÃO ---")
        print("1. Eixo X (Inverte Y)")
        print("2. Eixo Y (Inverte X)")
        print("3. Origem (Inverte X e Y)")

        opcao_reflexao = valida_int("Escolha o tipo de reflexão: ")
        pontos_atuais = refletir_figura(pontos_atuais, opcao_reflexao)
        
    elif escolha == 3:
        #op rotação
        pass
        
    elif escolha == 4:
        #op escala
        pass

    elif escolha == 5:
        print("\n--- OPÇÕES DE CISALHAMENTO ---")
        print("1. Em X")
        print("2. Em Y")
        print("3. Em X e em Y")

        opcao_c = valida_int("Informe o tipo de cisalhamento: ")
        c = valida_int("Informe o coeficiente de cisalhamento: ")
        pontos_atuais = cisalhar_figura(pontos_atuais, opcao_c, c)
        

    elif escolha == 6:
        m = criar_matriz()
        desenhar_eixos(m)
        desenhar_linhas(m, pontos, arestas)
        desenhar_pontos(pontos, m)
        imprimir_estrutura(pontos, arestas, faces, m)

    elif escolha == 7:
        pontos_atuais = pontos.copy()
        print("Objeto resetado.")

    elif escolha == 0:
        print("Encerrando...")
        break

    else:
        print("Opção inválida! Escolha um valor válido.")
