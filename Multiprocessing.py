import multiprocessing
import concurrent.futures
import time 

"""
Description:
	Python 3.8.5 
Notes:
	

"""


def do_something(seconds):
	print(f'Sleeping {seconds} second(s)')
	time.sleep(1)
	print('Done sleeping')
	
def do_something_else(seconds):
	print(f'Sleeping {seconds} second(s)')
	time.sleep(1)
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

	results = [executor.submit(do_something_else,1) for _ in range(4) ]	
	for f in concurrent.futures.as_completed(results):
		print(f.result())	

finish = time.perf_counter()
print(f'Finished in {round(finish-start,3)} seconds(s)')



