import csv
import plotter
import turtle


def quit():
    '''It allows the user quit the process and exit (Takes input Y,y,N,n)'''
    a = input("Are you sure?(y/n)")
    if a == "y" or a == "Y":
        return True

    return False



def student_average(input):
    ''' the function plots a single student’s grades on the graph.'''
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
    '''the function in your plots module that calculates the class average for a single grade item.'''
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
        print("Usage: avg <filename> <number>")
    return -1


def class_average(input):
    ''' the function in your plots module that plots the class average for all grade items.'''
    try:
        plotter.init("Class Average", "Assignments", "Marks out of 100")
        for x in range(2, 12):
            total = 0
            count = 1
            with open(input[1], "r") as f1:
                cr = csv.reader(f1)
                next(cr)
                total_avg = 0
                for row in cr:
                    total += float(row[x])
                    count += 1
                avg = total/count
                plotter.add_data_point(round(avg, 2))
                total_avg += avg
        plotter.plot()
        print("Plot is finished (window may be hidden)")
        total_avg = total_avg / 10
        return total_avg
    except FileNotFoundError:
        print("No such file:", input[1])
    except IndexError:
        print("Usage: cavg <filename>")



def help():
    '''This function should print the help message shown below (gives menu)'''
    print ("stu <filename> <first name> <last name> - plot student grades\n")
    print ("cavg <filename> - plot class average\n")
    print ("avg <filename> <number> - prints the average for the grade item\n")
    print ("quit - quits\n")
    print ("help - displays this message\n")


def main():
    while True:
        try:
            enter = input(">> ")
            enter = enter.split()
            if enter[0] == "quit":
                if quit() == True:
                    print("Goodbye!")
                    break
            elif enter[0] == "stu":
                x=student_average(enter)
                if x==True:
                    print("Plot finished (window may be hidden)")
                elif x == False:
                    print("Plot failed (no such student)")
            elif enter[0] == "avg":
                y=print_average(enter)
                if y!=-1:
                    print("Average:", y)
            elif enter[0] == "cavg":
                class_average(enter)
            elif enter[0]=="help":
                help()



            else:
                raise IndexError
        except IndexError:
            print("Enter a command or 'quit' to quit")
            continue


main()
