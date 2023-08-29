#!/usr/bin/env python3
"""It is an async function that wait a random time and then finally"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """It is an async function that wait a random time and then finally"""
    ran_num = random.uniform(0, max_delay)
    await asyncio.sleep(ran_num)
    return ran_num
