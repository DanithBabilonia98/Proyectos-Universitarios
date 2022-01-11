lista=[]
valor=int(input("Ingresar valor (presiona -1 para finalizar):"))
while valor!= -1:
    lista.append(valor)
    valor=int(input("Ingresar valor (-1 para finalizar):"))

unicos=[] 
repetidos=[]   
for i in lista:
    if i not in unicos:
       unicos.append(i)
    else:
        if i not in repetidos:
            repetidos.append(i)

print("Lista anterior :", lista)
print("elementos unicos de la  lista:", unicos)
print("elementos repetidos de la  lista:", repetidos)
