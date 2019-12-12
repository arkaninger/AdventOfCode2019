class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

    def __hash__(self):
        return hash(self.__str__())


def move(start, movement):
    if movement.startswith('R'):
        return move_right(start, movement[1:])
    elif movement.startswith('L'):
        return move_left(start, movement[1:])
    elif movement.startswith('U'):
        return move_up(start, movement[1:])
    elif movement.startswith('D'):
        return move_down(start, movement[1:])


def move_right(start, movement):
    partial_path = set()
    current_position = start
    for x in range(int(movement)):
        new_position = Coordinate((current_position.get_x() + 1), current_position.get_y())
        partial_path.add(new_position)
        current_position = new_position
    return partial_path, current_position


def move_left(start, movement):
    partial_path = set()
    current_position = start
    for x in range(int(movement)):
        new_position = Coordinate((current_position.get_x() - 1), current_position.get_y())
        partial_path.add(new_position)
        current_position = new_position
    return partial_path, current_position


def move_up(start, movement):
    partial_path = set()
    current_position = start
    for x in range(int(movement)):
        new_position = Coordinate((current_position.get_x()), current_position.get_y() + 1)
        partial_path.add(new_position)
        current_position = new_position
    return partial_path, current_position


def move_down(start, movement):
    partial_path = set()
    current_position = start
    for x in range(int(movement)):
        new_position = Coordinate((current_position.get_x()), current_position.get_y() - 1)
        partial_path.add(new_position)
        current_position = new_position
    return partial_path, current_position


def manhattan(coordinate):
    return abs(coordinate.get_x()) + abs(coordinate.get_y())


if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"

    with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
        wire_one = input_file.readline().rstrip('\n').split(',')
        wire_two = input_file.readline().rstrip('\n').split(',')

    starting_point = Coordinate(0, 0)

    # print(wire_one)
    path_one = set()
    path_one.add(starting_point)
    next_starting_point = starting_point
    for movement_one in wire_one:
        partial_path, next_starting_point = move(next_starting_point, movement_one)
        path_one = path_one.union(partial_path)
    # print(path_one)

    # print(wire_two)
    path_two = set()
    path_two.add(starting_point)
    next_starting_point = starting_point
    for movement_two in wire_two:
        partial_path, next_starting_point = move(next_starting_point, movement_two)
        path_two = path_two.union(partial_path)
    # print(path_two)

    intersection_points = path_one.intersection(path_two)
    intersection_points.remove(starting_point)
    # print(intersection_points)
    distances = [manhattan(intersection) for intersection in intersection_points]
    distances.sort()
    print("The Manhattan distance from the central port to the closest intersection is", distances[0])
