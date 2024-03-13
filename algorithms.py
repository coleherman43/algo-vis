from graph import *
import math

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
    low = find_lowest_weight(g)
    while len(vertices) < g.size:
        pass
    return path


def find_lowest_weight(g: Graph) -> tuple[Point, Point, int]:
    """Given a Graph or ConnectedGraph, find the lowest weight edge"""
    low = g.edges[0][2]
    res = g.edges[0]
    for edge in g.edges:
        if edge[2] < low:
            res = edge
            low = edge[2]
    return res

            
        


if __name__ == "__main__":
    pass