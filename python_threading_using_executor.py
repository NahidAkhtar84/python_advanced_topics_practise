import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} second')
    time.sleep(seconds)
    return (f'done sleeping of {seconds}')

with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something, 1)
    # f2 = executor.submit(do_something, 1)
    # print(f1.result())
    # print(f2.result())

    # Use for loop
    
    #this is for declared one second
    # result = [executor.submit(do_something, 1) for _ in range(10)]
    
    # If we want to use random seconds
    secs = [5,4,5,3,4,2,1]
    result = [executor.submit(do_something, sec) for sec in secs]
    for f in concurrent.futures.as_completed(result):
        print(f.result())



finish = time.perf_counter()

print('Finished in {} seconds'.format(finish-start))

