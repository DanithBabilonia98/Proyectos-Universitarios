def Costo(): 
    f = int(input("¿Cuánto cuesta 1 segundo de comunicacion? "))
    n = int(input("¿Cuántas comunicaciones hubo? "))
    for x in range(n):
        hs =int(input("¿Cuántas horas habló "))
        minut = int(input("¿Cuántos minutos habló? "))
        seg =int(input("¿Cuántos segundos habló? "))
        segsal = 3600 * hs + 60 * minut + seg
        costo = segsal * f
        print ("Costo : ",costo, "$.")
 
 
Costo()
