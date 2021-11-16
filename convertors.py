mile = 1.609344 #km
km = 0.621371192 #miles

def f_to_c(x):
    sum1 = float(x) - float(32)
    sum = float(sum1) * float(0.5556)
    print(cislo, "Farenhaitu je: ", sum, "C")

def c_to_f(x):
    sum1 = float(x) * float(1.8)
    sum = float(sum1) + float(32)
    print(cislo, "Celsia je: ",sum, "F")

def mile_to_km(x):
    sum = float(x) * float(mile)
    print(cislo, "Milí je: ", sum, "km")

def km_to_mile(x):
    sum = float(x) * float(km)
    print(cislo, "Kilometru je: ", sum, "miles")
while True:
    userInput = input("Co chcete převadět, Dálku(distance) nebo stupně(degrees)")
    if userInput == "distance":
#-----------------------------------------------
        vyber = input("Chcete převest kilometry(km) nebo míle(mile): ")
        if vyber == "km":
            cislo = input("Zadej hodnotu kilometru: ")
        else:
            cislo = input("Zadej hodnotu milí: ")

        if vyber == "mile":
            mile_to_km(cislo)
        else:
            km_to_mile(cislo)
    else:
#-----------------------------------------------
        vyber = input("Chcete převest farnhaity(fah) nebo celsia(cel): ")
        if vyber == "fah":
            cislo = input("Zadej hodnotu farenhaitu: ")
        else:
            cislo = input("Zadej hodnotu celsia: ")

        if vyber == "fah":
            f_to_c(cislo)
        else:
            c_to_f(cislo)
#-----------------------------------------------
