def conversion():
    dolares= pesoColombiano / 3000
    print("Los pesos colombianos en dolares son :", dolares) 

    euros= pesoColombiano / 3522.48
    print("Los pesos colombianos en euros son :", euros)

    bitcoins= pesoColombiano / 11800249.20
    print("Los pesos colombianos en bitcoins son :", bitcoins)

pesoColombiano= float(input("Ingrese una cantidad en peso colombiano \n"))

conversion()