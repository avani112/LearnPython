for num in range(1,101):
	print("fizzbuzz") if num % 3 == 0 and num % 5 == 0 else print("fizz") if num % 3 == 0 else print("buzz") if num % 5 == 0 else print(num)
