#Compara los numeros adyacentes, cada elemento burbujea hasta el lugar que pertenece, compara los valores de 2 en 2 cada vez que sigue el ciclo

def bubbleSort(nlist):
    #! Importante! Aqui buscamos el numero maximo de la lista menos uno porque no hay otro numero luego de este
    for passnum in range(len(nlist)-1,0,-1):
        #Creamos otro iterador que pasa sobre el rango de la lista de la lista
        for i in range(passnum):
            #Aqui comparamos el valor de la izquierda con el de la derecha. Si es mayor lo ponemos en la variable temp
            #y en las otras lineas de abajo las intercambiamos
            if nlist[i]>nlist[i+1]:
                temp=nlist[i]
                nlist[i]=nlist[i+1]
                nlist[i+1]=temp

    # Lista de numeros desorganizados
    nlist=[80,1007,13,16,53,71,42,61,45,20,70]
    #Llamamos a la funcion
    bubbleSort(nlist)

    #Imprimimos la lista que ahora tendra los numeros organizados
    print(nlist)