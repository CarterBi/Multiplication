num = int(raw_input("What number do you want to go up to?"))

num2 = range(1,num + 1)

for i in num2:
	for j in num2:
		print "%03d" % (i * j),
	print ""

