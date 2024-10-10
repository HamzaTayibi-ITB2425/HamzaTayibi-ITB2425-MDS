from datetime import datetime

def main():
    # Demanar dia, mes i any de naixement
    dia = int(input("Introdueix el dia de naixement:"))
    mes = int(input("Introdueix el mes de naixement:"))
    any = int(input("Introdueix l'any de naixement:"))

    # Data actual
    avui = datetime(2024, 9, 27)

    # Data de naixement
    data_naixement = datetime(any, mes, dia)

    # Calcular l'edat
    edat = avui.year - data_naixement.year - ((avui.month, avui.day) < (data_naixement.month, data_naixement.day))

    # Verificar si és major o menor d'edat
    if edat >= 18:
        print("Ets major d'edat.")
    else:
        print("Ets menor d'edat.")

if __name__ == "__main__":
    main()
