
from threading import Thread
import time

class Hello(Thread):
    
    def run(self):
        for _ in range(50):
            print('hello')
            time.sleep(.5)

    
class Hi(Thread):

    def run(self):
        for _ in range(50):
            print('hi')
            time.sleep(.5)


hello = Hello()
hi = Hi()

hello.start()
hi.start()

# We are using join here to say the main thred to wait and hello and hi thread to join
# the execution. so,,after executing hello and hi thread jobs, then main thread will come in action and print bye
Hello.join()
hi.join()

print('Bye')