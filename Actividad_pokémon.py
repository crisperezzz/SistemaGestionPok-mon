import csv
import os
import msvcrt
pokemon = ""
with open('pokemon_primera_generacion(1).csv', newline='', encoding='utf-8') as f:
    data  = csv.reader(f, delimiter=',')
    pokemon = list(data)
cinturon = []

while True:
    print ("<<Presione una tecla para continuar>>")
    msvcrt.getch()
    os.system("cls")

    print("""
------------------------------------------
1. Mostrar todos los Pokémon disponibles.
2. Buscar un Pokémon por nombre.
3. Agregar un Pokémon al cinturón.
4. Mostrar los Pokémon en el cinturón.
5. Quitar un Pokémon en el cinturón.
6. Generar reporte de cinturon a CSV.
0. Salir.
------------------------------------------""")
    opcion = int(input("Seleccione una opción : "))

    if opcion==0:
        break
    elif opcion ==1:
        print("\033[34mMostrar todos los Pokémon disponibles\033[0m")
        for i in range (1,len(pokemon)):
            if len(pokemon[i][1])>9:
                print(f"{i}.- {pokemon[i][1]} \t  |Tipo: {pokemon[i][2]}  |Altura: {pokemon[i][3]}  |Peso: {pokemon[i][4]}")
            else:
                print(f"{i}.- {pokemon[i][1]} \t\t  |Tipo: {pokemon[i][2]} | Altura: {pokemon[i][3]}  |Peso: {pokemon[i][4]}")
    elif opcion ==2:
        print("\033[34mBuscar un Pokémon por nombre\033[0m")
        nombre = input("Ingrese nombre del Pokémon : ")
        centinela = False
        for pkm in pokemon:
            if pkm [1]==nombre:
                print(f"Pokémon encontrado | {pkm[1]} | Tipo: {pkm[2]} | Altura: {pkm[3]} | Peso: {pkm[4]}")
                centinela = True
                break
        if not centinela:
            print('\033[31mPokémon no encontrado\033[0m')
    elif opcion ==3:
        print("\033[34mAgregar un Pokémon al cinturón\033[0m")
        if len(cinturon)<6:
            nombre = input("Ingrese pokémon : ").capitalize()
            centinela = False
            for pkm in pokemon:
                if pkm [1]==nombre:
                    print(f"Pokémon encontrado | {pkm[1]} | Tipo: {pkm[2]} | Altura: {pkm[3]} | Peso: {pkm[4]}")
                    #Validando que el pokemon no se repita
                    repetido = False
                    for pk in cinturon:
                        if pk[1]==nombre:
                            repetido = True
                    if not repetido:
                        cinturon.append(pkm)
                        print("\033[32mPokémon registrado\033[0m")
                    centinela = True
                    break #romper la busqueda si ya se encontro
            if not centinela:
                print('\033[31mPokémon no encontrado\033[0m')            
        else:
            print("\033[31mCinturón lleno\033[0m")
    elif opcion ==4:
        print("\033[34mMostrar los Pokémon en el cinturón\033[0m")
        if len(cinturon)>0:
            for p in cinturon:
                print(f" N°{p[0]} Nombre: {p[1]} Tipo: {p[2]}")
        else:
            print("\033[31mCinturón vacio\033[0m")
    elif opcion ==5:
        print("\033[34mQuitar un Pokémon en el cinturón\033[0m")
        nombre = input("Ingrese pokémon para eliminar : ").capitalize()
        centinela = False
        for p in cinturon:
            if p[1] == nombre:
                cinturon.remove(p)
                print("\033[32mPokémon eliminado\033[0m")
                centinela = True
                break
        if not centinela:
            print("\033[31mPokémon no encontrado\033[0m")
    elif opcion ==6:
        if len(cinturon)>0:
            with open('REPORTE_CINTURÓN.csv', 'w', newline='', encoding='utf-8') as a:
                escritura = csv.writer(a, delimiter=',')
                escritura.writerows(cinturon)
                print("\033[32mReporte generado\033[0m")
    else:
        print("\033[31mSeleccion no valida\033[0m")