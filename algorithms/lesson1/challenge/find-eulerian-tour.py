import unittest

use_harder_tests = True

# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_starting_node(edges):
    degrees = get_degree(edges)
    #print "find starting node: " + str(edges)
    print "INITIAL degrees: " + str(degrees)

    max_degree = (0, 0)
    for node, degree in degrees.iteritems():
        if degree % 2 == 1: return node
        if degree > max_degree[0]: max_degree = (degree, node)
    return max_degree[1]

def find_edge(origin, edges):
    candidates = []
    for edge in edges:
        src, dest = edge
        if src == origin or dest == origin:
            candidates.append((edge, get_destination(origin, edge)))
    if candidates:
        degrees = get_degree(edges)
        max_degree = (0, None)
        print "degrees:", degrees
        for candidate in candidates:
            degree = degrees[candidate[1]]
            edge = candidate[0]
        #for node, degree in degrees.iteritems():
            if degree > max_degree[0]: max_degree = (degree, edge)
        # use the edge that doesn't paint us into a corner
        print "edge with max degree:", max_degree
        return max_degree[1]
    else:
        raise Exception("Unable to find a valid edge given origin: %s and edges: %s" % (origin, edges))

def find_edges(origin, edges):
    candidates = []
    for edge in edges:
        src, dest = edge
        if src == origin or dest == origin:
            candidates.append((edge, get_destination(origin, edge)))
    return candidates

def get_destination(source, edge):
    assert edge is not None
    a, b = edge
    if a == source:
        return b
    elif b == source:
        return a
    else:
        return None

def find_eulerian_recursive(accum, edges):
    print "find_eulerian_recursive(%s, %s)" % (accum, edges)
    if not edges:
        print "all done!"
        return accum
    else:
        if not accum:
            print "finding starting node"
            starting_node = find_starting_node(edges)
            return find_eulerian_recursive([starting_node], edges)
        else:
            here = accum[-1]
            local_edges = find_edges(here, edges)
            print "edges found:", local_edges
            for edge, destination in local_edges:
                print "edge found:" + str(edge)
                #destination = get_destination(here, edge)
                print "destination: " + str(destination)
                try:
                    new_accum = list(accum)
                    new_edges = list(edges)
                    new_accum.append(destination)
                    new_edges.remove(edge)
                    result = find_eulerian_recursive(new_accum, new_edges)

                    first_node = result[0][0]
                    last_node = result[-1][1]
                    #if result[0][0] is not result[-1][1]
                    if first_node != last_node:
                        raise Exception("graph is not an eulerian tour!")
                    else:
                        return result
                except Exception, e:
                    print "Found an invalid result. Exception:", e
        #raise Exception("Failed early with the following edges not visited: %s" % edges)
        raise Exception("Failed early with edges not visited.")

def get_degree(tour):
    degree = {}
    for x, y in tour:
        degree[x] = degree.get(x, 0) + 1
        degree[y] = degree.get(y, 0) + 1
    return degree

def find_eulerian_tour(graph):
    print "find_eulerian_tour:", graph
    return find_eulerian_recursive([], graph)

def count_occurrences(traversal):
    count = {}
    for x in traversal:
        count[x] = count.get(x, 0) + 1
    return count

