def dosCaracter():
    cas=cadena[0:2]
    print(cas)

def tresCaracter():
    cad=cadena[:3]
    print(cad)


def cada2Car():
    cad=cadena[::2]
    print(cad)


def invertir():
    cadInvertida= cadena [::-1]     
    print(cadInvertida)

cadena=input('ingrese una palabra :' ) 
dosCaracter()         
tresCaracter() 
cada2Car()
invertir()