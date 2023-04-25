import os
os.system("clear")
################################

print("*" * 7, "MODULES II - main: ", "*" * 7)

import utils

def metodo():
  keys, values = utils.get_poblacion()
  print(keys)
  print(values)
  
  data = [
    {
      "Pais" : "BRA",
      "poblacion" : 100
    },
    {
      "Pais" : "PER",
      "poblacion" : 200
    },
    {
      "Pais" : "COL",
      "poblacion" : 150
    }
  ]
  
  pais = input("País:")
  result = utils.get_poblacion_por_pais(data, pais)
  print(result)

if __name__ == "__main__":
  metodo()
