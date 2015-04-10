def calculate_e(precision):
	sum = 1
	y=0
	z=1
	x = 0
	while (x<precision):
		x=x+1
		y=1/(x*z)
		sum = sum+y
		z=x*z
	return sum
