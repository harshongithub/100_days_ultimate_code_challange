#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
bill=float(input("what was the total bill?\n"))
tip=int(input("what percentage tip would you like to give? 10,12, or 15?"))
split=input("How many people to split the bill?")
tip=bill*(tip/100)
total_bill=bill+tip
split=total_bill/int(split)
final_amount="{:.2f}".format(split) #format funtion helps in formating =, here we formated to 2 decimal numbers formating change data type to string
print(f"Each person should pay: {final_amount}")