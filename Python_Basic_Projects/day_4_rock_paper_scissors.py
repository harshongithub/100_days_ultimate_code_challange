import random

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
'''
paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_ins=[rock,paper,scissors]
user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(f"You choose - \n{game_ins[user]}")

computer=random.randint(0,1)
print(f"Computer choose - \n{game_ins[computer]}")
if user >= 3 or user< 0: 
  print("You typed an invalid number, you lose!")
elif (user==0 and computer==1) or (user==1 and computer==2) or (user==2 and computer==0):
  print("You lost!")
elif (user==0 and computer==2 ) or (user==1 and computer==0) or (user==2 and computer==1):
  print(f"You won!")
else:
  print(f"It's a tie!")
  