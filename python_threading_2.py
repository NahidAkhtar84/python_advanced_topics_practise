import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print('Sleeping for {seconds} second')
    time.sleep(seconds)
    print('done sleeping')


# we start the threads through a for loop but can not join here as each time loop through to start a new thread
# So we have to store the threads in a list to join
threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for t in threads:
    t.join()




finish = time.perf_counter()

print('Finished in {} seconds'.format(finish-start))

