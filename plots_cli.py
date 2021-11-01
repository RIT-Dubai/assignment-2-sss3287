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


def student_average(input):
    try:
        with open(input[1], "r") as f1:
            cr = csv.reader(f1)
            next(cr)
            count = 0
            plotter.init(input[2] + " " + input[3], "Assignment", "Marks out of 100")
            for row in cr:
                if row[0] == input[3]:
                    count += 1
                    if row[1] == input[2]:
                        count += 1
                        for data in range(2, len(row)):
                            plotter.add_data_point(float(row[data]))
            if count == 2:
                plotter.plot()
                return True
            else:
                return False
    except FileNotFoundError:
        print("No such file:", input[1])
    except IndexError:
        print("Usage: stu <filename> <first name> <last name>")


def print_average(input):
    try:
        if int(input[2])>=12:
            print("Grade item does not exist")
            return -1
        with open(input[1], "r") as f1:
            cr = csv.reader(f1)
            next(cr)
            total = 0
            count = 0
            avg = 0
            for row in cr:
                total += float(row[int(input[2]) + 1])
                count += 1
            avg = round(total/count, 2)
            return avg
    except ValueError:
        print("Grade item must be a number.")
    except FileNotFoundError:
        print("No such file:", input[1])
    except IndexError:
        print("Usage: stu <filename> <first name> <last name>")
    return





def help():
    print ("stu <filename> <first name> <last name> - plot student grades\n")
    print ("cavg <filename> - plot class average\n")
    print ("avg <filename> <number> - prints the average for the grade item\n")
    print ("quit - quits\n")
    print ("help - displays this message\n")


main()
