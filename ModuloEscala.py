'''
def muda_escala(ponto, fatorX, fatorY):
    ponto[0] *= fatorX
    ponto[1] *= fatorY
    print(ponto)

muda_escala([2,5], 8, 9)

pontos = [
    (3,4), (6,4), (5,8), (4,8),
    (9,4), (12,4), (11,8), (10,8),
    (15,4), (18,4), (17,8), (16,8)
]
'''

def escalada(figura, fatorX, fatorY):
    nova_figura = []
    for (x,y) in figura:
        nova_figura.append((x*fatorX, y*fatorY))
    print(nova_figura)
    
#escalada(pontos, 8, 9)
