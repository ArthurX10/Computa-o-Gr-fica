def rotacionar_pontos(pontos, angulo_graus, cx = 0, cy = 0):

    theta = np.radians(angulo_graus) # transforma em radianos
    c, s = np.cos(theta), np.sin(theta) # calcula o sen e o cos

    R = np.array([
        [c, -s],
        [s,  c]
    ])

    novos_pontos = []
    for (x, y) in pontos:
        ponto = np.array([x, y]) 
        rotacionado = R @ ponto # é um multiplicador de matrizes do numpy
        novo_x = round(rotacionado[0] + cx)
        novo_y = round(rotacionado[1] + cy)
        novos_pontos.append((novo_x, novo_y))

    return novos_pontos
