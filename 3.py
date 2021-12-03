from utils import get_input
from collections import defaultdict

counts = defaultdict(int)
source = [val for val in get_input(day=3).split("\n")]

result = [defaultdict(int) for i in range(len(source[0]))]
for reading in source:
    for idx, char in enumerate(reading):
        result[idx][char] += 1

gamma = "".join(["0" if entry["0"] > entry["1"] else "1" for entry in result])
epsilon = "".join(["0" if entry["0"] < entry["1"] else "1" for entry in result])

print(source[:10])
print(f"gamma: {gamma} => {int(gamma, 2)}")
print(f"epsilon: {epsilon} => {int(epsilon, 2)}")
print("PART 1")
print(int(gamma, 2) * int(epsilon, 2))

"""
Before searching for either rating value, start with the full list of binary numbers from
your diagnostic report and consider just the first bit of those numbers. Then:

Keep only numbers selected by the bit criteria for the type of rating value for which you
are searching. Discard numbers which do not match the bit criteria.
If you only have one number left, stop; this is the rating value for which you are searching.
Otherwise, repeat the process, considering the next bit to the right.

The bit criteria depends on which type of rating value you want to find:
- To find oxygen generator rating, determine the most common value (0 or 1) in the
current bit position, and keep only numbers with that bit in that position. If
0 and 1 are equally common, keep values with a 1 in the position being considered.
- To find CO2 scrubber rating, determine the least common value (0 or 1) in the
current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
"""


def getCountsAtIndex(values, index):
    result = {"0": 0, "1": 0}
    for value in values:
        result[value[index]] += 1
    return result


def getMostCommonBit(values, index):
    counts = getCountsAtIndex(values, index)
    return "0" if counts["0"] > counts["1"] else "1"


def getLeastCommonBit(values, index):
    counts = getCountsAtIndex(values, index)
    return "0" if counts["0"] <= counts["1"] else "1"


def filter(values, index, target):
    return [value for value in values if value[index] == target]


oxygenValues = source
for index in range(len(source[0])):
    target = getMostCommonBit(oxygenValues, index)
    oxygenValues = filter(oxygenValues, index, target)
    if len(oxygenValues) == 1:
        break

co2Values = source
for index in range(len(source[0])):
    target = getLeastCommonBit(co2Values, index)
    co2Values = filter(co2Values, index, target)
    if len(co2Values) == 1:
        break

print("")
print(f"oxygen reading: {oxygenValues[0]} => {int(oxygenValues[0], 2)}")
print(f"CO2 reading: {co2Values[0]} => {int(co2Values[0], 2)}")
print("PART 2")
print(int(oxygenValues[0], 2) * int(co2Values[0], 2))
