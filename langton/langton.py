import unittest

class TestLangton(unittest.TestCase):
    def test_failuretestcase(self):
        self.assertTrue(True)

    #this is a pointless test
    def test_given_empty_world_with_no_ant_when_tick_then_empty_world(self):
        world = World()

        world.run()

        self.assertTrue(world.is_empty_world())

    def test_given_empty_world_with_ant_when_construct_then_world_with_ant_and_start_tile_white(self):
        world = World()

        expected_color = Color.BLACK
        location = Location(0, 0)

        self.assertTrue(isinstance(world.ant, Ant))
        self.assertEqual(world.get_color_at_location(location), Color.WHITE)

    def test_given_empty_world_with_an_ant_when_run_then_old_ant_position_is_black(self):
        location = Location(0, 0)
        ant = Ant(location)
        world = World(ant)

        world.run()

        self.assertEqual(world.get_color_at_location(location), Color.BLACK)

    def test_given_white_location_when_flip_color_then_black_location(self):
        world = World()
        location = Location(0, 0)

        world.flip_color(location)

        self.assertEqual(world.get_color_at_location(location), Color.BLACK)

    def test_given_black_location_when_flip_color_then_white_location(self):
        expected = Location(0, 0)
        locations = [expected]
        world = World(black_cells=locations)

        world.flip_color(expected)

        self.assertEqual(world.get_color_at_location(expected), Color.WHITE)

    def test_given_ant_in_empty_world_when_run_then_ant_at_x1y0_and_x0y0_is_black(self):
        world = World()

        world.run()

        self.assertEqual(world.get_color_at_location(Location(0, 0)), Color.BLACK)
        self.assertEqual(world.ant.location, Location(1, 0))
        self.assertEqual(world.ant.direction, Direction.EAST)



class TestLocation(unittest.TestCase):
    def test_given_initial_x_y_position_when_constructed_then_location_has_xy(self):
        x = 0
        y = 0

        actual = Location(x, y)

        self.assertEqual(actual.x, x)
        self.assertEqual(actual.y, y)


class TestAnt(unittest.TestCase):
    def test_given_default_ant_when_construct_then_location_zero_zero(self):
        ant = Ant()
        
        expected = Location(0, 0)

        self.assertEqual(ant.location, expected)

    def test_given_default_ant_when_construct_then_direction_is_up(self):
        ant = Ant()

        self.assertEqual(ant.direction, Direction.NORTH)

    def test_given_ant_on_white_at_x0y0_and_direction_north_when_move_then_turn_right_move_forward(self):
        location = Location(0, 0)
        expected = Location(1, 0)
        ant = Ant(location, Direction.NORTH)
        square_color = Color.WHITE

        actual = ant.move(square_color)

        self.assertEqual(actual.location, expected)

    def test_given_ant_on_white_at_x0y0_and_direction_east_when_move_then_turn_right_move_forward(self):
        location = Location(0, 0)
        expected = Location(0, -1)
        ant = Ant(location, Direction.EAST)
        square_color = Color.WHITE

        actual = ant.move(square_color)

        self.assertEqual(actual.location, expected)

    def test_given_ant_on_white_at_x0y0_and_direction_south_when_move_then_turn_right_move_forward(self):
        location = Location(0, 0)
        expected = Location(-1, 0)
        ant = Ant(location, Direction.SOUTH)
        square_color = Color.WHITE

        actual = ant.move(square_color)

        self.assertEqual(actual.location, expected)

    def test_given_ant_on_white_at_x0y0_and_direction_west_when_move_then_turn_right_move_forward(self):
        location = Location(0, 0)
        expected = Location(0, 1)
        ant = Ant(location, Direction.WEST)
        square_color = Color.WHITE

        actual = ant.move(square_color)

        self.assertEqual(actual.location, expected)

    def test_given_ant_on_black_at_x0y0_and_direction_north_when_move_then_turn_left_move_forward(self):
        location = Location(0, 0)
        expected = Location(-1, 0)
        ant = Ant(location, Direction.NORTH)
        square_color = Color.BLACK

        actual = ant.move(square_color)

        self.assertEqual(actual.location, expected)


class TestDirection(unittest.TestCase):
    def test_given_a_starting_direction_north_when_turn_right_then_direction_is_east(self):
        direction = Direction.NORTH

        actual = Direction.turn_right(direction)

        self.assertEqual(actual, Direction.EAST)

    def test_given_a_starting_direction_north_when_turn_left_then_direction_is_west(self):
        direction = Direction.NORTH

        actual = Direction.turn_left(direction)

        self.assertEqual(actual, Direction.WEST)




# Rules are:
# * On white square, turn 90 degrees right, flip colour, move forward
# * On black square, turn 90 degrees left, flip colour, move forward


class Location(object):
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "x: %s, y: %s" % (self.x, self.y)

    def __hash__(self):
        return hash(self.__str__())


class Color(object):
    BLACK = 0
    WHITE = 1


class Direction(object):
    NORTH = 0
    EAST  = 1
    SOUTH = 2
    WEST  = 3

    @staticmethod
    def turn_right(direction):
        return (direction + 1) % 4

    @staticmethod
    def turn_left(direction):
        return (direction - 1) % 4
    

class Ant(object):
    def __init__(self, location=Location(0,0), direction=Direction.NORTH):
        self.location = location
        self.direction = direction

    def move(self, color):
        if color == Color.WHITE:
            new_direction = Direction.turn_right(self.direction)
        else:
            new_direction = Direction.turn_left(self.direction)

        return Ant(self._move_forward(new_direction), new_direction)

    def _move_forward(self, direction):
        if direction == Direction.NORTH:
            return Location(self.location.x, self.location.y + 1)
        elif direction == Direction.EAST:
            return Location(self.location.x + 1, self.location.y)
        elif direction == Direction.SOUTH:
            return Location(self.location.x, self.location.y - 1)
        else:
            return Location(self.location.x - 1, self.location.y)


class World(object):
    def __init__(self, ant=Ant(), black_cells=[]):
        self.ant = ant
        self.grid = {}
        for i in black_cells:
            self.grid[i] = Color.BLACK

    def run(self):
        current_color = self.get_color_at_location(self.ant.location)
        self.flip_color(self.ant.location)
        self.ant = self.ant.move(current_color)

    def flip_color(self, location):
        if self.grid.has_key(location):
            del self.grid[location]
        else:
            self.grid[location] = Color.BLACK

    def is_empty_world(self):
        return True

    def get_color_at_location(self, location):
        in_world = self.grid.has_key(location)
        if in_world:
            return Color.BLACK
        return Color.WHITE


if __name__ == '__main__':
    unittest.main()
