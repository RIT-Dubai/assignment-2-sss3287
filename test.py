import csv
import plotter
import turtle
import plots_cli

def test_student_average():
    '''This function tests if the function plots a single student’s grades on the graph'''
    a=plots_cli.student_average("stu GCIS.123.600-assignment2-sample.csv Zeyad Bonita".split())
    assert(a==True)


def test_print_average():
    '''This function tests the function in your plots module that calculates the class average for a single grade item.'''
    a=plots_cli.print_average("avg GCIS.123.600-assignment2-sample.csv 5".split())
    assert(a!=-1)


def test_class_average():
    '''This function tests the function in your plots module that plots the class average for all grade items'''
    a=plots_cli.class_average("cavg GCIS.123.600-assignment2-sample.csv".split())
    assert(a!=None)


'''NOTE : In order for all these tests to pass you may have comment out only the main function
           that is def main() and call main in the plots_cli module
           to do that just put # in front of them #def main(): and #main()'''
