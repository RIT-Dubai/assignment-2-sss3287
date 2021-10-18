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
    c = z.split()
    q = ('quit')
try:
    if c[0] == q:
        quit(raw_input("Are you sure?(y/n)"))
    else:
        raise ("Invalid Command")
except:
    print("Enter a command or 'quit' to quit.")
#quit(raw_input("Are you sure?(y/n)"))
 #or each_cmd in z:
