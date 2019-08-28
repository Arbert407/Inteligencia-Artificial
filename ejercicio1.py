import math
import re
# Nota: recuerde que no está permitido modificar los nombres de las funciones
# ni los parámetros que reciben.





def distintos(lista):
  """Retorna True sólo si <lista> contiene sólo números diferentes"""
  conjunto = set(lista) #Los conjuntos tienen la propiedad de no repetir sus elementos
  if (len(conjunto) == len(lista)): #Si el numero de elementos del conjunto es igual al numero de elementos de lista entonces no hay elementos repetidos
    print("Esta lista no posee elementos repetidos")
    return True
  else:
    print("Esta lista posee elementos repetidos")
    return False

def producto_punto(vector1, vector2):
  """Retorna el producto punto de <vector1> por <vector2>. 

  <vector1> y <vector2> se representan como tuplas del mismo tamaño n. Recuerde
  que el resultado del producto punto entre dos vectores es un valor
  escalar."""
  producto = 0
  for i in range(len(vector1)):
    producto += vector1[i] * vector2[i] # a punto b = a1*b1 + a2*b2 + ... + an*bn
  return producto

def cuenta_vocales(cadena):
  """Retorna el número de vocales que contiene la cadena."""
  resultado = 0
  for x in cadena:
      if x in ('a','e','i','o','u','A','E','I','O','U'): # Tanto mayusculas como minusculas
          resultado += 1
  return resultado

def cuenta_palabras(cadena):
  """Retorna un diccionario con todas la palabras que estén en <cadena> y la
  cantidad de veces que aparece cada una.

  Por ejemplo si <cadena> contiene un total de 7 palabras por ejemplo:

  "hola mundo, Hola hola. Hola mundo. mundo"
   
  de las cuales 2 son la palabra 'hola', 2 son 'Hola' y 3 son la palabra
  'mundo', retornará un diccionario, (no una cadena), cuya representación
  sería:

  {'hola': 2, 'Hola': 2, 'mundo': 3}

  Observe que se distingue entre mayúsculas y minúsculas, los puntos y comas,
  no se cuentan como palabras."""
  palabras = re.findall(r'\w+', cadena)
  print(palabras)
  conjunto = set(palabras)
  diccionario = {}
  for x in conjunto:
      diccionario[x] = 0
  for x in palabras:
      if x in conjunto:
          diccionario[x] += 1
  return diccionario

def vuelto(cantidad_pagar, cantidad_entregada):
  """Retorna un diccionario con la cantidad de billetes y monedas que deben ser
  entregas como vuelto a un cliente.

  El proceso se hacer de acuerdo a la cantidad a pagar y a la cantidad que el
  cliente entregó. Para crear el diccionario utilice el sistema monetario
  hondureño e intente que la cantidad de monedas y billetes sea lo menos
  posible entregando primero las denominaciones más grandes, las claves de los
  billetes en el diccionario iniciarán con la letra 'b' y las de las monedas
  con la letra 'm', seguidas de un guión '-' y el valor en números.

  Por ejemplo, si se invoca de esta manera vuelto(86.5, 100), el diccionario
  sería:

  {'b-10': 1, 'b-2': 1, 'b-1': 1, 'm-50': 1}
  """
  dicc = dict.fromkeys(['b-10','b-2','b-1','m-50'],0)
  vuelto = cantidad_entregada - cantidad_pagar
  while (vuelto > 0):
    #print(vuelto)
    if (vuelto >= 10):
      dicc['b-10'] += 1
      vuelto -= 10
    elif (vuelto >= 2):
      dicc['b-2'] += 1
      vuelto -= 2
    elif (vuelto >= 1):
      dicc['b-1'] += 1
      vuelto -= 1
    elif (vuelto >= 0.5):
      dicc['m-50'] += 1
      vuelto -= 0.5
    else:
      break  
  return dicc
