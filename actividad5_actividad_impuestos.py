sueldo = float(input('Me puedes dar la cantidad de tus ingresos: '))
if (sueldo < 1000):
  impuesto = sueldo * 0.05
  print('Tus impuestos son', impuesto,'  Tu sueldo despues de impuesto es : ', sueldo - impuesto)
elif (sueldo >= 1000 and sueldo <= 2000):
  impuesto = sueldo * 0.15
  print('Tus impuestos son', impuesto,'  Tu sueldo despues de impuesto es : ', sueldo - impuesto)
elif (sueldo >= 2000 and sueldo <= 3000):
  impuesto = sueldo * 0.2
  print('Tus impuestos son', impuesto,'  Tu sueldo despues de impuesto es : ', sueldo - impuesto)
else:
  impuesto = sueldo * 0.3
  print('Tus impuestos son', impuesto,'  Tu sueldo despues de impuesto es : ', sueldo - impuesto)
     