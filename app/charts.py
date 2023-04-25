import os

os.system("clear")
################################

print("*" * 7, "CHARTS", "*" * 7)

import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f"./imgs/{name}.png")
  #plt.show()
  plt.close()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.legend(title="Prueba")
  ax.axis("equal")
  plt.savefig("pie.png")
  #plt.show()
  plt.close()

def generate_poblacion(k, v):
  fig, ax = plt.subplots()
  ax.legend(title="Poblaciones")
  ax.bar(k, v)
  plt.savefig("poblacion.png")
  #plt.show()
  plt.close()

if __name__ == "__main__":
  labels = ["A", "B", "C"]
  values = [50, 100, 80]

  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)