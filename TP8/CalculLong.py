from threading import Thread
from multiprocessing import Process
import sys
import time

def calcul_long(numero):
    n = 1E8
    while n>0:
        n -= 1
    sys.stdout.write(numero)
    sys.stdout.flush()

if __name__ == "__main__":
    thread_1 = Thread(target = calcul_long, args=("thread1 ",))
    thread_2 = Thread(target = calcul_long, args=("thread2 ",))
    thread_3 = Thread(target = calcul_long, args=("thread3 ",))
    thread_4 = Thread(target = calcul_long, args=("thread4 ",))

    print("Début des calculs utilisant les threads")

    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()

    print("\nFin des calculs utilisant les threads\n")

    time.sleep(1)

if __name__ == "__main__":
    process_1 = Process(target = calcul_long, args=("process1 ",))
    process_2 = Process(target=calcul_long, args=("process2 ",))
    process_3 = Process(target = calcul_long, args=("process3 ",))
    process_4 = Process(target = calcul_long, args=("process4 ",))

    print("Début des calculs utilisant les process")

    process_1.start()
    process_2.start()
    process_3.start()
    process_4.start()

    process_1.join()
    process_2.join()
    process_3.join()
    process_4.join()

    print("\nFin des calculs utilisant les process")
