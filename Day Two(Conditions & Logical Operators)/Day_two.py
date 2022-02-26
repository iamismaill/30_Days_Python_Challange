###Day two - Conditional Statements 

##Rollercoaster Game

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >120 :
  print(" you can ride the rollercoaster")
else:
  print("you can't ride the rollercoaster")

##Odd or Even number - Challange using Conditional Statements 

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number %2 ==0:
  print("Your input number is Even number")
else :
  print("Your input is Odd number")


### Nested conditon - roller coaster game 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age  = int(input("What's your age ?"))

if height >120 :
  print(" you can ride the rollercoaster")
  if age > 18:
    print("you have to pay $12")
  else:
    print("you have to pay $17")
else:
  print("you can't ride the rollercoaster")


  ###BMI Calculater - Nested Conditions
  # 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = weight / (height * height)
print("BMI is" + str(BMI))
if BMI > 35 :
  print(f"Your BMI is {BMI} , you are clinically obese weight")
elif BMI > 30 and BMI <35 :
  print(f"Your BMI is {BMI}, you are obese weight")
elif BMI >25 and BMI <30:
  print(f"Your BMI is {BMI},you are slightly overweight")
elif BMI > 18.5 and BMI <25 :
  print(f"Your BMI is {BMI}, you have normal weight")
else:
  print(f"Your BMI is{BMI},you are underweight")



 #This Code checks if a year is leap or normal and prints the result, then it prints the explanation why it is leap or normal
year = int(input("Which year you want to check ?"))

if year % 4 == 0 :
  if year % 100 == 0 :
    if year & 400 ==0:
      print("leap year")
    else:
      print("Not leap year")
  else:
    print("leap year")
    
else:
  print("it's not leap year")


###Pizza order - Nested Condition Statement

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
##small
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
##small
piza_bill = 0 

if size == "L":
  piza_bill =+25
elif size =="M":
  piza_bill  =+20
else:
  piza_bill =+15



if add_pepperoni =="Y":
  if size =="S":
    piza_bill +=2
  else:
    piza_bill +=3

if extra_cheese =="Y":
   piza_bill +=1 

print(f"Your final pizza price is {piza_bill}")
 

##Working out love score between two people using conditions , lower and count functions 

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

combined_names = name1 +name2

lower_strings = combined_names.lower()
print(lower_strings)

##True letters 
t = lower_strings.count("t")
r = lower_strings.count("r")
u = lower_strings.count("u")
e = lower_strings.count("e")

##Love letters 
l = lower_strings.count("l")
o = lower_strings.count("o")
v = lower_strings.count("v")
e = lower_strings.count("e")
love_word = l+o+v+e
true_word = t+r+u+e
total_letters = int( str(true_word) + str(love_word))
print(total_letters)
print(love_word)
print(true_word)
if total_letters <10 or total_letters > 90 :
  print(f"Your score is {total_letters}, you go together like coke and mentos.")
elif total_letters >40 and total_letters <50:
  print(f"Your score is {total_letters}, you are alright together")
else:
  print(f"Your score is {total_letters}")


###Treasure Game

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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

left_right = input("You\'re at a crossroad. Where do you want to go? Type left or right ? " )

if left_right == "left":
  swim_wait = input("You\'ve come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat. Type swim to swim across ")
  if swim_wait == "Wait":
    door = input(" You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose ")
    if door == "Yellow":
      
      print("You found the treasure! You Win!")
    elif door == "Blue":
      print("You enter a room of beasts. Game Over")
    elif door == "Red":
      print("It's a room full of fire. Game Over.")     
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else: 
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")