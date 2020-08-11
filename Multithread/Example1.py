from threading import *
import time

class Hell0(Thread):

    def run(self):
        for i in range (6):
            print("Hello")
            time.sleep(1)

class Hi(Thread):

    def run(self):
        for i in range(6):
            print("Hi")
            time.sleep(1)

s1 = Hell0()

s2 = Hi()

s1.start()
time.sleep(.2)
s2.start()

s1.join()
s2.join()

print("Bye")