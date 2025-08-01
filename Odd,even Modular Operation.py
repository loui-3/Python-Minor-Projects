first_number = int(input("Input a number: "))
second_number = int(input("Input a second number: "))
final_number = int(first_number % second_number)
if final_number == 0 :
    print("The number is Even")
else:
    print("The number is Odd")