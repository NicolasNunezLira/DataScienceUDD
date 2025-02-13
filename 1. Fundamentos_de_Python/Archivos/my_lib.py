# Esta es mi librería de pruebal

def saludo():
    print("Hola mundo desde el módulo my_lib ")
    
def isBisiesto(year):
    """
    Verifica si el año ingresado es bisiesto o no

    Parámetros:
    year (int): año a evaluar

    Salida:
    (boolean): dependiendo si es o no bisiesto

    """
    
    if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
        return True
    else:
        return False

def eliminar_puntuacion(texto :str) -> list[str]:
  """
  Función que elimina la puntuación de un texto, considerado que la puntuación
  como los simbolos:
        ¡!\""#$%&\'()*+,-./:;<=>¿?@[\\]^_`{|}~

  Argumentos:
  texto (str): Cadena de caracteres de la cual se desea eliminar la puntuación

  Retorna:
  list[str]: Lista con todas las palabras del texto, en el orden original, pero
              sin puntuación.   
  """
  puntuacion = '¡!\""#$%&\'()*+,-./:;<=>¿?@[\\]^_`{|}~'

  texto = texto.split(' ')
  lista = []

  for word in texto:
    for palabra in word.split('\n'):
      aux = ''.join([letter for letter in palabra if letter not in puntuacion])
      if aux != '':
        lista.append(aux)

  return lista

def elementos_unicos(lista: list[int]) -> list[int]:
  """
  Función que dada una lista de números enteros retorna una lista con elementos
  únicos de la original ordenada de manera decreciente.

  Argumentos:
  lista (list[int]): Lista de enteros a ordenar de manera decreciente y única

  Retorno:
  list[int]: Lista de elemnetos únicos retornados de manera decreciente.
  """
  lista = set(lista)
  res = []

  while len(lista) > 0:
    res.append(max(lista))
    lista.remove(max(lista))

  return res