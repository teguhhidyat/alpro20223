batas = int(input('masukan angka batas: '))

for i in range(batas):
	print(i + 1, end='')
	fizz = (i + 1) % 2 == 0
	buzz = (i + 1) % 3 == 0
	
	if fizz and buzz:
		print(' ->FizzBuzz')
		
	elif fizz:
		print(' ->Fizz')
	elif buzz:
		print(' ->Buzz')
	else:
		print('')