
n = int(raw_input("Enter a number divisible by three, and I will give you its cube:  "))

def cube(n):
	return n**3

def by_three(n):
	i = 0
	while (n%3 !=0):
		too_many_tries = (i>2)
		if too_many_tries:
			return "Too Many Tries. You only get three."
		else:
			print "%d is not divisble by three" % n
			n = int(raw_input("Try again:  "))
		i += 1
	return "Cube of %d is %d" % (n,cube(n))

print by_three(n)
print 'This is Radio Clash'

