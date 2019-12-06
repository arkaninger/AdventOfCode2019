if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"

    with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
        program = input_file.read().split(',')
        program = [int(x) for x in program]
        program[1] = 12
        program[2] = 2
        pointer = 0
        while pointer <= program.__len__():
            op_code = program[pointer]
            input1_position = program[pointer + 1]
            input2_position = program[pointer + 2]
            output_position = program[pointer + 3]
            if op_code == 1:
                program[output_position] = program[input1_position] + program[input2_position]
            elif op_code == 2:
                program[output_position] = program[input1_position] * program[input2_position]
            elif op_code == 99:
                break
            pointer += 4
    print("Value at position 0 is {0}".format(program[0]))
