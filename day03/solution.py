with open("./input.txt", "r") as f:
    corrupted_memory = f.read()

import re

def run_muls(str: str):
    regex = re.compile("mul\((\d+),(\d+)\)")

    muls = regex.findall(str)

    total = 0
    for mul in muls:
        first = int(mul[0])
        second = int(mul[1])
        total += first * second
    
    return total

total = run_muls(corrupted_memory)

print(total)

# Part 2
dos = corrupted_memory.split("do()")

total = 0
for do in dos:
    do_and_dont = do.split("don't()")
    do_part = do_and_dont[0]
    total += run_muls(do_part)

print(total)