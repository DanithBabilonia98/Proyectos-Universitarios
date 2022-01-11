lista = []
cantidad=int(input("cantidad de palabras: "))
i = 1
while cantidad>0 :
	palabra= input("Digite palabra N°"+ str(i)+": ").lower()
	lista.append(palabra)
	i+=1
	cantidad-=1

caracter=input("Digite caracter a ingresar: ").lower()
lista2 = lista[:]
for i in range(len(lista2)):
	lista2[i]=   caracter +lista2[i]

print (lista)