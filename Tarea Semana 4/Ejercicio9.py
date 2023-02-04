#se toman los datos convertidos en forma flotante
ingresos = float(input("inserte sus ingresos mensuales: "))
gastosAlimentacion = float(input("inserte sus gastos mensuales por alimentacion: "))

#operaciones para obtener porcenta de alimentacion por regla de 3 y el restante del porcentaje
porcentajeAlimentcion = 100 * gastosAlimentacion / ingresos
porcentajeRestante = 100 - porcentajeAlimentcion
print("El proncentaje de gasto por alimentacion es de: ",round(porcentajeAlimentcion), '%')
print("El porcentaje restante es de: ", round(porcentajeRestante),"%")
