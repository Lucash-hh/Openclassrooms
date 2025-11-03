import time

def measure_execution_time():
    start = time.time()
    for i in range(10001):
        i = 2+2
        end = time.time()
    return f"Execution time :  {end - start} seconds"
    
    
print(measure_execution_time())