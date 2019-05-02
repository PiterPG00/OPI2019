p = str(input())
a = 0
b = ""
c = ""
d = 0
l = []

if(len(p) > 10):
	l.extend(p)
	d = len(l)
	a = len(l)
	a = a - 2
	b = l[0]
	c = l[d-1]
	print("{}{}{}".format(b,a,c))

else:
	print(p)