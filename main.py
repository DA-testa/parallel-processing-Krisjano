import heapq

def parallel_processing(n, m, times):
    
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)
    results = []
    
    for i in range(m):
        job_time = times[i]
        start_time, thread_id = heapq.heappop(threads)
        results.append((thread_id, start_time))
        start_time += job_time
        heapq.heappush(threads, (start_time, thread_id))
    return results

if __name__ == "__main__":
    n, m = map(int, input().split())
    times = list(map(int, input().split()))

    results = parallel_processing(n, m, times)

    for thread_id, start_time in results:
        print(thread_id, start_time)
