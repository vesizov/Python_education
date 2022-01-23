array = [5,7,4,3,8,2]
n = len(array)
count = 0
for e in range(n-1):
	for i in range(n-1):
		if array[i]>array[i+1]:
			count += 1
			array[i], array[i+1] = array[i+1], array[i]
	print(array)

print(array, count)