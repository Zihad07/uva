

mysum = 0
month = 1
while month<=12:
    money = float(input())
    mysum += money
    month += 1

average = mysum/12.0
print("$%0.2f" %(average))

