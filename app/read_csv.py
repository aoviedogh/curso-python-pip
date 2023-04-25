import os

os.system("clear")
################################

print("*" * 7, "READ CSV", "*" * 7)

import csv

def read_csv(path):
  with open(path, "r") as file:
    reader = csv.reader(file, delimiter=",")
    header = next(reader)
    data = []

    #"""
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key : value for key, value in iterable}
      data.append(country_dict)

    return data

      #print("***" * 5, "Línea #:", counter, "***" * 5)
      #print(row)
    #"""

if __name__ == "__main__":
  data = read_csv("./app/data.csv")
  print(data)