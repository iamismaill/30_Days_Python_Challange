"""

Day One - Python 30 Days Challange -Ismail Abdulhakin Mohamud

"""

#1. Create a greeting for your program.
print("Welcome to the Band Name Generator")


#2. Ask the user for the city that they grew up in.
city_name =input("What's name of the city you grew up in ? \n")


#3. Ask the user for  the name of a pet.
pets_name = input("What's your pet's name ? \n")

#4. Combine the name of their city and pet and show them their band name.

print("Your band name could be " + city_name +" " + pets_name)


##Day one Excercise - Datatypes 

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
##print(type(two_digit_number))
####################################
#Write your code below this line 👇
a = int(two_digit_number[0])
b = int(two_digit_number[1])
c= a +b 
print(c)


##BMI Calculater 
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = int(weight) / float(height)

print(round(BMI))


### Life in weeks
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇

age_as_int = int(age)
years_remaining = 90- age_as_int
days_remaining = years_remaining *365
weeks_remaining = days_remaining * 52
months_remaining = weeks_remaining * 12 

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)



##Tip Calculator 

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator !")
total_bill =  input("What was the total bill ?")
percentage_bill = input("How much tip would you like to give? 10, 12, or 15?")
split_bill =      input("How many people to split the bill? ")

total_bill_int = int(total_bill)
percentage_bill_int = int(percentage_bill)
split_bill_int = int(split_bill)

total = total_bill_int *(percentage_bill_int /100)
share = round(total/split_bill_int ,2 )
print(f"the bill price is {share} ")



### Day one challange i have learneed Strings & Variables 