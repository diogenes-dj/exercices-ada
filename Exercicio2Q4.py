lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]

lista_final = []

for item in lista_inicial:

    if item % 2 == 0:

        if item < 0:

            lista_final.append(-item) #A
    
        else:

            lista_final.append(item) #B
    else:

        if item < 0:
            
            lista_final.append(-2*item) #C
    
        else:

            lista_final.append(2*item) #D