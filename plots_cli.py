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





def help():
    print ("stu <filename> <first name> <last name> - plot student grades\n")
    print ("cavg <filename> - plot class average\n")
    print ("avg <filename> <number> - prints the average for the grade item\n")
    print ("quit - quits\n")
    print ("help - displays this message\n")


if __name__ == '__main__':
    try:
        z = raw_input("Enter a Command!")
        c = z.split()
        q = ('quit')
        h = ('help')
        if c[0] == q:
            quit(raw_input("Are you sure?(y/n)"))
        elif c[0] == h:
            help()
        else:
            raise "Invalid Command"
    except:
        print("Enter a command or 'quit' to quit.")
        z = raw_input("Enter a Command!")
        c = z.split()
        q = ('quit')
        if c[0] == q:
            quit(raw_input("Are you sure?(y/n)"))
        else:
            raise "Invalid Command"

#quit(raw_input("Are you sure?(y/n)"))
 #or each_cmd in z:
