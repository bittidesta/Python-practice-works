largest = None
smallest = None

while True:
    try:
        num = raw_input("Enter a number: ")
        n = int(num)
        if largest is None:
            largest = n
            smallest = n
        elif n > largest:
            largest = n
        elif n < smallest:
            smallest = n
    except:
        if num == "done":
            break
        else:
            print "Invalid input"
print "Minimum", smallest
print "Maximum", largest
