import time
from concurrent.futures import ThreadPoolExecutor

#Change for pull

def Collatz(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def ParallelCollatz(N, num_threads):

    nums = list(range(1, N + 1))
    results = [0] * N

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(Collatz, num) for num in nums]
        for i, future in enumerate(futures):
            results[i] = future.result()

    avg_steps = sum(results) / len(results)

    return avg_steps, results



N = 20000
num_threads = 6

start_time = time.time()

avg_steps_dynamic, results_dynamic = ParallelCollatz(N, num_threads)

end_time = time.time()

execution_time = end_time - start_time

print(f"Середня кількість кроків: {avg_steps_dynamic}")
#print(f"Results (dynamic): {results_dynamic}")
print(f"Час виконання: {execution_time:.4f} сек.")
