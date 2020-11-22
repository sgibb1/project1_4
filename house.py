# all inputs are taken in try block to handle invalid inputs
try:
    bathrooms = int(input("Enter number of bathrooms: "))
    bedrooms = int(input("Enter number of bedrooms: "))
    chairs = int(input("Enter number of chairs: "))
    sofas = int(input("Enter number of sofas: "))
    table = int(input("Enter number of tables: "))
    distance = int(input("Enter distance from college: "))
# handling invalid inputs
except:  # catching all types of errors , ValueError can also be used specifically
    # if user inputs invalid print Nope
    print("NOPE!")
# if all inputs are valid then check if house is good or bad
else:
    # if house have 3 bathrooms, 4 bedrooms and less than 10 miles from college
    if bathrooms >= 3 and bedrooms >= 4 and distance <= 10:
        # and if 2 ~ 4 chairs and have a table OR have a sofa then print 'good'
        if (2 <= chairs <= 4 and table > 0) or (sofas > 0):
            # NOTE: This message can be changed
            print("Good!")
        # else print 'bad'
        else:
            print("Bad!")
    # else print 'bad'
    else:
        print("Bad!")
