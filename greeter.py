def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

count = 0
#This is an infinite loop
while count < 5:
    print("\nPlease tell your name:")
    f_name = input("First Name:")
    l_name = input("Last Name:")
    if l_name == 'q':
        break
    count += 1
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
