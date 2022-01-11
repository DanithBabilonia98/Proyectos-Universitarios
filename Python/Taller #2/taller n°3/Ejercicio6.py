
def productLista(lista)        :
    if len(lista)==1:
         return lista[0]
    else:
        return lista[0] * productLista(lista[1:])     

numero = int(input("Dígame cuántos valores tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame el valor numérico", str(i + 1) + ": ", end="")
        valor = int(input())
        lista += [valor]

suma= sum(lista,0)
maximo=max(lista)
minimo=min(lista)

print('La suma de los valores de la lista es : ',suma)
print('El producto de los valores de la lista es: ', productLista(lista))
print('El valor máximo es :', maximo, 'y el valor mínimo es: ',minimo)