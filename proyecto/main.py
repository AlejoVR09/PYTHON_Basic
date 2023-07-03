import random
choices=('Piedra', 'Papel', 'Tijera')


rounds=1
while True:
  user_choice=input("Elija la opcion: ")
  computer_choice=random.choice(choices)
  print(computer_choice)
  print("*"*10)
  print("ROUND", rounds)
  print("*"*10)
  if user_choice.isdigit():
    if int(user_choice)-1 > len(choices)-1 or int(user_choice) <= 0:
      print("Escoja un valor adecuado")
      continue
    else:
      user_choice=int(user_choice)
      if choices[user_choice-1]=='Piedra':
        if computer_choice=="Papel":
          print("Gana el pc")
        elif computer_choice=="Tijera":
          print("Gana el usuario")
        else:
          print("Empate")
      elif choices[user_choice-1]=='Papel':
        if computer_choice=="Tijera":
          print("Gana el pc")
        elif computer_choice=="Piedra":
          print("Gana el usuario")
        else:
          print("Empate")
      else:
        if computer_choice=="Piedra":
          print("Gana el pc")
        elif computer_choice=="Papel":
          print("Gana el usuario")
        else:
          print("Empate")
  else:
    print("No es un numero")
  break