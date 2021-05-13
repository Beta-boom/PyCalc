print('¡Hola! Esta es la PyCalc (la calculadora de Python) selecciona un número para empezar.')
print('1. SUMAR')
print('2. RESTAR')
print('3. MULTIPLICACIÓN')
print('4. DIVISIÓN')
selection = input('Elige una función: ')
if selection == '1':
	plusvalue1 = int(input('Elige tu valor 1: '))
	plusvalue2 = int(input('Elige tu valor 2: '))
	plusresult = plusvalue1 + plusvalue2
	print(f'La suma de tus cifras es: {plusresult}')
elif selection == '2':
  minusvalue1 = int(input('Elige tu valor 1: '))
  minusvalue2 = int(input('Elige tu valor 2: '))
  minusresult = minusvalue1 - minusvalue2
  print(f'La resta de tus cifras es: {minusresult}')
elif selection == '3':
  multvalue1 = int(input('Elige tu valor 1: '))
  multvalue2 = int(input('Elige tu valor 2: '))
  multresult = multvalue1 * multvalue2
  print(f'La multiplicación de tus cifras es: {multresult}')
elif selection == '4':
  divvalue1 = int(input('Elige tu valor 1: '))
  divvalue2 = int(input('Elige tu valor 2: '))
  divresult = divvalue1 / divvalue2
  print(f'La división de tus cifras es: {divresult}')
else:
	print('Debes seleccionar una opción válida. Abortando...')

print('¡Gracias por usar la PyCalc 1.0!')
print('Copyright (C) 2021 Josep Valencia - josepvalencia.ga')