#!/usr/bin/env python

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

class NewClass(CalcClass):
	def __init__(self, x, y, z):
	    CalcClass.__init__(self, x, y)
	    self.num3 = z
	def calc_sum(self):
	    return self.num1 + self.num2 + self.num3

'''
Classes can them be called as follows
'''

a = CalcClass(5,10)
b = NewClass(6,56,43)

print("Parameters sent to CalcClass are %s & %s" % (a.num1, a.num2))
print("Parameters sent to NewClass are: {0},{1}, & {2}".format(b.num1, b.num2, b.num3))

 


