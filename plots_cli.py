import plotter
import csv

def quit(x):

    import csv
import plotter
import turtle


def quit():
    ans = input("Are you sure?(y/n)")
    if ans == "y" or ans == "Y":
        return True

    return False


def main():
    while True:
        try:
            choice = input(">> ")
            choice = choice.split()
            if choice[0] == "quit":
                if quit() == True:
                    print("Goodbye!")
                    break
            elif choice[0] == "stu":
                x=student_average(choice)
                if x==True:
                    print("Plot finished (window may be hidden)")
                elif x == False:
                    print("Plot failed (no such student)")
            elif choice[0] == "avg":
                y=print_average(choice)
                if y!=-1:
                    print("Average:", y)
            elif choice[0] == "cavg":
                class_average(choice)
            elif choice[0]=="help":
                help()
            else:
                raise RuntimeError
        except RuntimeError:
            print("Enter a command or 'quit' to quit")


d


def help():
    print ("stu <filename> <first name> <last name> - plot student grades\n")
    print ("cavg <filename> - plot class average\n")
    print ("avg <filename> <number> - prints the average for the grade item\n")
    print ("quit - quits\n")
    print ("help - displays this message\n")


main()
