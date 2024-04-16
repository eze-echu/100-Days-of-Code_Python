#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the Tip Calculator!")
try:
    bill = float(input("What was the total bill? \n"))

    percentage = float(input("What percentage tip would you like to give? 10, 12, 15\n"))

    if percentage not in [10, 12, 15]:
        raise Exception("That's not a valid percentage choice")

    people = int(input("How many people to split the bill? \n"))

    tip_per_person = (bill * percentage / 100) / people

    print(f"Each person should pay: ${tip_per_person:.2f}")
except:
    pass