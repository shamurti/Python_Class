
#!/usr/bin/env python

print "This is before the function"

a = 100

def my_func():
	b = a + 1
	print "hello there! This is from inside the function"
	print (r"This is 'b = a + 1' from inside the function:  {}").format(b)
	
print "This is text after the function"
print "This is 'a' from outside the function:  {}".format(a)


