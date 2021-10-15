import time
def calculate_time(fnc):
    current_time = time.time()
    fnc()
    return print(f"Total time {time.time() - current_time}")
