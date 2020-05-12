# import concurrent.futures
# import time

# start = time.perf_counter()

# def do_something(seconds):
#     print(f"Sleeping {seconds} second(s)...")
#     time.sleep(seconds)
#     return f"Done Sleeping...{seconds}"

# #Creating threads: 
# #targer: is the function we want to run.
# # t1 = threading.Thread(target=do_something)
# # t2 = threading.Thread(target=do_something)

# # t1.start()
# # t2.start()

# # t1.join()
# # t2.join()

# #context manager: 
# with concurrent.futures.ThreadPoolExecutor() as executor: 
#     # f1 = executor.submit(do_something, 1)
#     # f2 = executor.submit(do_something, 1)
#     secs = [5,4,3,2,1]
#     results = executor.map(do_something, secs)
#     for result in results: 
#         print(result)
#     # result = [executor.submit(do_something, sec) for sec in secs]
#     # for f in concurrent.futures.as_completed(result): 
#     #     print(f.result())

# # threads = []
# # #Threading inside a loop: 
# # for _ in range(10):
# #     t = threading.Thread(target=do_something, args=[1.5])
# #     t.start()
# #     threads.append(t)

# # for threads in threads:
# #     threads.join()

# finish = time.perf_counter()
# print(f'Finished in {round(finish-start, 2)} second(s)')


import threading
import time


class ThreadingExample(object):
    """ Threading example class

    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor

        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            print('Doing something imporant in the background')

            time.sleep(self.interval)

example = ThreadingExample()
time.sleep(3)
print('Checkpoint')
time.sleep(2)
print('Bye')