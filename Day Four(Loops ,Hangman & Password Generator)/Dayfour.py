###Day four Functions
def paint_calc(height,width,cover):
  area = height * width 
  n_cons = area /5 
  round_n = round(n_cons)
  print(round_n)
  
  

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)



##Prime_number_checker function 
#Write your code below this line 👇

def prime_checker (number):
  if number % 2 == 0:
    print("it's not prime number")
  else:
    print("it's prime number")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



