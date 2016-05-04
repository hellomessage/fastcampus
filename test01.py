#for i in range(5,-1,-1):
#	for j in range(5):
#		if(i <= j):
#			print("*")
#		else:
#			print(" ")


#for i in range(5,-1,-1):
#	for j in range(5):
#		if(i <= j):
#			sys.stdout.write("*")
#		else:
#			sys.stdout.write(" ")
#	print()

#count = 5
#def star_tow(count): 
#	for i in range(count,-1,-1):
#		for j in range(count):
#			if(i <= j):
#				sys.stdout.write("*")
#			else:
#				sys.stdout.write(" ")
#		print()
#
#star_tow(count)

#count = int(input("별 개수 입력 : "))
#
#def star_tow(count): 
#	for i in range(count,-1,-1):
#		for j in range(count):
#			if(i <= j):
#				sys.stdout.write("*")
#			else:
#				sys.stdout.write(" ")
#		print()
#
#star_tow(count)


count = int(input("ver1. 별 개수 입력 : "))

def star_one(count): 
	for i in range(count):
		print("*" * (i + 1))

star_one(count)

count = int(input("ver2. 별 개수 입력 : "))

def star_tow(count): 
	for i in range(count):
		sys.stdout.write(" " * (count - i))
		sys.stdout.write("*" * (i + 1))
		print()

star_tow(count)


count = int(input("ver3. 3별 개수 입력 : "))

def star_three(count): 
	for i in range(count):
		sys.stdout.write("*" * (count - i))
		sys.stdout.write(" " * (i + 1))
		print()

star_three(count)


count = int(input("ver.4 별 개수 입력 : "))

def star_four(count): 
	for i in range(count):
		sys.stdout.write(" " * (i + 1))
		sys.stdout.write("*" * (count - i))
		print()

star_four(count)
