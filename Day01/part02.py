def calculate_fuel(input_mass):
    new_mass = input_mass
    fuel = 0
    while True:
        partial_fuel = (new_mass // 3) - 2
        if partial_fuel > 0:
            fuel += partial_fuel
            new_mass = partial_fuel
        else:
            break
    return fuel

if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"

    # exercise constraints
    fuel = 0

    with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
        masses = input_file.read().splitlines()
        for mass in masses:
            fuel += calculate_fuel(int(mass))
        print("Total fuel required {0}".format(fuel))
