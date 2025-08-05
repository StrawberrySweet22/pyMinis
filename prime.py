import numpy as np

x = 10001
nth_max = int(x*(np.log(x)+np.log(np.log(x))))
i = 2
num_list = list(1 for i in range(nth_max))
current_index = 0
primes = list(0 for i in range(int(x*np.log(x))))
while i < nth_max:
	if num_list[i] == 1:
		for j in range(i,nth_max):
			if j%i == 0:
				num_list[j] = 0
			j+=1
		primes[current_index] = i
		current_index += 1
	i+=1

print(primes[x-1])