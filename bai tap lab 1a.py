#Q3 lab1a 1:
number1 = 20
number2 = 30
multiplication = number1 * number2
print("The result is:",multiplication)
#
number1 = 40
number2 = 30
addition = number2 + number1
print("The result is:",addition)
#Q3 lab1a 2:
for i in range(1, 11):
    current_number = i
if i > 1:
    previous_number = i - 1
else:
    previous_number = 0 
sum = current_number + previous_number
print(f"Current Number: {current_number}, Previous Number: {previous_number}, Sum: {sum}")
#lab1a 3:
print("Name", "Is", "James", sep="**")
#Q4 1:
num = 8
octal_number = oct(num)
print(f"the octal number of the decimal number {num} is {octal_number}")
#Q$ 2:
num = 458.541315
formatted_float = f"{num:.2f}"
print(f"{formatted_float}")
