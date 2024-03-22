"""Create a graph with some number of points to run algorithms on"""

import math
from random import randint
import matplotlib.pyplot as plt
import time

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

SIZE = 10 # size is the number of vertices in the graph
WAIT_TIME = 4 # wait time is the time between adding each edge for visualizations in seconds

class Point:
    """Points have (x,y) coordinates and can calculate distance between each other
    Ex: Point(0,0) and Point(3,4) distance_to = 5
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def distance_to(self, other: "Point") -> float:
        return math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))
    
    def __eq__(self, other: "Point") -> bool:
        return self.x == other.x and self.y == other.y


class Graph:
    """Graphs have a size, which is the # of random (or specified) points within it,
    have optional format and weights for manual input of graphs
    Wrapper for list of Points
    Ex. Graph(10) makes a graph with 10 random points
    """

    def __init__(self, size: int, format: list[Point]=[]):
        self.size = size
        self.points: list[Point] = []
        # edges are stored as (point1, point2, weight)
        self.edges: list[tuple[Point, Point, float]] = []
        # Generate a graph depending on if there are present points or not
        self.generate_from_list(format) if format else self.generate_points()

    def generate_points(self, draw_size: int=200):
        used = set()
        while len(used) < self.size:
            x,y = randint(0,200), randint(0,draw_size)
            if (x,y) not in used:
                used.add((x,y))
                self.points.append(Point(x,y))

    def generate_from_list(self, format: list[Point]):
        for point in format:
            self.points.append(point)

    def connect(self, p1: Point, p2: Point, weight: float):
        assert p1 in self.points and p2 in self.points, "Both points must be in the graph"
        assert (p1, p2, weight) not in self.edges and (p2, p1, weight) not in self.edges, "Edge already exists"
        assert weight != 0, "Weight can't be 0"
        self.edges.append((p1, p2, weight))

    def draw(self):
        plt.figure(figsize=(5,5))
        # Draw points
        for point in self.points:
            plt.plot(point.x, point.y, 'bo')
        # Draw edges
        for edge in self.edges:
            p1, p2, weight = edge
            plt.plot([p1.x, p2.x], [p1.y, p2.y], 'k-')
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Graph of Points and Edges")
        plt.show()

    def draw_incremental(self):
        fig, ax = plt.subplots(figsize=(5,5))
        
        # Draw initial points without edges
        for point in self.points:
            ax.plot(point.x, point.y, 'bo')
        
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_title("Graph of Points with Weighted Edges")

        plt.show(block=False)

        for edge in self.edges:
            p1, p2, weight = edge  # Unpack the edge tuple
            # Calculate the midpoint of the edge for text placement
            midpoint_x = (p1.x + p2.x) / 2
            midpoint_y = (p1.y + p2.y) / 2
            # Draw each edge
            ax.plot([p1.x, p2.x], [p1.y, p2.y], 'k-')
            # Place the weight text near the midpoint of the edge
            ax.text(midpoint_x, midpoint_y, str(weight), color='red', fontsize=9)
            
            fig.canvas.draw()
            time.sleep(WAIT_TIME)  # Pause to make the drawing of each edge visible
            fig.canvas.flush_events()
            

        plt.show()

    def draw_points(self):
        plt.figure(figsize=(5,5))
        for point in self.points:
            plt.plot(point.x, point.y, 'bo')
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Graph of Points")
        plt.show()

    def draw_edges(self):
        for edge in self.edges:
            p1, p2, weight = edge
            midpoint_x = (p1.x + p2.x) / 2
            midpoint_y = (p1.y + p2.y) / 2
            plt.text(midpoint_x, midpoint_y, str(weight), color='red', fontsize=9)
            plt.plot([p1.x, p2.x], [p1.y, p2.y], 'k-')


class ConnectedGraph(Graph):
    """Connected graphs are graphs wheere there are edges between vertices (complete by default)
    """

    def __init__(self, size: int, format: list[Point]=[]):
        # make self.size, self.points, 
        super().__init__(size)
        log.debug(f"Edges: {self.edges}")
        # if a format is specified, create given connected graph. Else randomly generate
        # self.generate_from_list(format) if format else self.generate_points(size)
        self._connect_all()
        log.debug(f"Edges: {self.edges}")
    
    def _connect_all(self):
        for i in range(self.size):
            for a in range(i+1, self.size):
                point1 = self.points[i]
                point2 = self.points[a]
                assert point1 is not point2
                dist = point1.distance_to(point2)
                self.connect(point1, point2, dist)






    
    



if __name__ == "__main__":
    g = Graph(SIZE)
    # For preset values:
    # g = Graph(4, [Point(0,5), Point(10,15), Point(150,7), Point(8,134)])
    # g.draw_points()
    p1 = g.points[0]
    p2 = g.points[1]
    g.connect(p1, p2, 4)
    g.connect(g.points[2], g.points[3], 2)
    g.connect(g.points[4], g.points[5], 7)
    g.connect(g.points[5], g.points[6], 10)
    g.draw_incremental()
    print("Graph executed")
