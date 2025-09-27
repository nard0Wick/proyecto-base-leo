from clases.avanzadas import Operaciones

def main():
    op = Operaciones()
    op.leerNumeros()
    op.elevarPotencia()
    op.mostrarResultado()
    
    #Llamar a la función raíz cuadrada
    op.raiz()
    op.mostrarResultado()

if __name__ == "__main__":
    main()
    