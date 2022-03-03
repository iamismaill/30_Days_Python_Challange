alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from Sawiir import logo
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")



##Encryption function 
def encrypt (plain_text, plain_shift):
  
  cipher_text =""
  for letter in plain_text:
    position = alphabet.index(letter)
    
    new_position = position + plain_shift
  
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print("Your encoded password is "+cipher_text)

  ##Decryption funcition 
def decrpyt (dec_text, dec_shit):
  decrpy_text =""  
  for letter in dec_text:
    position = alphabet.index(letter)
    
    new_position = position - dec_shit
  
    new_letter = alphabet[new_position]
    decrpy_text += new_letter
  print("Your decoded password is "+decrpy_text)
    
##Condition either the input is encode or decode 

if direction =="encode":
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  encrypt(plain_text =text, plain_shift = shift)
elif direction == "decoded":
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  decrpyt(dec_text =text, dec_shit=shift)
else :
  print("your input is wrong !!")
  
  


    
 

   