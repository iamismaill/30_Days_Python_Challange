### 
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

  
###For in list counting list of items

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

##counting list items
list_itmes_no = 0
for itemsno in student_heights:
  list_itmes_no += 1


##sum up the total values of the list 
total  =0 
for total_no in student_heights:
   total += total_no
   ##print(total)

### Average
average = total/list_itmes_no
print(f"The average is : {average} ")

##Checking the highest number in list of elements
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
heigh_score = 0
for score in student_scores:
  if score > heigh_score:
    heigh_score = score 
print(f"The highest score is {heigh_score}")
    
    
##Calculating the total of even numbes between 0 to 100
#Write your code below this row 👇
total = 0

###even_numbers =0
for number in range(0,101,2):
 total += number
print(total)

total2 =0
for number in range (0,101):
  if number %2 == 0:
    total2 += number
print(total2)

##Check if the number is divisible by 5 , 3 or 5 and 3 using for loop
#Write your code below this row 👇

for number in range(0,101):
  if number % 3 and number %5 == 0:
    print("Fizz Buzz")
  elif number % 3 ==0:
    print("Fizz")
  elif number %5 == 0:
    print("Buzz")
  else :
    print(number)
   ## print(number)
