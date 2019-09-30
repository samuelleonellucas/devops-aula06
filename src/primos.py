Numero = int(input("Numeros: "))

NumeroInit = 1
NumeroPrimo = []
while True:
    if Numero <= 0:
        break
    if NumeroInit > 1:
        for i in range(2,NumeroInit):
            if (NumeroInit % i) == 0:
                break
        else:
            NumeroPrimo.append(NumeroInit)
    if (len(NumeroPrimo) == Numero):
        print(NumeroPrimo)
        break
    else:
        NumeroInit = NumeroInit + 1
        