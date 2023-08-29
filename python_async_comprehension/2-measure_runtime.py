#!/usr/bin/env python3
""" The coroutine will collect 10 random numbers using an async
comprehensing over async_generator, then return the 10 random numbers."""
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ The coroutine will collect 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random
    numbers."""
    time1 = time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    time2 = time()
    return time2 - time1
