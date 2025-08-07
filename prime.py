import numpy as np
import timeit
import matplotlib.pyplot as plt

def sieve(n):
	num_list = []
	if(n > 6):
		n_max = int(n*(np.log(n)+np.log(np.log(n))))
		sqr_n = int(np.sqrt(n))
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
	else:
		return[2, 3, 5, 7, 11, 13]

start = timeit.default_timer()
x_plot = []
y_plot = []
for i in range(100000):
	array_start = timeit.default_timer()
	sieve(i)
	array_stop = timeit.default_timer()
	x_plot.append(i)
	array_tot = array_stop - array_start
	y_plot.append(array_tot)
	
plot(x_plot, y_plot)
plt.show()

stop = timeit.default_timer()

print('Time: ', stop - start)  