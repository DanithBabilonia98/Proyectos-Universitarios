def contVocal(cadena):
    vocal = 0
    for c in cadena:
        if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c =='O' or c == 'U':
            vocal=vocal+1
    return vocal


cadena = input('Ingrese una palabra, texto  : ')
print("las vocales en esta palabra son :", contVocal(cadena))