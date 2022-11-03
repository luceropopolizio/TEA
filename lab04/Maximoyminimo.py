try:
    #defino programas
    def mostrarmínimo(m):
        print('\nEl numero mínimo es: ',m)
       
    def mostrarmáximo(M):
        print('\nEl numero máximo es: ',M)

    def pedirdato():
        mínimo=None
        máximo=None
        while True:
            n=input('Ingrese un número: ')
            if n=='fin':
                break
            if máximo is None or n>máximo:
                máximo=n
            if mínimo is None or n<mínimo:
                mínimo=n
        mostrarmáximo(máximo)
        mostrarmínimo(mínimo)
#Comienza Programa
    pedirdato()
#Fin del Programa
except:
    print('\nError!! Ingrese un número o la palabra "fin".\nEl programa ha dinalizado')


