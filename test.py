import time

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s \n" % i)

    print("START")

    for i in range(5):
        long_task()

    print("END")
