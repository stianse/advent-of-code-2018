#!/usr/bin/env python3

with open('09.txt') as f:
    line = f.read().split()
    NUM_PLAYERS = int(line[0])
    LAST_MARBLE = int(line[6])

class Marble(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def get_neighbour(self, offset):
        ret = self
        if offset > 0:
            for i in range(offset):
                ret = ret.next
        else:
            for i in range(-offset):
                ret = ret.prev
        return ret

def get_winning_score(num_players, last_marble):
    points = [0] * num_players
    player = 0

    current = Marble(0)
    current.prev = current
    current.next = current

    for value in range(1, last_marble+1):
        if value % 23 == 0:
            pop = current.get_neighbour(-7)
            points[player] += value + pop.value
            pop.prev.next = pop.next
            pop.next.prev = pop.prev
            current = pop.next
        else:
            new = Marble(value)
            neighbour = current.get_neighbour(1)
            new.prev = neighbour
            new.next = neighbour.next
            new.prev.next = new
            new.next.prev = new
            current = new

        player = (player + 1) % NUM_PLAYERS

    return max(points)

print('Part 1', get_winning_score(NUM_PLAYERS, LAST_MARBLE))
print('Part 2', get_winning_score(NUM_PLAYERS, LAST_MARBLE * 100))
