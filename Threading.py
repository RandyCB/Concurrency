import time
import threading
import concurrent.futures


"""
Description
	Python 3.8.5 

Notes:
	CPU bound processes => use multiprocessing (alot of computation like math)
	IO bound processes => use threading (waiting long time to end a process, downloding large files)	
	the underscore in the for loop is used as a throw away variable
	
Test case:
	Intel(R) Core(TM) i3-4005U CPU @ 1.70GHz
	20.04.2 LTS (Focal Fossa)
	
	using the thread pool method of threading, with a for loop of 9>= the 
	process will execute in more than a second while using the threading module
	will execute in a ~1 with 10 iterations
	
"""

def do_something(seconds):
	print(f'Sleeping {seconds} s...')
	time.sleep(seconds)
	print('done sleeping')
	
def do_something_else(seconds):
	print(f'Sleeping {seconds} s...')
	time.sleep(seconds)
	return 'done sleeping'
	
	
start = time.perf_counter()
threads = []
for _ in range(10):
	t = threading.Thread(target=do_something, args=[1])  		#arg pass the argument into the target function
	t.start()
	threads.append(t)

for thread in threads:
	thread.join()								#avoids the script to run concurrently

finish = time.perf_counter()
print(f'Finished in {round(finish-start,3)} seconds(s)')


print('\n'*3)


start2 = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:			#context manager
	results = [executor.submit(do_something_else,1) for _ in range(10)]	#list comprehension statement
	
	for f in concurrent.futures.as_completed(results):
		print(f.result())
		
		
finish2 = time.perf_counter()
print(f'Finished in {round(finish2-start2,3)} seconds(s)')	
