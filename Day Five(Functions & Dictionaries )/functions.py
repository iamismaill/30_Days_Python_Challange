##Leap year function 
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year.")
        return True
      
      else:
        print("Not leap year.")
        return False
        
    else:
      print("Leap year.")
      return True
     
  else:
    print("Note Leap year")
    return False

    print("Not leap year.")


def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  

  if is_leap(year)  and month ==2 :
    return 29
    
    
    
  
  

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)




##Add function 
def add(n1,n2):
  return n1+n2

##substract 
def sub(n1,n2):
  return n1-n2

##Multiplication 

def mult(n1,n2):
  return n1 * n2

##Division 

def dev(n1,n2):
  return n1/n2

operations = {
  "+": add,
  "-": sub,
  "*": mult,
  "/": dev
  
  
}

num_input =  input("Enter number one ")
num2_input = input("Enter number two ")

for operator in operations :
  print(operator)

symbol = input(" Choose which operator  + , - , / or * ")

calculation_operation = operations[symbol]
answer = calculation_operation(num_input,num2_input)
print(f"a{answer}")
 









