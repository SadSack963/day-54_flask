# day-54-1-exercise

import time

# current_time = time.time()
# print(current_time)


def speed_calc_decorator(function):
    def calc():
        t0 = time.time()
        function()
        t1 = time.time()
        print(f"{function.__name__} run speed: {t1 - t0} seconds")

    return calc


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
