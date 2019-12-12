def has_two_adjacents(candidate):
    str_candidate = str(candidate)
    for i in range(str_candidate.__len__() - 1):
        equals_among = str_candidate[i] == str_candidate[i + 1]
        prev_diff = (i == 0 or str_candidate[i - 1] != str_candidate[i])
        next_diff = (i + 2 == str_candidate.__len__() or str_candidate[i + 2] != str_candidate[i+1])
        if equals_among and (prev_diff and next_diff):
            return True
    return False


def never_decreases(candidate):
    str_candidate = str(candidate)
    for i in range(str_candidate.__len__() - 1):
        if str_candidate[i] > str_candidate[i + 1]:
            return False
    return True


def is_password(candidate):
    # We know from the input it'll always be a six-digit number
    # and will be within the range in the input
    return has_two_adjacents(candidate) and never_decreases(candidate)


if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"

    # for example in [112233, 123444, 111122]:
    #     print(str(example), "is_password?", is_password(example))

    with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
        input_range = [int(element) for element in input_file.readline().rstrip('\n').split('-')]
    verified_candidates = 0
    for candidate in range(input_range[0], (input_range[1]) + 1):
        if is_password(candidate):
            verified_candidates += 1
    print("The number of different passwords within the range given in the puzzle input meeting the criteria is",
          str(verified_candidates))
