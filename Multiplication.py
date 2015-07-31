
num = int(raw_input("What number do you want to go up to? \nPlease do not exceed 30."))

while True:
	num = int(raw_input("What number do you want to go up to? \nPlease do not exceed 30."))
	if num > 30:
		print "Please write a smaller number."
	else:
		break

num2 = range(1,num + 1)

for i in num2:
	for j in num2:
		print "%03d" % (i * j),
	print ""

