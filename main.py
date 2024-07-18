import random
trabajadores = [ 'Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','Miguel Sánchez','Isabel Gómez','Francisco Díaz', 'Elena Fernández']
trabajadoresConSaldo = {}
def menu():
    print('-'*39)
    print('-'*10,'Analisis de datos','-'*10)
    print('-'*39)
def Opuno():
    for i in trabajadores:
        trabajadoresConSaldo[i] = random.randrange(300000,2500000,510)
    print(trabajadores)
    print(trabajadoresConSaldo)
def Opdos(tipo):
    contador=0
    global acumulador
    clasifisueldos={}
    if tipo=='a':
        text='menores a $800.000  TOTAL: '
        for clientes, sueldos in trabajadoresConSaldo.items():
            if sueldos<800000:
                clasifisueldos[clientes]=sueldos
                contador=contador+1
                acumulador=acumulador+sueldos
    if tipo=='b':
        text='entre $800.000 y $2.000.000  \nTOTAL: '
        for clientes, sueldos in trabajadoresConSaldo.items():
            if sueldos>=800000 and sueldos<=2000000:
                clasifisueldos[clientes]=sueldos
                contador=contador+1
                acumulador=acumulador+sueldos
    if tipo=='c':
        text='superiores a $2.000.000  \nTOTAL: '
        for clientes, sueldos in trabajadoresConSaldo.items():
            if sueldos>2000000:
                clasifisueldos[clientes]=sueldos
                contador=contador+1
                acumulador=acumulador+sueldos
    print("Sueldos ", text, contador)
    print('\nNombre empleado     Sueldo')
    for a,b in clasifisueldos.items():
        aa=len(a)
        aa=18-aa
        print(a,' '*aa,'$',b)
    print('\nTOTAL SUELDOS: ', acumulador)
    



menu()
Opuno()
acumulador=0
print('-')
Opdos('a')
print('-')
Opdos('b')
print('-')
Opdos('c')
print(acumulador)
