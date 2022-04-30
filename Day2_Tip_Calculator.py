#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#beginning
print("Welcome to the tip calculator!")

#total bill as float 
total_bill = float(input("What was the total bill? $"))

#Tip percentage as float 
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
tip_perc = tip/100 + 1

#Split
split = int(input("How many people to split the bill? "))

#format for 2 decimal places
total = round(total_bill / split * tip_perc,2)
total = "{:.2f}".format(total_bill / split * tip_perc)

#convert total 
print(f"Each person should pay: ${total}")
