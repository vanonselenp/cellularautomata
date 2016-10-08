import unittest
import ast

class TestWorld(unittest.TestCase):
    def test_given_world_with_cell_when_get_neighbours_return_six(self):
        cells = [[0, 0]]
        world = World(cells)

        neighbours = world.get_neighbours([0, 0])

        self.assertTrue(len(neighbours) == 6)

    def test_given_world_with_single_cell_when_run_cell_is_dead(self):
        cells = [[0, 0]]
        world = World(cells)

        world.run()

        self.assertFalse(world.is_alive(cells[0]))

    def test_world_with_three_cells_when_run_thenm_remain_alive(self):
        cells = [
            [1, 1],
            [1, 2],
            [2, 2]
        ]
        world = World(cells)

        world.run()

        self.assertTrue(world.is_alive(cells[0]))

    def test_world_with_two_cells_when_run_cell_is_dead(self):
        cells = [
            [1, 1],
            [2, 2]
        ]
        world = World(cells)

        world.run()

        self.assertFalse(world.is_alive(cells[0]))


class World(object):
    def __init__(self, cells=[]):
        defaults = [
            [1, 1],
            [1, 2],
            [2, 2]
        ]

        if len(cells) == 0:
            cells = defaults

        self.cells = cells

    def run(self):
        newcells = []
        agg_cells = {}

        for cell in self.cells:
            neighbours = self.get_neighbours(cell)
            for n in neighbours:
                key = repr(n)
                agg_cells[key] = agg_cells.get(key, 0) + 1

        for cell in agg_cells:
            c = ast.literal_eval(cell)
            if agg_cells[cell] == 3 or (agg_cells[cell] == 2 and c in self.cells):
                newcells.append(c)

        self.cells = newcells

    def is_alive(self, cell):
        return cell in self.cells

    def get_neighbours(self, cell):
        # due to hex structure these are the neighbours
        offset = 0
        if cell[0] % 2:
            offset = 1
        
        result = [
            [cell[0] - 1 + offset, cell[1] - 1],
            [cell[0] + offset, cell[1] - 1],
            [cell[0] - 1, cell[1]],
            [cell[0] + 1, cell[1]],
            [cell[0] - 1 + offset, cell[1] + 1],
            [cell[0] + offset, cell[1] + 1]
        ]
        return result



if __name__ == '__main__':
    unittest.main()

