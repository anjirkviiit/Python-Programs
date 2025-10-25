import time

def my_execution(func):
    def wrapper():
        start_time = time.perf_counter()
        func()
        end_time = time.perf_counter()
        print(end_time-start_time)
    return wrapper

@my_execution
def calc_sum():
    x=5
    y=10
    print(x+y)
    
if __name__ == "__main__":
    calc_sum()