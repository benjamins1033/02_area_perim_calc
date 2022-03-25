def num_check(question):
    valid = False
    while not valid:

        error = "please enter a number that is more than 0"

        try: 

            response = float(input(question))

            if response > 0:
                return response
            
            else:
                print(error)
                print() 

        except ValueError: 
            print(error)

print()
print("**** area perimeter calculator *****")
print()

keep_going = ""
while keep_going == "":

    width = num_check ("width: ")
    height = num_check("height: ")

    area = width * height
    perimeter = 2 * (width + height)

    print("perimeter: {:.2f} units".format(perimeter))
    print("area: {:.2f} square units".format(area))
    print()
    keep_going = input("press <enter> to keep going or any key to quit")

print()
print("thanks for using the area / perimeter calculator")
