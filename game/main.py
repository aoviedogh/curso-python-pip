import os
import random

os.system("clear")
################################

print("*" * 9, "JUEGO", "*" * 9)


#ELEGIR OPCIONES
def elegir_opcion():
  opciones = ("piedra", "papel", "tijera")
  eleccion = input("¿Piedra, Papel o Tijera?: ").lower()
  robot = random.choice(opciones).lower()

  if not eleccion in opciones:
    print("'" + eleccion + "' no es una opción permitida!")
    return None, None
  else:
    print("Opción usuario: ", eleccion)
    print("Opción robot: ", robot)

  return eleccion, robot


#REGLAS DE JUEGO
def reglas(eleccion, robot, usuario_wins, robot_wins):
  if (eleccion == robot):
    print("Empate")
  elif (eleccion == "piedra"):
    if (robot == "tijera"):
      print("Ganaste")
      usuario_wins += 1
    elif (robot == "papel"):
      print("Perdiste")
      robot_wins += 1
  elif (eleccion == "papel"):
    if (robot == "tijera"):
      print("Perdiste")
      robot_wins += 1
    elif (robot == "piedra"):
      print("Ganaste")
      usuario_wins += 1
  elif (eleccion == "tijera"):
    if (robot == "piedra"):
      print("Perdiste")
      robot_wins += 1
    elif (robot == "papel"):
      print("Ganaste")
      usuario_wins += 1

  return usuario_wins, robot_wins


#VERIFICA GANADOR
def verificar_ganador(usuario_wins, robot_wins):
  if (usuario_wins == 3):
    print("ACABÓ EL JUEGO -", "GANÓ USUARIO")
  elif (robot_wins == 3):
    print("ACABÓ EL JUEGO -", "GANÓ ROBOT")


#EJECUCION FINAL
def run():
  ronda = 0
  usuario_wins = 0
  robot_wins = 0

  while (usuario_wins < 3 and robot_wins < 3):
    ronda += 1
    print("*" * 29)
    print("******     RONDA", ronda, "    ******")
    print("*" * 29)

    eleccion, robot = elegir_opcion()
    usuario_wins, robot_wins = reglas(eleccion, robot, usuario_wins,
                                      robot_wins)
    verificar_ganador(usuario_wins, robot_wins)

    print("Usuario Score:", usuario_wins)
    print("Robot Score:", robot_wins)


run()
