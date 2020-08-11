import threading
import datetime


class MyThread(threading.Thread):

    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.ThreadID = counter
        self.Name = name
        self.Counter = counter

    def run(self):
        print("\nStarting the thread" + self.Name)
        print_date(self.Name, self.Counter)
        print("Exiting the thread" + self.Name)


def print_date(threadName, counter):
    dateField = []
    today = datetime.date.today()
    dateField.append(today)
    print('{}[{}]: {}'.format(threadName, counter, dateField[0]))


# To Create new thread

thread1 = MyThread("Thread1", 1)
thread2 = MyThread("Thread2", 2)

# To Start new thread

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Exiting from threading")
