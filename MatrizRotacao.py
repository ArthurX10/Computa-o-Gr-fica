#dentro do switch vai ter que colocar uma linha para coletar o angulo para a rotação do trapezio
angulo = valida_int("O valor do angulo que você deseja rotacionar: ")
def matrizRotacao(pontos, angulo): 
  print("\nMatriz de Rotação\n")
   theta = np.radians(angulo_graus)
  #criar um for para calcular todos os pontos
   c, s = np.cos(theta), np.sin(theta)
   R = np.array(((c, -s) (s, c)))

   return np.dot(R, ponto)

   ponto = np.array((1, 0))
