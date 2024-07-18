import random, csv
from statistics import geometric_mean
trabajadores = [ 'Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','Miguel Sánchez','Isabel Gómez','Francisco Díaz', 'Elena Fernández']
trabajadoresConSaldo = {}
Reportefinal={}
def menu():
    print('-'*39)
    print('-'*10,'Analisis de datos','-'*10)
    print('-'*39)
    print('1. Asignar sueldos aleatorios')
    print('2. Clasificar sueldos')
    print('3. Ver estadísticas.')
    print('4. Reporte de sueldos')
    print('5. Salir del programa')


def Opuno():
    for i in trabajadores:
        trabajadoresConSaldo[i] = random.randrange(300000,2500000,510)
    print('Trabajadores añadidos exitosamente')

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
    print("\nSueldos ", text, contador)
    print('\nNombre empleado     Sueldo')
    for a,b in clasifisueldos.items():
        aa=len(a)
        aa=18-aa
        print(a,' '*aa,'$',b)

def Optres(tipo):
    saldos=list(trabajadoresConSaldo.values())
    if tipo==1:
        a='Sueldo mas alto: '
        SaldoFinality=max(saldos)
    if tipo==2:
        a='Sueldo mas bajo: '
        SaldoFinality=min(saldos)
    if tipo==3:
        a='Promedio de sueldos: '
        SaldoFinality=round(sum(saldos)/len(saldos))
    if tipo==4:
        a='Media geometrica: '
        try:
            SaldoFinality=geometric_mean(saldos)
        except:
            SaldoFinality=0
    print('\n- ',a,SaldoFinality)
def Opcuatro():
    for emple, sald in trabajadoresConSaldo.items():
        Reportefinal[emple]=[sald,round(sald*0.07),round(sald*0.12),sald-round(sald*0.07+sald*0.12)]
        bla={'Nombre empleado': ['Sueldo base','Descuento Salud','Descuento AFP','Sueldo Liquido']}
        print(bla)
        print(Reportefinal)
        report=Reportefinal.items()
        with open("Reporte Financiero.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(report)
        print("\nReporte guardado exitosamente...")
        print("\nReporte Financiero: ")
        with open('Reporte Financiero.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
        for row in rows:
            print(row)



while True:
    menu()
    e=int(input("Ingrese una opcion: "))
    if e == 1:
        Opuno()
    elif e ==2:
        acumulador=0
        Opdos('a')
        Opdos('b')
        Opdos('c')
        print('\nTOTAL SUELDOS: $', acumulador)
    elif e == 3:
        Optres(1)
        Optres(2)
        Optres(3)
        Optres(4)
    elif e == 4:
        Opcuatro()
    elif e == 5:
        print('Saliendo del programa...')
        print("David Salazar")
        print('22.082.698-8')
        break
    else:
        print("Eleccion incorrecta...")
