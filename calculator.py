num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

print("calculation: +, -, *, /")
select = input("Select calculation: ")
if select == "+":
    print(num1, "+", num2, "=", num1+num2)

elif select == "-":
     print(num1, "-", num2, "=", num1 - num2)
elif select == "*":
    print(num1, "*", num2, "=", num1 * num2)
elif select == "/":
    print(num1, "/", num2, "=", num1 / num2)

else:
    print("Not Calculeted")
