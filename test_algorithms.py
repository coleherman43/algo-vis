import unittest
from graph import *
from algorithms import *

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

class TestFindLowestWeight(unittest.TestCase):
    
    def test_find_lowest_weight_edge(self):    
        a = Point(0,5)
        b = Point(10,15)
        c = Point(150,7)
        d = Point(8,134)
        points = [a,b,c,d]
        g = ConnectedGraph(4, points)
        log.debug(g.edges)
        # find actual answer
        dist1 = a.distance_to(b)
        dist2 = a.distance_to(c)
        dist3 = a.distance_to(d)
        dist4 = b.distance_to(c)
        dist5 = b.distance_to(d)
        dist6 = c.distance_to(d)
        ans = min(dist1, dist2, dist3, dist4, dist5, dist6)
        # assert actual answer
        found = find_lowest_weight_edge(g)
        assert ans == found[2], f"Lowest weights are different: {found[2]} is not {ans}"



if __name__ == "__main__":
    unittest.TestCase()
    print("Tests ran")