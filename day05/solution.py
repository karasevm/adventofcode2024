import sys
from collections import defaultdict


def parse_input(input_list: list[str]) -> tuple[defaultdict, list[list[str]]]:
    rules = defaultdict(list)
    updates = []
    updates_flag = False
    for line in input_list:
        if line == "":
            updates_flag = True
            continue
        if updates_flag:
            updates.append(line.split(","))
        else:
            rules[line.split("|")[0]].append(line.split("|")[1])
    return (rules, updates)


def part1(input_list: list[str]) -> int:
    rules, updates = parse_input(input_list)
    result = 0

    for update in updates:
        for position, number in enumerate(update):
            if number not in rules.keys():
                continue
            subrules = rules[number]
            for rule in subrules:
                if rule in update[0:position]:
                    break
            else:
                continue
            break
        else:
            mid = update[len(update) // 2]
            result += int(mid)
            continue

    return result


def part2(input_list: list[str]) -> int:
    rules, updates = parse_input(input_list)
    bad_updates: list[list[str]] = []
    result = 0

    for update in updates:
        for position, number in enumerate(update):
            if number not in rules.keys():
                continue
            subrules = rules[number]
            for rule in subrules:
                if rule in update[0:position]:
                    bad_updates.append(update)
                    break
            else:
                continue
            break
        else:
            continue

    modified = True
    while modified:
        modified = False
        for update in bad_updates:
            for position, number in enumerate(update):
                if number not in rules.keys():
                    continue
                subrules = rules[number]
                for rule in subrules:
                    if rule in update[0:position]:
                        update.remove(rule)
                        update.insert(position + 1, rule)
                        modified = True
                else:
                    continue
            else:
                continue

    for update in bad_updates:
        mid = update[len(update) // 2]
        result += int(mid)

    return result


if __name__ == "__main__":
    try:
        f = open(sys.argv[1], "r")
    except IOError:
        print("Error opening the file, try again")
        sys.exit(1)
    with f:
        lines = f.readlines()
        f.close()
        lines = [line.rstrip() for line in lines]
        print(f"Part 1 answer: {part1(lines)} Part 2 answer: {part2(lines)}")
