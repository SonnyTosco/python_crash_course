# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero foo")
print("Give me two numbers, and I'll divide them")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break;
    second_number = input("Second Number: ")
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

    # try:
    #     answer = int(first_number) / second_number
    # except ZeroDivisionError:
    #     print("Illegal opEratioonm")
    # else:
    #     print(answer)
