import subprocess
import threading

def count_to_1000():
    for i in range(1, 1001):
        print(i)

def sayA():
    print("a")

def sayB():
    print("b")

if __name__ == "__main__":
    # Define threads for sayA, count_to_1000, and sayB
    thread_a = threading.Thread(target=sayA)
    thread_count = threading.Thread(target=count_to_1000)
    thread_b = threading.Thread(target=sayB)
    
    # Start the threads
    thread_a.start()
    thread_count.start()
    thread_b.start()
    
    # Wait for count_to_1000 to finish before proceeding
    thread_count.join()
