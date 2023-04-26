import os

os.system("clear")
################################

print("*" * 7, "RETO", "*" * 7)

import csv
import utils
import charts
import pandas as pd

def read_csv(path):
  """ #Lo comentamos para implementar Pandas
  with open(path, "r") as file:
    reader = csv.reader(file, delimiter=",")
    header = next(reader)
    #print("header:", header)
    #print("reader:", reader)

    #NUEVO
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key : value for key, value in iterable}
      data.append(country_dict)
    #NUEVO

    paises = list(map(lambda x: x["Country/Territory"], data))
    #print("paises:", paises)
    porcentajes = list(map(lambda x: x["World Population Percentage"], data))
    #print("porcentajes:", porcentajes)
    """ #Lo comentamos para implementar Pandas

  df = pd.read_csv(path)
  df = df[df["Continent"] == "Africa"]
  paises = df["Country/Territory"].values
  porcentajes = df["World Population Percentage"].values

  charts.generate_pie_chart(paises, porcentajes)

  """
  pais = input("País:")
  result = utils.get_poblacion_por_pais(data, pais)
  print("result:", result)

  if len(result) > 0:
    pais = result[0]
    labels, values = utils.get_reto(pais)
    charts.generate_bar_chart(pais["Country/Territory"], labels, values)
  """
  """
  pais_search = input("País:")
  
  for row in reader:
    print("PAIS A EVALUAR:", row[1])
    print("ROW:", row)
    
    if pais_search == row[1]:
      print("***" * 5, "PAIS ENCONTRADO", "***" * 5)
      iterable = zip(header, row)
      pais = dict(iterable)
      print(pais)
      k, v = utils.get_reto(pais)
      print("***" * 5, "PAIS ENCONTRADO", "***" * 5)
      
      charts.generate_poblacion(k, v)
      break
  """

if __name__ == "__main__":
  read_csv("data.csv")