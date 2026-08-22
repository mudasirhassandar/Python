# WAP TO CHECK IF A NUMBER ENTERED BY THE USER IS ODD OR EVEN
number = int(input("Enter the number = "))
if number % 2 == 0:
    print("Entered Number is Even")
else:
    print("Entered Number is Odd")

# WAP TO FIND THE GREATEST OF 3 NUMBERS ENTERED BY THE USER
num1 = int(input("Enter first number = "))
num2 = int(input("Enter second number = "))
num3 = int(input("Enter third number = "))

if num1 > num2 and num1 > num3:
    print(num1, " is the greatest")
elif num2 > num3:
    print(num2, " is the greatest")
else:
    print(num3, " is the greatest")

# WAP TO CHECK IF A NUMBER IS MULTIPLE OF 7 OR NOT
x = int(input("Enter the number = "))
if x % 7 == 0:
    print(x, "is mutiple of 7")
else:
    print(x, "is not multiple of 7")
