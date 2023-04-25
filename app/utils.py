import os
os.system("clear")
################################

print("*" * 7, "MODULES II: utils", "*" * 7)

def get_poblacion():
  keys = ["BRA", "COL", "PER", "MEX",]
  values = [100, 200, 300, 450]
  return keys, values

def get_poblacion_por_pais(data, pais):
  print(pais)
  result = list(filter(lambda x: x["Country/Territory"] == pais, data))
  return result

def get_reto(pais):
  poblaciones = {
    "2022" : int(pais["2022 Population"]),
    "2020" : int(pais["2020 Population"]),
    "2015" : int(pais["2015 Population"]),
    "2010" : int(pais["2010 Population"]),
    "2000" : int(pais["2000 Population"]),
    "1990" : int(pais["1990 Population"]),
    "1980" : int(pais["1980 Population"]),
    "1970" : int(pais["1970 Population"])
  }

  k = poblaciones.keys()
  v = poblaciones.values()

  return k, v