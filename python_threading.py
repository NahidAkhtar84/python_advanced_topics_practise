import time
import threading

start = time.perf_counter()

def do_something():
    print('Sleeping for 1 second')
    time.sleep(1)
    print('done sleeping')


t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)
# Start the threads to run
t1.start()
t2.start()
# while our threads were running fto sleep for 1 second,,rest of the code executes so,,
# to hold the code till sleeping and waiting for rest of the code to run we had to use joi
t1.join()
t2.join()

finish = time.perf_counter()

print('Finished in {} seconds'.format(finish-start))

