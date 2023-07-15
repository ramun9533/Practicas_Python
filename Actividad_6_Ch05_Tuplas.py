#altura = 2.5
#base = 3.2
#color = 'verde'
altura = float(input('Proporcioname la altura del rectangulo: '))
base = float(input('Proporcioname la Base del rectangulo: '))
color = str(input('Proporcioname el color del rectangulo: '))
def calcula_rectangulo(alturA, basE, coloR):
  """Calculates the area and perimeter of a square"""

  area = base * altura
  perimetro = 2 * base + 2 * altura

  return (area, perimetro, color)
results = calcula_rectangulo(altura, base, color)
print(results)
result_area =  results[0]
result_perimetro = results[1]
result_color = results[2]
print('El area del rectangulo es: ', result_area)
print('El perimetro del rectangulo es: ',result_perimetro)
print('El color del rectangulo es: ',result_color)
