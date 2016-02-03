#!/usr/bin/env python

import math

bt = float(raw_input("Enter bill total: "))
tax = float(raw_input("Enter the amount of tax: "))
pt = float(raw_input("Enter tip amount desired in percent: "))

def calc_tip():
    tip = float((bt-tax)*(pt/100.0))
    total = math.ceil(float(bt+tip))
    return total

print "Total rounded up including tip is: %.2f" % (calc_tip())



        

