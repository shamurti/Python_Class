a = range(10)

for i,elm in enumerate(a):
    if a[i]%2 != 0:
        b = elm**2
        print b
        continue
    elif a[i]%2 == 0:
        c = elm**3
        print c