class TestTour(unittest.TestCase):
    # def test_even(self):
    #     edges = [(1, 2), (2, 3), (3, 1)]
    #     possible_tour = [1, 2, 3, 1]
    #     self.assertEqual(find_eulerian_tour(edges), possible_tour)

    # def test_odd(self):
    #     edges = [
    #             (1, 2),
    #             (1, 4),
    #             (2, 3),
    #             (3, 4),
    #             (4, 1)
    #             ]
    #     possible_tour = [1, 2, 3, 4, 1, 4]
    #     self.assertEqual(find_eulerian_tour(edges), possible_tour)

    sample_graphs = [
            [
            (0, 1),
            (0, 4),
            (1, 5),
            (1, 6),
            (1, 7),
            (2, 4),
            (2, 5),
            (3, 6),
            (3, 7),
            (4, 5),
            (4, 8),
            (5, 9),
            (8, 9)],

        [(1, 13), (1, 6), (6, 11), (3, 13),
        (8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),
        (1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),
        (7, 14),  (10, 13)],

        [(8, 16), (8, 18), (16, 17), (18, 19),
        (3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14),
        (1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15),
        (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]
    ]


    def test_graph_0(self):
        print "test graph 0"
        graph = self.sample_graphs[0]
        tour = find_eulerian_tour(graph)
        self.assertEqual(len(tour), 14)
        expected = [1, 7, 3, 6, 1, 5, 4, 8, 9, 5, 2, 4, 0, 1]
        self.assertEqual(count_occurrences(tour), count_occurrences(expected))

    def test_graph_1(self):
        print "test graph 1"
        graph = self.sample_graphs[1]
        tour = find_eulerian_tour(graph)
        self.assertEqual(len(tour), len(graph) + 1)
        # expected = [1, 7, 3, 6, 1, 5, 4, 8, 9, 5, 2, 4, 0, 1]
        # self.assertEqual(count_occurrences(tour), count_occurrences(expected))

    def test_graph_2(self):
        print "test graph 2"
        graph = self.sample_graphs[2]
        tour = find_eulerian_tour(graph)
        self.assertEqual(len(tour), len(graph) + 1)
        #expected = [1, 7, 3, 6, 1, 5, 4, 8, 9, 5, 2, 4, 0, 1]
        #self.assertEqual(count_occurrences(tour), count_occurrences(expected))

    def test_hard_graph(self):
        graph = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 2),
                (4, 5), (5, 6), (6, 4), (6, 7), (7, 8), (8, 6),
                (8, 9), (9, 10), (10, 8), (10, 11), (11, 12), (12, 10),
                (12, 13), (13, 14), (14, 15), (15, 16),
                (16, 14), (16, 17), (17, 18), (18, 16), (18, 19),
                (19, 20), (20, 18), (20, 21), (21, 22), (22, 20),
                (22, 23), (23, 24), (24, 22), (24, 25), (25, 26), (26, 24),
                (26, 27), (27, 28), (28, 26), (28, 29), (29, 30), (30, 28),
                (30, 31), (31, 32), (32, 30), (32, 33), (33, 34),
                (34, 32), (34, 35), (35, 36), (36, 34),
                (36, 37), (37, 38), (38, 36), (38, 39), (39, 40),
                (40, 38), (40, 41), (41, 42), (42, 40), (42, 43),
                (43, 44), (44, 42), (44, 45), (45, 46), (46, 44),
                (46, 47), (47, 48), (48, 46), (48, 49), (49, 50),
                (50, 48), (50, 51), (51, 52), (52, 50), (52, 53),
                (53, 54), (54, 52), (54, 55), (55, 56), (56, 54),
                (56, 57), (57, 58), (58, 56), (58, 59), (59, 60),
                (60, 58), (60, 61), (61, 62), (62, 60), (62, 63),
                (63, 64), (64, 62), (64, 65), (65, 66), (66, 64),
                (66, 67), (67, 68), (68, 66), (68, 69), (69, 70), (70, 68),
                (70, 71), (71, 72), (72, 70), (72, 73), (73, 74), (74, 72),
                (74, 75), (75, 76), (76, 74), (76, 77), (77, 78), (78, 76),
                (78, 79), (79, 80), (80, 78), (80, 81), (81, 82), (82, 80),
                (82, 83), (83, 84), (84, 82), (84, 85), (85, 86), (86, 84),
                (86, 87), (87, 88), (88, 86), (88, 89), (89, 90), (90, 88),
                (90, 91), (91, 92), (92, 90), (92, 93), (93, 94), (94, 92),
                (94, 95), (95, 96), (96, 94), (96, 97), (97, 98), (98, 96),
                (98, 99), (99, 100), (100, 98)]

        tour = find_eulerian_tour(graph)
        #self.assertEqual(len(tour), len(graph) + 1)
        self.assertEqual(tour, None)


if __name__ == '__main__':
    unittest.main()

