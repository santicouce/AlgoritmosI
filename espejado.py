def espejado():
    """Me devuelve una lista con los granos de arena que tiene cada celda, una vez espejado"""
    #me da original y espejado horizontal#
    dic={(1,1): 1,(2,0): 2} #vendria de otra funcion
    lista=[]
    lista_primer_espejado=[]
    dic_primer_espejado={} #Primero espejado 
    cantidad_filas=3  #vendria de otra funcion
    cantidad_columnas=2  #vendria de otra funcion
    veces_a_espejar=2 #vendria de otra funcion
    contador=veces_a_espejar
    
    while veces_a_espejar>0: #De todos modos funciona para espajar 1 vez
            for keys in dic: 
                posicion_columna=keys[1]+1
                columna_espejada=2*(cantidad_columnas+1)-posicion_columna-1 
                columna=columna_espejada-1
                posicion_espejada=(keys[0],columna)
                dic_primer_espejado[posicion_espejada]=dic[keys]
           
            veces_a_espejar-=1
     #Este dic tiene las posiciones originales de los monticulos y sus posiciones espejadas
    dic.update(dic_primer_espejado)
    for x in range (0,cantidad_filas):
                for y in range (0,cantidad_columnas*contador):
                    clave=dic.get((x,y),0)
                    lista.append(clave)

    print(lista) #esta lista seria 1 espejado 

