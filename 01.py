meal=float(input("price of meal:"))
tax=float(input("perscent of tax: "))
tip=float(input("percent of tip: "))
tax= tax/100
tip=tip/100
meal=meal+tax*meal
meal=meal+tip*meal
print("your bill is:" + str(meal))
