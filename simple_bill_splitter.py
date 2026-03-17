#Program to split a bill among friends
total = float(input("Enter the total bill amout:"))
people = int(input("Enter the number of people sharing the bill:"))

split = total / people
print(f"Each person should pay: ${split:.2f}")