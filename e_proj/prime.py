import numpy as np
import timeit
import matplotlib.pyplot as plt

def sieve(n=False, n_max = False):
	num_list = []
	tester = int(6*(np.log(6)+np.log(np.log(6))))
	if(not(n_max)):
		n_max = int(n*(np.log(n)+np.log(np.log(n))))
		sqr_n = int(np.sqrt(n))
	else:
		sqr_n = int(np.sqrt(n_max))
	if(n < 6 and n_max < tester):
		return[2, 3, 5, 7, 11, 13]
	else:
		num_list = sieve(sqr_n)
		test_list = list(num_list)
		for i in range(max(num_list),n_max):
			tester = False
			for j in test_list:
				if i%j == 0:
					tester = True
					break	
			if(not(tester)):		
				num_list.append(i)

		for i in num_list[sqr_n:]:
			i_m = i*i
			if(i_m < n_max):
				for j in num_list[i:]:
					if j%i == 0:
						num_list.remove(j)
		return num_list	

start = timeit.default_timer()
print(sum(sieve(False, 2000000)))
stop = timeit.default_timer()

print('Time: ', stop - start)  