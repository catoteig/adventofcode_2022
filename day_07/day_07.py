import re


# Fetched from https://www.geeksforgeeks.org/sum-elements-n-ary-tree/ and modified
class Node:
    def __init__(self):
        self.size = 0
        self.name = ''
        self.children = []
        self.parent = None


def newNode(size, name, parent):
    temp = Node()
    temp.size = size
    temp.name = name
    temp.parent = parent
    temp.children = []
    return temp


def sumNodes(root):
    Sum = 0

    if root == None:
        return 0

    q = []
    q.append(root)

    while len(q) != 0:
        n = len(q)

        while n > 0:
            p = q[0]
            q.pop(0)
            Sum += p.size

            for i in range(len(p.children)):
                q.append(p.children[i])
            n -= 1
    return Sum


def main():
    with open('input.txt') as f:
        commands = [_ for _ in f.read().splitlines()]

    root = newNode(0, '/', None)
    curr_node = root
    all_directories = [root]

    total_disc_space = 70000000
    needed_disc_space = 30000000

    for command in commands:
        if re.fullmatch('^\$ cd /$', command):
            curr_node = root
        elif re.fullmatch('^\$ ls$', command):
            continue
        elif re.fullmatch('^\$ cd \w*$', command):
            directory = command.split(' ')[-1]
            dir = filter(lambda x: x.name == directory, curr_node.children)
            curr_node = next(dir)
        elif re.fullmatch('\$ cd \.{2}$', command):
            curr_node = curr_node.parent
        else:
            p1, p2 = command.split(' ')
            if p1 == 'dir':
                curr_node.children.append(n := newNode(0, p2, curr_node))
                all_directories.append(n)
            else:
                curr_node.children.append(newNode(int(p1), p2, curr_node))

    # Part 1
    total_size = 0
    for node in all_directories:
        if (size := sumNodes(node)) <= 100*1000:
            total_size += size

    print(total_size)

    # Part 2
    used_disc_size = sumNodes(root)
    to_delete = needed_disc_space - (total_disc_space - used_disc_size)
    values = []
    for node in all_directories:
        if (size := sumNodes(node)) >= to_delete:
            values.append(size)

    print(min(values))


if __name__ == '__main__':
    main()
