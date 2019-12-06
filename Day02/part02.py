if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"

    # exercise constraints
    desired_output = 19690720

    found = False

    for noun in range(0, 99):
        for verb in range(0, 99):
            with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
                program = input_file.read().split(',')
                program = [int(x) for x in program]
                program[1] = noun
                program[2] = verb
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
                if program[0] == desired_output:
                    found = True
                    print("100 * noun + verb is {0}".format(100 * noun + verb))
            if found:
                break
        if found:
            break
