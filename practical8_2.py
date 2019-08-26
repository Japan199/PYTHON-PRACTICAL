input_string = input("Enter family members separated by comma ")
a  = input_string.split(",")
number = input('Check if a number is on the list: ')
if number in a:
    print(True)
else:
    print(False)
