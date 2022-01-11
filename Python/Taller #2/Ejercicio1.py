while True:
    try:        
        number1=int(input("Ingrese un número entero "))
        number2=int(input("Ingrese otro número entero "))
        for i in range(number1,number2+1):
            if i %2 ==0:
                print("EL número ",i," par")                
    except ValueError:
         print("valor ingresado no es válido.")