"""
Section 3
Concurrency, CPU Bound vs I/O Bound - CPU Bound(2) - Multiprocessing

Keyword - CPU Bound, 

"""
# CPU-Bound Multiprocessing 예제(https://realpython.com/python-concurrency/#synchronous-version)

from multiprocessing import current_process, Array, freeze_support, Process, Manager
import time
import os
import threading
import queue

def cpu_bound2(number, output):

    thread_name = threading.current_thread().getName()
    process_name = current_process().name

    # Process 정보 출력
    print(f"Thread Name: {thread_name}, Process Name: {process_name}")

    result = sum(i * i for i in range(number))

    output.put(result)

def main():

    numbers = [3_000_000 + x for x in range(30)]
    
    out_pipeline = queue.Queue(maxsize=30)

    threads = list()

    # 실행시간 측정
    start_time = time.time()

    # 프로세스 생성 및 실행
    for i in numbers: # 1 ~ 100 적절히 조절
        # 생성
        #t = Process(name=str(i), target=cpu_bound, args=(i,total_list,))
        x = threading.Thread(target=cpu_bound2, args=(i, out_pipeline,), daemon=False)
        # 배열에 담기
        threads.append(x)
        # 시작
        x.start()

    # Join
    for thread in threads:
        thread.join()

    print()
    
    sums = 0

    while not out_pipeline.empty():
        sums = sums+out_pipeline.get()

    # 실행 시간 종료
    duration = time.time() - start_time

    print()

    # 수행 시간
    print(sums)
    print(f"Duration : {duration} seconds")

if __name__ == "__main__":
    # 윈도우 예외시 
    # freeze_support()
    
    # 메인 함수 실행
    main()