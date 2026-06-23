# Arithmetic operator

x = 10
y = 5
# addition
print('Sum: ', x + y)
# subtraction
print('Subtraction: ', x - y)
# multiplication
print('Multiplication: ', x * y)
# division
print('Division: ', x / y)
# floor division
print('Floor Division: ', x // y)
# modulo
print('Modulo: ', x % y)
# x to the power y
print('Power: ', x ** y)


# Comparison operator

a = 10
b = 7
# equal to operator
print('a == b ', a == b)
# not equal to operator
print('a != b ', a != b)
# greater than operator
print('a > b ', a > b)
# less than operator
print('a < b ', a < b)
# greater than or equal to operator
print('a >= b ', a >= b)
# less than or equal to operator
print('a <= b ', a <= b)


# Assignment operator

# assign 10 to n1
n1 = 10
# assign 20 to n2
n2 = 20
# assign the sum of n1 and n2 to n1
n1 += n2 # n1 = n1 + n2
print("Ans is ", n1)


# And operator

a = int(input('Enter first number : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number : '))
if a > b and a > c:
 print("a is the largest number")
if b > a and b > c:
 print("b is the largest number")
if c > a and c > b:
 print("c is the largest number")
 
 
 
# Or operator

x = 20
print(x > 10 or x < 30)


# Not operator

x = 7
print(not(x > 1 and x < 10))


# Membership operator

mylist = [10, 20.5, "Hello"]
n1 = 10
n2 = 100
print(n1 in mylist)
print(n2 in mylist)
print(n2 not in mylist)



# Identity operator

mylist1 = [10, 20]
mylist2 = [10, 20]
mylist3 = mylist1
print(mylist1 is mylist3)
print(mylist1 is mylist2)
print(mylist1 == mylist2)
print(mylist1 is not mylist2)