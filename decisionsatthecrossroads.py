#Decisions at the Crossroad
#Task 1 Code Correction for script that uses conditional statements to tell if a number is positive, negative, or zero.
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")