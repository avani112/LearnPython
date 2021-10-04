Number = int(input("Enter any Number "))
Sum = 0
for i in range(1, Number):
    if(Number % i == 0):
        Sum = Sum + i
if (Sum == Number):
    print("{} is a Perfect Number".format(Number))
else:
    print("{} is not a Perfect Number".format(Number))
