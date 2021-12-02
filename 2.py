from utils import get_input


source = [val.split(" ") for val in get_input(day=2).split("\n")]
source = [(val[0], int(val[1])) for val in source]

horizontal, depth = 0, 0

for instruction, value in source:
    if instruction == "forward":
        horizontal += value
    if instruction == "down":
        depth += value
    if instruction == "up":
        depth -= value


print("PART 1")
print(f"{horizontal} - {depth} total: {horizontal * depth} \n")

horizontal, depth, aim = 0, 0, 0

for instruction, value in source:
    if instruction == "forward":
        horizontal += value
        depth += aim * value
    if instruction == "down":
        aim += value
    if instruction == "up":
        aim -= value

print("PART 2")
print(f"{horizontal} - {depth} total: {horizontal * depth}")
