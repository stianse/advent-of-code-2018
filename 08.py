#!/usr/bin/env python3

with open('08.txt') as f:
    for line in f:
        tree_spec = map(int, line.split())

class Node(object):
    def __init__(self):
        self.childs = []
        self.meta = []

    def sum_meta(self):
        ret = sum(self.meta)
        for child in self.childs:
            ret += child.sum_meta()
        return ret

    def get_value(self):
        if not self.childs:
            return sum(self.meta)
        value = 0
        for m in self.meta:
            if m == 0 or m > len(self.childs):
                continue
            value += self.childs[m - 1].get_value()
        return value


def make_node(spec):
    node = Node()
    num_childs = next(spec)
    num_meta = next(spec)

    for x in range(num_childs):
        child_node = make_node(spec)
        node.childs.append(child_node)

    for x in range(num_meta):
        meta = next(spec)
        node.meta.append(meta)

    return node


root = make_node(tree_spec)
# Part 1
print(root.sum_meta())
# Part 2
print(root.get_value())
