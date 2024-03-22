from graph import *
import math

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

def prims_algo(g: ConnectedGraph):
    """pick lowestweight edge, then loop through neighbors and choose
    lowest weight edge to unkown vertex, repeat"""
    assert g.size > 0
    assert len(g.points) > 0
    # simply list of used vertices
    vertices: list[Point] = []
    # list of edges in (p1, p2, weight) form in order of adding. Will become path to return
    path: list[tuple[Point,Point, int]] = []
    # point to start with FIXME have to find minimum weight edge
    low = find_lowest_weight_edge(g)
    while len(vertices) < g.size:
        pass
    return path


def find_lowest_weight_edge(g: Graph) -> tuple[Point, Point, float]:
    """Given a Graph or ConnectedGraph, find the lowest weight edge"""
    ordered = sorted(g.edges, key=lambda edge: edge[2])
    return ordered[0]

            
        


if __name__ == "__main__":
    pass