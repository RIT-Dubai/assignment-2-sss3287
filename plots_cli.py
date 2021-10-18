def quit(x):

    a = ('Y')
    b = ('y')
    if x == a:
        print("Goodbye!")
        return True
    elif x == b:
        print("Goodbye!")
        return True
    else:
        return False


if __name__ == '__main__':
    z = raw_input("Enter a Command!")
    q = ('quit')
    if z == q:
              quit(raw_input("Are you sure?(y/n)"))
    else:
        print ("Please enter a valid command!")
#quit(raw_input("Are you sure?(y/n)"))
 #or each_cmd in z:
