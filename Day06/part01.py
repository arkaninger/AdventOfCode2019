def extract_center_orbitant(direct_orbit):
    extracted = direct_orbit.split(')')
    return extracted[0], extracted[1]


def get_distance(celest_object, all_orbits):
    if celest_object == "COM":
        return 0
    else:
        orbital_center = all_orbits[celest_object]
        return 1 + get_distance(orbital_center, all_orbits)


if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"

    orbits = {}
    with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
        direct_orbits = input_file.read().splitlines()
        for direct_orbit in direct_orbits:
            center, orbitant = extract_center_orbitant(direct_orbit)
            orbits[orbitant] = center

    total_orbits = 0
    for obj in orbits:
        total_orbits += get_distance(obj, orbits)
    print("Number of direct and indirect orbits:", total_orbits)


