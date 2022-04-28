from math import atan2


class FightRoom:
    """
    Initialises a room assuming its bottom left corner at origin of a cartesian plane.
    Also, initialises two points inside the room for our own position and trainer's (opponent) position.
    Finally, initialises the max distance that the laser beam can travel before becoming faint
    """
    def __init__(self, dimensions, your_position, trainer_position, distance):
        self.room_x, self.room_y = dimensions
        self.my_x, self.my_y = your_position
        self.trainer_x, self.trainer_y = trainer_position
        self.distance = distance

    def check_corner_cases(self):
        """
        Checks for corner cases like the beam is too faint to reach the target even directly or just enough.
        :return:
        """
        if self.squared_distance_between(self.my_x, self.my_y, self.trainer_x,
                                               self.trainer_y) > self.distance ** 2:
            return True, 0

        if self.squared_distance_between(self.my_x, self.my_y, self.trainer_x,
                                               self.trainer_y) == self.distance ** 2:
            return True, 1

        return False, None

    def squared_distance_between(self, x1, y1, x2, y2):
        """
        We use square of distance in all calculations as it's easier to work with sq than sqrt
        :param x1: x coordinate of point 1
        :param y1: y coordinate of point 1
        :param x2: x coordinate of point 2
        :param y2: y coordinate of point 2
        :return: distance between point 1 and point 2
        """
        return (x1 - x2)**2 + (y1 - y2)**2

    def get_mirrors_in_first_quadrant(self, player_x, player_y):
        """
        Calculates all reflections of player that fall in distance range of laser in 1st quadrant
        :param player_x: player's x-coordinate
        :param player_y: player's y-coordinate
        :return: list containing all distance-validated reflections
        """
        mirrors_against_Y_axis = [[player_x, player_y]]
        multiplier = 1

        # mirrors against Y axis
        while True:
            last_mirror_x = mirrors_against_Y_axis[-1][0]
            mirrored_x = self.room_x * multiplier + (self.room_x * multiplier - last_mirror_x)

            if self.squared_distance_between(self.my_x, self.my_y, mirrored_x, player_y) <= self.distance**2:
                mirrors_against_Y_axis.append([mirrored_x, player_y])
                multiplier += 1
            else:
                break

        # now mirror each point against X axis
        all_mirrors = list()
        for mirror in mirrors_against_Y_axis:
            mirrors_of_single_point_against_X_axis = [[mirror[0], mirror[1]]]
            current_x = mirror[0]
            multiplier = 1

            # mirror this point against X axis
            while True:
                last_mirror_y = mirrors_of_single_point_against_X_axis[-1][1]
                mirrored_y = self.room_y * multiplier + (self.room_y * multiplier - last_mirror_y)

                if self.squared_distance_between(self.my_x, self.my_y, current_x, mirrored_y) <= self.distance**2:
                    mirrors_of_single_point_against_X_axis.append([current_x, mirrored_y])
                    multiplier += 1
                else:
                    break

            all_mirrors.extend(mirrors_of_single_point_against_X_axis)

        return all_mirrors


    def mirror_to_other_quadrant(self, mirrors, x_multiplier, y_multiplier):
        """
        Calculates distance-validated reflections of passed coordinates based on passed multipliers
        :param mirrors: list of coordinates to be mirrored
        :param x_multiplier: factor to adjust x coordinate with
        :param y_multiplier: factor to adjust y coordinate with
        :return: list of all distance-validated reflections in another quadrant
        """
        other_quad_mirror = list()

        for mirror in mirrors:
            mirrored_x, mirrored_y = mirror[0] * x_multiplier, mirror[1] * y_multiplier

            if self.squared_distance_between(self.my_x, self.my_y, mirrored_x, mirrored_y) <= self.distance**2:
                other_quad_mirror.append([mirrored_x, mirrored_y])

        return other_quad_mirror


    def get_valid_mirrors(self, player_x, player_y):
        """
        Calls utility functions to calculate distance-validated reflections of player in all quadrants.
        Calculates reflections mathematically for 1st quadrant and then mirrors it into other quadrants.
        :param player_x: x-coordinate of player to calculate reflections for
        :param player_y: y-coordinate of player to calculate reflections for
        :return: list of all distance-validated reflections in all quadrants
        """
        first_quad_mirrors = self.get_mirrors_in_first_quadrant(player_x, player_y)

        second_quad_mirrors = self.mirror_to_other_quadrant(first_quad_mirrors, -1, 1)
        third_quad_mirrors = self.mirror_to_other_quadrant(first_quad_mirrors, -1, -1)
        fourth_quad_mirrors = self.mirror_to_other_quadrant(first_quad_mirrors, 1, -1)

        return first_quad_mirrors + second_quad_mirrors + third_quad_mirrors + fourth_quad_mirrors


    def get_angle_min_distance_map(self, mirrors):
        """
        Creates a dictionary which contains angles as keys and for each angle contains the distance of the first
        point that falls on the line starting from our position and making that angle with the X axis.
        It does so by traversing over each point passed to it and then checking the angle that the line, from that point
        to our position, makes with the X-axis.
        :param mirrors: points to check for angles
        :return: dict with keys as angles and values as minimum distance a point has on the line with that angle
        """
        angle_min_distance_map = dict()

        for mirror in mirrors:
            mirror_x = mirror[0]
            mirror_y = mirror[1]

            # my mirrors have 1 entry for my original position - skip that case
            if mirror_x == self.my_x and mirror_y == self.my_y:
                continue

            current_mirror_distance = self.squared_distance_between(self.my_x, self.my_y, mirror_x, mirror_y)

            angle_with_x_axis = atan2((mirror_y - self.my_y), (mirror_x - self.my_x))

            # if the current angle doesn't exist in dict or if the distance for current angle in dict is larger than current mirror dist
            if not angle_min_distance_map.get(angle_with_x_axis, None) or angle_min_distance_map[angle_with_x_axis] > current_mirror_distance:
                angle_min_distance_map[angle_with_x_axis] = current_mirror_distance

        return angle_min_distance_map


    def get_room_corner_angle_distance_map(self):
        """
        :return: Returns dictionary with keys as angles of corners of the room and values as the distance they have
        from our position
        """
        corner_coordinates = [[0, 0], [0, self.room_y], [self.room_x, 0], [self.room_x, self.room_y]]
        corner_angle_distance_map = dict()

        for corner in corner_coordinates:
            corner_x = corner[0]
            corner_y = corner[1]

            corner_angle_with_x_axis = atan2((corner_y - self.my_y), (corner_x - self.my_x))

            corner_angle_distance_map[corner_angle_with_x_axis] = self.squared_distance_between(self.my_x, self.my_y, corner_x, corner_y)

        return corner_angle_distance_map


