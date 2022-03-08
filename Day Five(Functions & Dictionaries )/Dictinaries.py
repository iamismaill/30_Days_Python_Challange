##Day Five: Dictinaries,Nesting Dictinaries & List
from replit import clear
from art import logo

name = input("What's your name ? ")
price =int(input("what's the bird price ? "))


dict = {} 


empyt_list = []
def list_haye():
  for i in name :
    empyt_list.append(i)
  print(empyt_list)
    
   
    

##input_data(name = name, price=price)
another_user = input("Is there another user who wants bird Yes or No ?")

if another_user == "yes":
  clear()
  name = input("What's your name ? ")
  price =int(input("what's the bird price ? "))
  list_haye()
  ##print(dict)
else:
  print("Hello")





student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
 

student_grades ={}

for student in student_scores:
  print(student)
  score = student_scores[student]
  print(score)
  if score > 90 :
      student_grades[student] ="Outstanding"
  elif score > 81 :
      student_grades[student] ="Exceeds Expectations"
  elif score > 71 :
      student_grades[student] = "Acceptable"
  elif score <71:
      student_scores[student] ="Faile"
    

print(student_grades)


