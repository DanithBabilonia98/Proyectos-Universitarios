n=int(input('Ingrese un valor '))
cadena=[]
for x in range (n):
    cadena=input("ingrese una cadena \t")

cad=input('¿cuál cadena desea buscar? ')
for cad in cadena:
    Numcar= cadena.count(cad)
    
print(Numcar)
