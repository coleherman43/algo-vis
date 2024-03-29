import unittest
from graph import *

class Test_Point(unittest.TestCase):
    """Points have an x, y value and can measure distance between themselves"""

    def test_initialize(self):
        testPoint = Point(10,30)
        expected = "Point(10, 30)"
        assert testPoint == expected

    def test_distance_to(self):
        p1 = Point(0,0)
        p2 = Point(30,40)
        testDist = p1.distance_to(p2)
        expected = 50
        assert testDist == expected


class Test_Graph(unittest.TestCase):
    """Graphs have a size and size number of points inside
    To test, need to be able to be generated from a list of points
    """

    def test_size(self):
        points = [Point(0,5), Point(10,15), Point(150,7), Point(8,134)]
        g1 = Graph(4, points)
        g2 = Graph(4)
        assert len(g1.points) == len(g2.points)

    def test_weighted_connections(self):
        p = [Point(1,5), Point(35, 67), Point(123, 36), Point(90, 150)]
        g = Graph(len(p), p)
        g.connect(g.points[0], g.points[1], 10)
        assert len(g.edges) == 1
        assert g.edges[0][2] == 10
        g.connect(g.points[1], g.points[2], 12)
        assert len(g.edges) == 1
        assert g.edges[1][2] == 12


class TestConnectedGraph(unittest.TestCase):
    """Connected graphs have a specified size (number of points)
    Every point is connected to every other point"""
    def test_connections(self):
        # Prob can calculate number, should just be (n-1)! or something
        size = 5
        g = ConnectedGraph(size)
        assert len(g.edges) == size * (size-1) / 2


if __name__ == "__main__":
    unittest.TestCase()
    print("Tests ran")