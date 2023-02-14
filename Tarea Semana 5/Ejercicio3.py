#se toma la fecha de nacimiento en formato YYYY
nacimiento = int(input("Ingrese su año de nacimiento: "))
#Si la fecha es divisible entre cuatro y no es divisible entre 100 entonces sera biciesto
if nacimiento%4 == 0 and nacimiento%100 != 0:
    print("Su año es biciesto")
#Si la fecha es divisible entre cuatro y es divisible entre 100 mientras al tiempo sea divisible entre 400 sera biciesto
elif nacimiento%4 == 0 and nacimiento%100 == 0 and nacimiento%400 == 0:
    print("Su año es biciesto")
else:
#Si no es niguna de las anteriores no sera biciesto
    print("Su año no es biciesto")



