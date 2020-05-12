import threading
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print("Done Sleeping...")

#Creating threads: 
#targer: is the function we want to run.
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

threads = []
#Threading inside a loop: 
for _ in range(10):
    t = threading.Thread(target=do_something, args=[5])
    t.start()
    threads.append(t)

for threads in threads:
    threads.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')