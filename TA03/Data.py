import calendar

def DiesMes():
    try:
        # Demano el mes i l'any a l'usuari
        any = int(input("Introdueix l'any: "))
        mes = int(input("Introdueix el mes (1-12): "))

        # Valido si el mes és vàlid
        if 1 <= mes <= 12:
            # Obténgo el nombre de dies
            dies_mes = calendar.monthrange(any, mes)[1]
            print(f"El mes {mes} de l'any {any} té {dies_mes} dies.")
        else:
            print("Mes no vàlid. Introdueix un número entre 1 i 12.")

    except ValueError:
        print("Si us plau, introdueix números vàlids per l'any i el mes.")

# Crido la funció
DiesMes()
