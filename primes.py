import time

# The idea I had in the call- doubtful of whether it passed

class goodSolution:
    def solve(self, n: int):
        origin = time.perf_counter_ns()
        if n < 2:
            return []

        def prime_list(num: int):
            if num < 3:
                return {2: True}
            
            init = {i: True for i in range(2, num + 1)}
            for i in prime_list(int((num ** 0.5) // 1 + 1)):
                for composite in range(i * 2, num + 1, i):
                    if composite > num: break
                    init.pop(composite, None)
            return list(init.keys())
        full = prime_list(n)
        print("SOLVE TIME:", (time.perf_counter_ns() - origin) * 10**-6, "ms")
        return full
        
solver = goodSolution()

testCases = [
    2, 10, 21, 41, 67, 100, 1000, 10000, 100000
]
fullOrigin = time.perf_counter_ns()
for case in testCases:
    print(f"Testing case: {case}")
    complete = solver.solve(case)
    if case > 1000:
        print("First 10 primes:", complete[:10])
        print("Last 10 primes:", complete[-10:])
    print(len(complete), "primes found")

print("FULL TIME:", (time.perf_counter_ns() - fullOrigin) * 10**-6, "ms")