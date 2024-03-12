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
    
    while len(vertices) < g.size:
        pass
    return path


if __name__ == "__main__":
    pass