amount = float(input("Enter your amount : "))
print("Your change is ")

if amount >= 20:
    print(int(amount/20), "twenties")
    amount = amount % 20
else:
    print("0 twenties")

if amount >= 10:
    print(int(amount/10), "ten")
    amount = amount % 10
else:
    print("0 ten")

if amount >= 5:
    print(int(amount/5), "five")
    amount = amount % 5
else:
    print("0 five")

if amount >= 1:
    print(int(amount/1), "ones")
    amount = amount % 1
else:
    print("0 ones")

if amount >= 0.25:
    print(int(amount/0.25), "quarters")
    amount = amount % 0.25
else:
    print("0 quarters")

if amount >= 0.1:
    print(int(amount/0.1), "dimes")
    amount = amount % 0.1
else:
    print("0 dimes")

if amount >= 0.05:
    print(int(amount/0.05), "nickels")
    amount = amount % 0.05
else:
    print("0 nickels")

if amount >= 0.01:
    print(int(amount/0.01), "pennies")
    amount = amount % 0.01
else:
    print("0 pennies")
