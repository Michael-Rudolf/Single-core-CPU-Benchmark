import time
import sys

sys.set_int_max_str_digits(100000000)
last_number = 1
current_number = 1

for _ in range(1000000000):
    new_current_number = current_number + last_number
    last_number = current_number
    current_number = new_current_number
    print(current_number)

