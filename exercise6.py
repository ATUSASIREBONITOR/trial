x1 = float(input("Enter point x1 : "))
y1 = float(input("Enter point y1 : "))
x2 = float(input("Enter point x2 : "))
y2 = float(input("Enter point y2 : "))

d = (((x2-x1)**2) + ((y2-y1)**2))**(1/2)
print("The distance between the points is " + str(d))
