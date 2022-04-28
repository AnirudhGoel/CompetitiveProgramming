from math import atan2

def get_mirrors_from_all_walls(room_x, room_y, player_x, player_y):
    return {(player_x, 2 * room_y - player_y), (2 * room_x - player_x, player_y), (player_x, -player_y), (-player_x, player_y), }


def squared_distance_between(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2


def get_valid_mirrors_as_per_distance(my_x, my_y, mirrors, distance):
    valid_mirrors = set()

    for mirror in mirrors:
        mirror_x = mirror[0]
        mirror_y = mirror[1]

        if squared_distance_between(my_x, my_y, mirror_x, mirror_y) <= distance**2:
            valid_mirrors.add(mirror)

    return valid_mirrors


def get_valid_mirrors(room_x, room_y, my_x, my_y, player_x, player_y, distance):
    all_mirrors = {(player_x, player_y), }

    # Using 2 sets because sets are unordered so cannot iterate like a list
    curr_mirror_set = {(player_x, player_y), }

    while curr_mirror_set:
        curr_player_x, curr_player_y = curr_mirror_set.pop()

        # mirrors is a set of all 4 reflections of player's current position
        mirrors = get_mirrors_from_all_walls(room_x, room_y, curr_player_x, curr_player_y)

        # remove mirrors which are already present in all_mirrors
        mirrors = mirrors - all_mirrors

        distance_validated_mirrors = get_valid_mirrors_as_per_distance(my_x, my_y, mirrors, distance)

        # after validating distance remaining mirrors are unioned to both sets
        curr_mirror_set = curr_mirror_set | distance_validated_mirrors
        all_mirrors = all_mirrors | distance_validated_mirrors

    return all_mirrors


def get_angle_min_distance_map(my_x, my_y, mirrors):
    angle_min_distance_map = dict()

    for mirror in mirrors:
        mirror_x = mirror[0]
        mirror_y = mirror[1]

        # my mirrors have 1 entry for my original position - skip that case
        if mirror_x == my_x and mirror_y == my_y:
            continue

        current_mirror_distance = squared_distance_between(my_x, my_y, mirror_x, mirror_y)

        angle_with_x_axis = atan2((mirror_y-my_y), (mirror_x-my_x))

        # if the current angle doesn't exist in dict or if the distance for current angle in dict is larger than current mirror dist
        if not angle_min_distance_map.get(angle_with_x_axis, None) or angle_min_distance_map[angle_with_x_axis] > current_mirror_distance:
            angle_min_distance_map[angle_with_x_axis] = current_mirror_distance

    return angle_min_distance_map


def get_room_corner_angle_distance_map(room_x, room_y, my_x, my_y):
    corner_coordinates = [[0, 0], [0, room_y], [room_x, 0], [room_x, room_y]]
    corner_angle_distance_map = dict()

    for corner in corner_coordinates:
        corner_x = corner[0]
        corner_y = corner[1]

        corner_angle_with_x_axis = atan2((corner_y-my_y), (corner_x-my_x))

        corner_angle_distance_map[corner_angle_with_x_axis] = squared_distance_between(my_x, my_y, corner_x, corner_y)

    return corner_angle_distance_map


def solution(dimensions, your_position, trainer_position, distance):
    room_x, room_y = dimensions
    my_x, my_y = your_position
    trainer_x, trainer_y = trainer_position

    # check here if original distance between you and trainer is < distance of laser
    if squared_distance_between(my_x, my_y, trainer_x, trainer_y) > distance**2:
        return 0

    if squared_distance_between(my_x, my_y, trainer_x, trainer_y) == distance**2:
        return 1

    # these mirrors include the original position of the trainer as well
    all_valid_trainer_mirrors = get_valid_mirrors(room_x, room_y, my_x, my_y, trainer_x, trainer_y, distance)

    # these mirrors include my original position as well
    all_valid_my_mirrors = get_valid_mirrors(room_x, room_y, my_x, my_y, my_x, my_y, distance)

    trainer_angle_min_distance_map = get_angle_min_distance_map(my_x, my_y, all_valid_trainer_mirrors)

    my_angle_min_distance_map = get_angle_min_distance_map(my_x, my_y, all_valid_my_mirrors)

    all_trainer_angles = list(trainer_angle_min_distance_map)

    for trainer_angle in all_trainer_angles:
        if trainer_angle in my_angle_min_distance_map and my_angle_min_distance_map[trainer_angle] <= trainer_angle_min_distance_map[trainer_angle]:
            del trainer_angle_min_distance_map[trainer_angle]

    room_corner_angle_distance_map = get_room_corner_angle_distance_map(room_x, room_y, my_x, my_y)

    room_corner_angles = list(room_corner_angle_distance_map)

    # remove all angles where beam hits corner of room before hitting trainer
    for room_angle in room_corner_angles:
        if room_angle in trainer_angle_min_distance_map and room_corner_angle_distance_map[room_angle] <= trainer_angle_min_distance_map[room_angle]:
            del trainer_angle_min_distance_map[room_angle]

    return len(trainer_angle_min_distance_map.keys())

print(solution([2,5], [1,2], [1,4], 11))