def solution(dimensions, your_position, trainer_position, distance):
    trainer_x, trainer_y = trainer_position
    my_x, my_y = your_position

    # initialise fight_room object
    fight_room = FightRoom(dimensions, your_position, trainer_position, distance)

    # check if we have a corner case
    is_corner_case, return_value = fight_room.check_corner_cases()
    if is_corner_case:
        return return_value

    # these are distance validated mirrors and include the original position of the trainer as well
    all_valid_trainer_mirrors = fight_room.get_valid_mirrors(trainer_x, trainer_y)

    # these are distance validated mirrors and include our original position as well
    all_valid_my_mirrors = fight_room.get_valid_mirrors(my_x, my_y)

    # creates a mapping of angles that the line passing through us and each trainer reflection makes with x-axis and
    # values are distance of the first point that falls on the line that makes that angle
    trainer_angle_min_distance_map = fight_room.get_angle_min_distance_map(all_valid_trainer_mirrors)

    # creates similar mapping for our reflections
    my_angle_min_distance_map = fight_room.get_angle_min_distance_map(all_valid_my_mirrors)

    # remove angles where we hit ourselves (our reflections) before hitting the trainer
    all_trainer_angles = list(trainer_angle_min_distance_map)
    for trainer_angle in all_trainer_angles:
        if trainer_angle in my_angle_min_distance_map and my_angle_min_distance_map[trainer_angle] <= trainer_angle_min_distance_map[trainer_angle]:
            del trainer_angle_min_distance_map[trainer_angle]

    # remove angles where beam hits corner of room before hitting trainer
    room_corner_angle_distance_map = fight_room.get_room_corner_angle_distance_map()
    room_corner_angles = list(room_corner_angle_distance_map)
    for room_angle in room_corner_angles:
        if room_angle in trainer_angle_min_distance_map and room_corner_angle_distance_map[room_angle] <= trainer_angle_min_distance_map[room_angle]:
            del trainer_angle_min_distance_map[room_angle]

    return len(trainer_angle_min_distance_map.keys())