first_number = int(input("Input a number: "))
if first_number <= 0:
    print("The number is zero, cannot perform modulus operation.")
    exit()
second_number = int(input("Input a second number: "))
if second_number <= 0:
    print("The number is zero, cannot perform modulus operation.")
    exit()
final_number = float(first_number % second_number)
if final_number == 0 :
    print("The number is Even")
else:
    print("The number is Odd")
