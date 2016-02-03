a = int(raw_input('Enter value of a: '))
b = int(raw_input('Enter value of b: '))
c = int(raw_input('Enter value of c: '))
if c > a*b:
	print "%s is larger than %s x %s" % (c,a,b)
	d = a*b
	print "%1f times %1f is: %1f" % (a,b,d)
else:
	print "%s is smaller than %s x %s" % (c,a,b)

