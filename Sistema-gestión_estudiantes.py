import csv
import os
import msvcrt

#leer información del csv
estudiantes = ""
with open('datos_estudiantes.csv', newline='', encoding='utf-8') as a:
    datos = csv.reader(a, delimiter=',')
    estudiantes = list(datos)

while True:
    print ('<<Presione una tecla para continuar>>')
    msvcrt.getch()
    os.system('cls')

    print('''
Sistema de gestión de estudiantes
*********************************
1) Ver listado de estudiantes
2) Buscar estudiante
3) Agregar estudiante
0) SALIR''')
    opcion = input('Seleccione : ')
    if opcion=='0':
        break
    elif opcion =='1':
        print('\033[33mListado de estudiantes\033[0m')
        for i in range(1,len(estudiantes)):
            print (f'{i}.- {estudiantes[i][0]}\tNotas: {estudiantes[i][1]} | {estudiantes[i][2]}| {estudiantes[i][3]}') 
    elif opcion =='2':
        print('\033[33mBuscar estudiante\033[0m')
        nombre = input('Ingrese nombre para buscar : ')
        centinela = False
        for est in estudiantes:
            if est [0]==nombre:
                promedio = (float(est[1])+ float(est[2])+ float(est[3]))/3
                print(f"Estudiamte encontrado {est[0]} {est[1]} {est[2]} {est[3]} promedio {round(promedio,1)}")
                centinela = True
        if not centinela:
            print('\033[31mEstudiante no encontrado\033[0m')
    elif opcion =='3':
        print('\033[33mAgregar estudiante\033[0m')
        nombre  =input("Ingrese nombre y apellido : ")
        if len(nombre)>=5:
            nota1 = float(input("Ingrese nota 1 : "))
            nota2 = float(input("Ingrese nota 2 : "))
            nota3 = float(input("Ingrese nota 3 : "))
            estudiantes.append([nombre, nota1, nota2, nota3])
            print('\033[32mEstudiante registrado\033[0m')

            #Guardar los estudiantes nuevos en el csv
            with open('datos_estudiantes.csv', 'w', newline='', encoding='utf-8') as a:
                escribir = csv.writer(a, delimiter=',')
                escribir.writerows(estudiantes)
        else:
            print('\033[31Nombre inválido\033[0m')
    else:
        print('\033[31mOpción inválida\033[0m')