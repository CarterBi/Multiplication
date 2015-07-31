num = int(raw_input("What number do you want to go up to? \nPlease do not exceed 30."))

num2 = range(1,num + 1)

while True:

	if num > 30:
		print "Please write a smaller number."
	else:
		break

for i in num2:
	for j in num2:
		print "%03d" % (i * j),
	print ""

