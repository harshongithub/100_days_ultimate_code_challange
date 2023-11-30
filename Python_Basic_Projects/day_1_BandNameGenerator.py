#This is the very first basic python project of mine
#Working  --> This project will take 2 input from the user with the help of input fuction "input()" and in last we 
#             will merge both the inputs and print it.

print("Welcome to the Band Name Genrator.")
city=input("What's the name of the city you grew up in?\n")
pet=input("" "What's your pet's name?" " 'Type null if you do not have any pet' \n" "")
if pet=="No pet"or"null":
    print("your band name could be The",city,"band")
else:
    print("your band name could be",city,pet)