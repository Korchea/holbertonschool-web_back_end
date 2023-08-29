#!/usr/bin/env python3
""" Create a measure_time function with integers n and max_delay
as arguments that measures the total execution time for
wait_n(n, max_delay), and returns total_time / n. Your function
should return a float.
Use the time module to measure an approximate elapsed time."""
import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ The same that above"""
    time1 = time()
    asyncio.run(wait_n(n, max_delay))
    time2 = time()
    total_time = 0.00
    total_time = time2 - time1
    return total_time / n
