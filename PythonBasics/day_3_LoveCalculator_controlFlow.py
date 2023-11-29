print("Please Enter two names")
name1 = input() 
name2 = input()
print("The Love Calculator is calculating your score...")

name=name1+name2
lower_case=name.lower()
t=lower_case.count("t")
r=lower_case.count("r")
u=lower_case.count("u")
e=lower_case.count("e")
True_=t+r+u+e
l=lower_case.count("l")
o=lower_case.count("o")
v=lower_case.count("v")
e=lower_case.count("e")
Love=l+o+v+e
score=str(True_)+str(Love)

score=int(score)
if score<10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")