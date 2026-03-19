def muda_escala(fatX, fatY):
    
    #global pontos
    
    for i in range(0,12):
        temp = pontos[i]
        pontos[i] = (temp[0]*fatX , temp[1]*fatY)
