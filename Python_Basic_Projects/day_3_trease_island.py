print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

step_1=input('''you're at a cross road. Where do you want to go? Type "left" or "right"\n''')
if step_1=="left":
  step_2=input('''You've coem to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim"'to swim across.\n''')
  if step_2 == "wait":
    step_3=input('''You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n''')
    if step_3=="blue":
      print("You found the treasure! You Win!")
    elif step_3=="red":
      print("It's a room full of fire. Game Over.")
    else:
      print("You fell in the hole and died. Game Over.")

  else:
    print("You got eaten by a shark. Game Over.")

else:
  print("you fell into the hole. Game Over.")