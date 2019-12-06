if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"

    # exercise constraints
    fuel = 0

    with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
        masses = input_file.read().splitlines()
        for mass in masses:
            int_mass = int(mass)
            fuel += (int(mass) // 3) - 2
        print("Total fuel required {0}".format(fuel))
