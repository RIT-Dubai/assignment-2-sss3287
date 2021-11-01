import csv
import plotter
import turtle
import plots_cli

def test_student_average():
    a=plots_cli.student_average("stu /Users/sohan_saimbhi/Desktop/GCIS.123.600-assignment2-sample.csv Zeyad Bonita".split())
    assert(a==True)


def test_print_average():
    a=plots_cli.print_average("avg /Users/sohan_saimbhi/Desktop/GCIS.123.600-assignment2-sample.csv 5".split())
    assert(a!=-1)


def test_class_average():
    a=plots_cli.class_average("cavg /Users/sohan_saimbhi/Desktop/GCIS.123.600-assignment2-sample.csv".split())
    assert(a!=None)
