#--Crea un script que dada una lista de listas M (numérica), identifique si se trata de una matriz y en ese caso imprima dos 
# listas correspondientes a:
#--1. La fila cuyos elementos suman el máximo
#--2. La columna cuyos elementos suman el máximo
m1=[[20,1,10],[6,1,8],[7,5,4]]
#m2=[[4,2,3],[4,5],[6,8,2]]

sumafila=[0] * len(m1)
sumacolumna=[0] * len(m1[0])

#--comprobamos si es una matriz para ello tiene que tener la misma cantidad de números en todas las filas
if len(m1[0])==len(m1[1])==len(m1[2]):
    #Recorremos con un bucle anidado las listas dentro de las listas para sacar el sumatorio
    for i in range(len(m1)):
        for x in range(len(m1[0])):
            sumafila[i] = sumafila[i] + m1[i][x]
            sumacolumna[x] = sumacolumna[x] + m1[i][x]
print(sumafila)
print(sumacolumna)

indicefila=sumafila.index(max(sumafila))
print(indicefila)
l1=m1[indicefila]
print(l1)

indicelumna=sumacolumna.index(max(sumacolumna))
l2=[m1[i][indicelumna] for i in range(len(m1))]
print(l2)