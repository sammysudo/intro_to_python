num1 = int(input("Enter the first number/operand: \n"))
num2 = int(input("Enter the second number/operand: \n"))
operator1 = input("Enter the operator to be used: \n 1 for + \n 2 for - \n 3 for * \n 4 for / \n")
print(f"You have entered {num1} and {num2}")

result = num1 + num2
result2 = num1 - num2
result3 = num1 * num2
result4 = num1 / num2
if operator1 == "1":
    print(f"Your solution: {num1} + {num2} = {result}")
elif operator1 == "2":
    print(f"Your solution: {num1} - {num2} = {result2}")
elif operator1 == "3":
    print(f"Your solution: {num1} * {num2} = {result3}")
elif operator1 == "4":
    print(f"Your solution: {num1} / {num2} = {result3}")
else:
    print("Invalid operation please retry! \n")
    
    

