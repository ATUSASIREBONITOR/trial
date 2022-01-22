c = float(input("Enter initial amount of investment : "))
r = float(input("Enter the yearly rate : "))
n = int(input("Enter number of times interest is compounded : "))
t = float(input("Enter the number of years : "))
p = round(c*((1+(r/n))**(t*n)), 2)

print("Your final value of investment is " + str(p))
