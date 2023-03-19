# python3

import heapq

n, m = map(int, input().split())
times = list(map(int, input().split()))

thread_times = [(0, i) for i in range(n)]
thread_job_assignments = [[] for _ in range(n)]

for i in range(m):
    job_time = times[i]
    start_time, thread_id = heapq.heappop(thread_times)
    thread_job_assignments[thread_id].append(i)
    finish_time = start_time + job_time
    heapq.heappush(thread_times, (finish_time, thread_id))
    
for i in range(n):
    print(i, end=' ')
    for j in thread_job_assignments[i]:
        print(j, end=' ')
    print()
