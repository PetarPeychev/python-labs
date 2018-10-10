import math
bill_total = float(input("Enter your restaurant bill total: "))
print("20% tip: ", math.ceil(bill_total * 20 / 100), "15% tip: ", math.ceil(bill_total * 15 / 100))
