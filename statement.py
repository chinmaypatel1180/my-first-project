# if Statement

# program 1
n1 = 10
if n1 == 10:
 print("n1 is 10")
 
  # program 2
 
 n1 = 10
if n1 % 2 == 0:
 print("Number is even")
if n1 % 2 == 1:
 print("Number is odd")
 
 
 
 # if...else Statement
 
 n1 = 11
if n1 % 2 == 0:
 print("Number is even")
else:
 print("Number is odd")



# if...elif...else Statement

n1 = 11
if n1 == 10:
 print("n1 is 10")
elif n1 > 10:
 print("n1 is greater than 10")
else:
 print("n1 is less than 10")



# match-case Statement

ch = int(input("Enter choice:"))
match ch:
 case 1:
  print("This is one")
 case 2:
  print("This is two")
 case 3:
  print("This is three")
 case _:
  print("Invalid value")
 
 
 
 # Nested if-else Statement
 
n1 = 10
if n1 >= 0:
 if n1 == 0:
  print("n1 is 0")
 else:
  print("n1 is positive")
else:
 print("n1 is negative")