#Find the first 10 numbers from geometric series.

a = float(input("Enter the first number in the series.\n"))
r = float(input("Enter the common ratio.\n"))
i = 0
print("First 10 terms of geometric series : \n")
while i<10 :
	print(a)
	a = a * r
	i += 1
