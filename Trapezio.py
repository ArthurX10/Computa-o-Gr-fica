import math
#Função para que a entrada aceite penas inteiros.
def valida_int(texto):
    cond = True
    while cond:
        try:
            valor = int(input(f"{texto}"))
            cond = False
        except ValueError:
            print("Digite apenas valores inteiros!")
    return valor

xmin = valida_int('Informe o limite inferior de X: ')
xmax = valida_int('Informe o limite superior de X: ')
ymin = valida_int('Informe o limite inferior de Y: ')
ymax = valida_int('Informe o limite superior de Y: ')

if xmin >= xmax or ymin >= ymax:
    print("Os valores minimos devem ser menores que os maximos.")
    exit()

l = xmax - xmin + 1
a = ymax - ymin + 1

m = []

for i in range(a):
    aux = []
    for j in range(l):
        aux.append('.')
    m.append(aux)

ponto = [
         (3,4), (6,4), (5,8), (4,8),     
         (9,4), (12,4), (11,8), (10,8),  
         (15,4), (18,4), (17,8), (16,8)   
        ]

aresta = [
           (0,1), (1,2), (2,3), (3,0),
           (4,5), (5,6), (6,7), (7,4),
           (8,9), (9,10), (10,11), (11,8)
         ]

face = [
        (0,1,2,3),
        (4,5,6,7),
        (8,9,10,11)
       ]

for (px, py) in ponto:
    col = px - xmin
    lin = ymax - py

    if 0 <= lin < a and 0 <= col < l:
        m[lin][col] = 'x'

def mapear_arestas(ponto, aresta):
print("\nMAPEAMENTO DE ARESTAS:\n")

for i,(p1, p2) in enumerate(aresta):
  x1, y1 = ponto[p1]
  x2, y2 = ponto[p2]

  comprimento = math.sqrt(x2 -x1)**2 + (y2 - y1)**2)

  print (f"E{i + 1}: ({x1}, {y1}) -> ({x2}, {y2}) " 
          f" | Comprimento = {comprimento: 2f}")
