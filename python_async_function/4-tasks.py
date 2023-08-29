#!/usr/bin/env python3
""" This file create a list of float that have the wait time"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ This file create a list of float that have the wait time"""
    list_float = []
    for i in range(n):
        list_float.append(await(task_wait_random(max_delay)))
    return sorted(list_float)
