#!/usr/bin/env python

# Sum, percentage, and multiplication calculator for two numbers

class CalcClass(object):
	def __init__(self, x, y):
	    self.num1 = x
	    self.num2 = y
	def calc_sum(self):
	    return self.num1 + self.num2
	def calc_product(self):
	    return self.num1 * self.num2
	def calc_percent(self):
	    return (100 * self.num2) / self.num1




#	    print("{0} is {1} percent of {2}".format(self.num1, per_cent, self.num2)



