from math import prod
import pprint
from collections import defaultdict


def parse_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        monkeys = {}
        while lines:
            monkeys[m := lines.pop(0)[:-1]] = {}
            monkeys[m]['start_items'] = [int(_) for _ in lines.pop(0).split(': ')[1].split(', ')]
            monkeys[m]['operation'] = [int(_) if _.isdigit() else _ for _ in lines.pop(0).split('= ')[1].split(' ')[1:]]
            monkeys[m]['test'] = {}
            monkeys[m]['test']['divisible_by'] = int(lines.pop(0).split(' ')[-1])
            monkeys[m]['test']['if_true'] = int(lines.pop(0).split(' ')[-1])
            monkeys[m]['test']['if_false'] = int(lines.pop(0).split(' ')[-1])
            if lines: lines.pop(0)
        return monkeys


def main():
    monkeys = parse_file('input.txt')

    items = defaultdict(list)
    for monkey in monkeys: items[monkey] = monkeys[monkey]['start_items']

    # Used the internet to figure this out...
    modulo = prod([_['test']['divisible_by'] for _ in monkeys.values()])

    inspected = defaultdict(int)
    for monkey in monkeys: inspected[monkey] = 0
    throw_to_list = []

    for _ in range(10*1000):
        for monkey in monkeys:

            # Inspect item
            for i, item in enumerate(items[monkey]):
                inspected[monkey] += 1
                operator, op_value = monkeys[monkey]['operation']
                worry_level = 0
                if op_value == 'old':
                    worry_level = item * item
                elif operator == '*':
                    worry_level = item * op_value
                elif operator == '+':
                    worry_level = item + op_value

                # worry_level //= 3 # Part 1
                worry_level %= modulo  # Part 2

                items[monkey][i] = worry_level
                if worry_level % monkeys[monkey]['test']['divisible_by'] == 0:
                    throw_to_list.append(monkeys[monkey]['test']['if_true'])
                else:
                    throw_to_list.append(monkeys[monkey]['test']['if_false'])

            # Throw item
            for item, throw_to in zip(items[monkey], throw_to_list):
                items[f'Monkey {str(throw_to)}'].append(item)
            items[monkey].clear()
            throw_to_list.clear()

    print(sorted(inspected.values())[-1] * sorted(inspected.values())[-2])


if __name__ == '__main__':
    main()
