number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second integer:"))

a = 12
b = 48
sumofodd = 0

print("The Common Divisors are:")

for i in range(1, min(number1, number2) + 1): 
    if number1 % i == b % i == 0:
        if (i % 2) == 0:
            print("{0} is Even".format(i))
        else:
            print("{0} is Odd".format(i))
            sumofodd = sumofodd + i
##This adds the odd numbers after testing if the numbers are odd or even##

print("The Sum of Odd Common Divisors is:", sumofodd)
