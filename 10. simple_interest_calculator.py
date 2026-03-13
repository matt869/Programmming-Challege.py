# Program to calculate simple interest
p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest: "))
t = float(input("Enter Time (in years): "))

interest = (p * r * t) / 100
print(f"The simple interest is: {interest}")
