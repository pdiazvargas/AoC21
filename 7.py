from utils import get_input

source = [int(val) for val in get_input(day=7).split(",")]
# source = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
max_value = max(source) + 1


def cost1(position):
    return sum((sum(i for i in abs(val - position)) for val in source))


def cost2(position):
    result = 0
    for val in source:
        diff = abs(val - position)
        result += (diff * (diff + 1)) / 2
    return result


cost_by_index = {cost1(position): position for position in range(max_value)}
min_val = min(cost_by_index.keys())

print("Part 1")
print(f"Move to: {cost_by_index[min_val]} Costs: {min_val}")

cost_by_index = {cost2(position): position for position in range(max_value)}
min_val = min(cost_by_index.keys())

print("Part 2")
print(f"Move to: {cost_by_index[min_val]} Costs: {min_val}")
