from utils import get_input


source = [int(val) for val in get_input(day=1).split("\n")]
result = len([1 for i in range(len(source) - 1) if source[i + 1] > source[i]])
print(f"Part 1 - {result}")

count = 0
currentSum = sum(source[:3])

for i in range(3, len(source)):
    newSum = currentSum + source[i] - source[i - 3]
    if newSum > currentSum:
        count += 1
    currentSum = newSum

print(f"Part 2 - {count}")
