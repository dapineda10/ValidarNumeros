def FuncionUno():
    numeroUsuario = PedirNumeroUsuario("Cuantos números quiere ingresar")
    contador = 0
    numeroActual = 0
    listaNumeros = []

    while contador < numeroUsuario:
        contador+=1
        numeroActual = PedirNumeroUsuario("Agregue un número")
        
        if CumpleCondiciones(numeroActual):
            print(f"El número {numeroActual} cumple las condiciones del ejercicio 1 punto A.")
        else:
            print(f"El número {numeroActual} no cumple las condiciones del ejercicio 1 punto A.")
            
        if(EsMultiploDe(numeroActual, 5)):
            if(EsMultiploDe(numeroActual, 9)):
                listaNumeros.append(numeroActual)
    
    print("El porcentaje es:" + str(PorcentajeNumeros(len(listaNumeros),numeroUsuario)))

def PedirNumeroUsuario(mensaje):
    num = int(input(f"{mensaje}: "))
    return num

def CumpleCondiciones(numeroActual):
    if(EsMayorQue(numeroActual,333)):
        if EsMultiploDe(numeroActual,9):
            if EsMultiploDe(numeroActual,45) != True:
                return True
    return False

def EsMayorQue(numeroUno, numeroDos):
    return numeroUno > numeroDos

def EsMultiploDe(numeroUno, numeroDos):
    return numeroUno % numeroDos == 0
    
def PorcentajeNumeros(valoresLista, valoresUsuario):
    valorTotal = (valoresLista * 100) / valoresUsuario
    return valorTotal