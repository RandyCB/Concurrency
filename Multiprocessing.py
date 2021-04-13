import multiprocessing
import concurrent.futures
import time 

"""
Description:
	Python 3.8.5 
	Program example for multiprocessing using two different methods
	
Notes:
	Multiprocessing is meant to be use in tasks that make high use of the CPU cores
	Using the contex manager will join processes automatically 
	The map method executes the function argument with all the elements of the list argument
	
Test case:
	Intel(R) Core(TM) i3-4005U CPU @ 1.70GHz
	On-line CPU(s) list:             0-3
	Thread(s) per core:              2
	20.04.2 LTS (Focal Fossa)

	Running the Process pool with more than 4 iterations at time
	will cause to execute in more than 1 second 
	since it is related with the HW cores in the PC where it is running	
"""


def do_something(seconds):
	print(f'Sleeping {seconds} second(s)')
	time.sleep(1)
	print('Done sleeping')
	
def do_something_else(seconds):
	print(f'Sleeping {seconds} second(s)')
	time.sleep(seconds)
	return 'Done sleeping'


#-------------------------------------------------------------------------------
#Old method
processes = []
start = time.perf_counter()

for _ in range(10):
	
	p = multiprocessing.Process(target=do_something, args=[1])
	p.start()
	processes.append(p)

for process in processes:
	process.join()


finish = time.perf_counter()
print(f'Finished in {round(finish-start,3)} seconds(s)')

print(" "*3)
#-------------------------------------------------------------------------------
#newer method
start = time.perf_counter()

with concurrent.futures.ProcessPoolExecutor() as executor:

	results = [executor.submit(do_something_else,1) for _ in range(5) ]	
	for f in concurrent.futures.as_completed(results):
		print(f.result())	

finish = time.perf_counter()
print(f'Finished in {round(finish-start,3)} seconds(s)')

print(" "*3)
#-------------------------------------------------------------------------------
#Using map function instead

start = time.perf_counter()
s = [5,4,3,2,1]
with concurrent.futures.ProcessPoolExecutor() as executor:
	results = executor.map(do_something_else, s)

	for result in results:
		print(result)


finish = time.perf_counter()
print(f'Finished in {round(finish-start,3)} seconds(s)')





