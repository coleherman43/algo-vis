import unittest
from graph import *
from algorithms import *


class TestFindLowestWeight(unittest.TestCase):
    points = [Point(0,5), Point(10,15), Point(150,7), Point(8,134)]
    g = ConnectedGraph(4, points)
    g1 = ConnectedGraph(4)
    # find actual answer
    # assert actual answer
    assert len(g.edges) == len(g1.edges)



if __name__ == "__main__":
    unittest.TestCase()