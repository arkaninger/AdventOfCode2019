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


def add_position_distance(path, position, distance):
    if position not in path.keys():
        path[position] = distance
    return path

def move(start, movement, current_distance):
    if movement.startswith('R'):
        return move_right(start, movement[1:], current_distance)
    elif movement.startswith('L'):
        return move_left(start, movement[1:], current_distance)
    elif movement.startswith('U'):
        return move_up(start, movement[1:], current_distance)
    elif movement.startswith('D'):
        return move_down(start, movement[1:], current_distance)


def move_right(start, movement, current_distance):
    partial_path = dict()
    current_position = start
    for x in range(int(movement)):
        new_position = Coordinate((current_position.get_x() + 1), current_position.get_y())
        current_distance = current_distance + 1
        partial_path = add_position_distance(partial_path, new_position, current_distance)
        current_position = new_position
    return partial_path, current_position, current_distance


def move_left(start, movement, current_distance):
    partial_path = dict()
    current_position = start
    for x in range(int(movement)):
        new_position = Coordinate((current_position.get_x() - 1), current_position.get_y())
        current_distance = current_distance + 1
        partial_path = add_position_distance(partial_path, new_position, current_distance)
        current_position = new_position
    return partial_path, current_position, current_distance


def move_up(start, movement, current_distance):
    partial_path = dict()
    current_position = start
    for x in range(int(movement)):
        new_position = Coordinate((current_position.get_x()), current_position.get_y() + 1)
        current_distance = current_distance + 1
        partial_path = add_position_distance(partial_path, new_position, current_distance)
        current_position = new_position
    return partial_path, current_position, current_distance


def move_down(start, movement, current_distance):
    partial_path = dict()
    current_position = start
    for x in range(int(movement)):
        new_position = Coordinate((current_position.get_x()), current_position.get_y() - 1)
        current_distance = current_distance + 1
        partial_path = add_position_distance(partial_path, new_position, current_distance)
        current_position = new_position
    return partial_path, current_position, current_distance


def merge_two_dicts(x, y):
    # Update x's values with y's values
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z


if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"

    with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
        wire_one = input_file.readline().rstrip('\n').split(',')
        wire_two = input_file.readline().rstrip('\n').split(',')

    starting_point = Coordinate(0, 0)

    # print(wire_one)
    path_one = dict()
    path_one[starting_point] = 0
    next_starting_point = starting_point
    current_distance_one = 0
    for movement_one in wire_one:
        partial_path, next_starting_point, current_distance_one = move(next_starting_point, movement_one, current_distance_one)
        path_one = merge_two_dicts(partial_path, path_one)
    # print(path_one)

    # print(wire_two)
    path_two = dict()
    path_two[starting_point] = 0
    next_starting_point = starting_point
    current_distance_two = 0
    for movement_two in wire_two:
        partial_path, next_starting_point, current_distance_two = move(next_starting_point, movement_two, current_distance_two)
        path_two = merge_two_dicts(partial_path, path_two)
    # print(path_two)

    intersection_points = set(path_one.keys()).intersection(path_two.keys())
    intersection_points.remove(starting_point)
    # print(intersection_points)

    steps = [path_one[intersection] + path_two[intersection] for intersection in intersection_points]
    steps.sort()
    print("The fewest combined steps the wires must take to reach an intersection is", steps[0])
