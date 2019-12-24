def extract_center_orbitant(direct_orbit):
    extracted = direct_orbit.split(')')
    return extracted[0], extracted[1]


if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"

    orbits = {}
    with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
        direct_orbits = input_file.read().splitlines()
        for direct_orbit in direct_orbits:
            center, orbitant = extract_center_orbitant(direct_orbit)
            orbits[orbitant] = center

    you_orbit_object = "YOU"
    santa_orbit_object = "SAN"
    you_path_to_COM = []
    santa_path_to_COM = []
    while you_orbit_object != "COM":
        you_path_to_COM.append(orbits[you_orbit_object])
        you_orbit_object = orbits[you_orbit_object]
    while santa_orbit_object != "COM":
        santa_path_to_COM.append(orbits[santa_orbit_object])
        santa_orbit_object = orbits[santa_orbit_object]

    common_objects = set(you_path_to_COM) ^ set(santa_path_to_COM)
    print("Travel distance:", len(common_objects))
