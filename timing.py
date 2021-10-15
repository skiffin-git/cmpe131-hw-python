import time
def calculate_time(fnc):
    def func():
        current_time = time.time()
        fnc()
        return print(f"Total time {time.time() - current_time}")
    return func
