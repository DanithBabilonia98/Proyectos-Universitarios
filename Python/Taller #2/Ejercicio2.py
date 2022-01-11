num = int(input("introduce un numero "))
 
resultado={}
for i in range(1,num+1):
	resultado[i]=(i*(i+1)/2)
 
for i in resultado:
	print (i,resultado[i])