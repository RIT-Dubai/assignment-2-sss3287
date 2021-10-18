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
    quit(raw_input("Are you sure?"))
