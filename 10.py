from utils import get_input
from functools import reduce

source = [row for row in get_input(day=10).split("\n")]

# source = [
#     "[({(<(())[]>[[{[]{<()<>>",
#     "[(()[<>])]({[<{<<[]>>(",
#     "{([(<{}[<>[]}>{[]{[(<()>",
#     "(((({<>}<{<{<>}{[]{[]{}",
#     "[[<[([]))<([[{}[[()]]]",
#     "[{[{({}]{}}([{[{{{}}([]",
#     "{<[[]]>}<{[{[{[]{()[[[]",
#     "[<(<(<(<{}))><([]([]()",
#     "<{([([[(<>()){}]>(<<{{",
#     "<{([{{}}[<[[[<>{}]]]>[]]",
# ]

matching_pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def get_corrupted_char(line):
    stack = []

    for char in line:
        if char in ("(", "[", "{", "<"):
            stack.append(char)
            continue
        if char == matching_pairs[stack[-1]]:
            stack.pop()
        else:
            return char

    return None


assert get_corrupted_char("()") is None
assert get_corrupted_char("([])") is None
assert get_corrupted_char("{()()()}") is None
assert get_corrupted_char("<([{}])>") is None
assert get_corrupted_char("[<>({}){}[([])<>]]") is None
assert get_corrupted_char("(((((((((())))))))))") is None


assert get_corrupted_char("{([(<{}[<>[]}>{[]{[(<()>") == "}"
assert get_corrupted_char("[[<[([]))<([[{}[[()]]]") == ")"
assert get_corrupted_char("[{[{({}]{}}([{[{{{}}([]") == "]"
assert get_corrupted_char("[<(<(<(<{}))><([]([]()") == ")"
assert get_corrupted_char("<{([([[(<>()){}]>(<<{{") == ">"

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

score = 0
for line in source:
    corrupted_char = get_corrupted_char(line)
    if corrupted_char is None:
        continue
    score += scores[corrupted_char]

print("Part 1")
print(score)


def get_complete_by(line):
    stack = []

    for char in line:
        if char in ("(", "[", "{", "<"):
            stack.append(char)
            continue
        if char == matching_pairs[stack[-1]]:
            stack.pop()

    if len(stack) == 0:
        return []

    return "".join(reversed([matching_pairs[value] for value in stack]))


scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

to_check = [line for line in source if get_corrupted_char(line) is None]


def matching_as_str(line):
    return "".join(get_complete_by(line))


assert matching_as_str("[({(<(())[]>[[{[]{<()<>>") == "}}]])})]"
assert matching_as_str("[(()[<>])]({[<{<<[]>>(") == ")}>]})"
assert matching_as_str("(((({<>}<{<{<>}{[]{[]{}") == "}}>}>))))"
assert matching_as_str("{<[[]]>}<{[{[{[]{()[[[]") == "]]}}]}]}>"
assert matching_as_str("<{([{{}}[<[[[<>{}]]]>[]]") == "])}>"


autocomplete_scores = []
# print(len(to_check))
for line in to_check:
    autocorrect = get_complete_by(line)
    # print("".join(autocorrect))
    score = 0
    for char in autocorrect:
        score = 5 * score + scores[char]
    autocomplete_scores.append(score)

print("Part 2")
# print(autocomplete_scores)

autocomplete_scores = sorted(autocomplete_scores)
print(autocomplete_scores[len(autocomplete_scores) // 2])
