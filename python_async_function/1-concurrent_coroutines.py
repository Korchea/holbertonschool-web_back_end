#!/usr/bin/env python3
""" This file create a list of float that have the wait time"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ This file create a list of float that have the wait time"""
    list_float = []
    for i in range(n):
        list_float.append(await(wait_random(max_delay)))
    return sorted(list_float)
