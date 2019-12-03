with open('input.txt', 'r') as f:
    first_wire = f.readline().strip().split(',')
    second_wire = f.readline().strip().split(',')


class CrossedWires:

    def __init__(self):
        self.grid = {
                'R': (0, 1),
                'U': (1, 0),
                'D': (-1, 0),
                'L': (0, -1)
                }

    def move(self, pos, direction):
        return tuple(map(sum, zip(pos, self.grid.get(direction))))

    def process(self, wire):
        position = (0, 0)
        steps = 0
        points = {}

        for i in wire:
            for _ in range(int(i[1:])):
                steps += 1
                position = self.move(position, direction=i[0])

                if position not in points:
                    points[position] = steps

        return points


if __name__ == '__main__':
    c = CrossedWires()

    steps1 = c.process(first_wire)
    steps2 = c.process(second_wire)

    intersections = steps1.keys() & steps2.keys()

    print(min(abs(p1) + abs(p2) for p1, p2 in intersections))
    print(min(steps1[p] + steps2[p] for p in intersections))
