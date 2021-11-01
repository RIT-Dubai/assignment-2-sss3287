import plots_cli
import csv
import plotter
import turtle


def test_student_average():
    x=plots_cli.student_average("stu GCIS.123.600-assignment2-sample.csv Zeyad Bonita".split())
    assert(x==True)

def test_print_average():
    x=plots_cli.print_average("avg GCIS.123.600-assignment2-sample.csv 5".split())
    assert(x!=-1)

def test_class_average():
    x=plots_cli.class_average("cavg GCIS.123.600-assignment2-sample.csv".split())
    assert(x!=None)
