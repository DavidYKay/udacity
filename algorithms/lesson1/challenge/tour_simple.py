import pdb, traceback, sys, code

def get_degree(tour):
    degree = {}
    for x, y in tour:
        degree[x] = degree.get(x, 0) + 1
        degree[y] = degree.get(y, 0) + 1
    return degree

def find_starting_node(edges):
    degrees = get_degree(edges)
    #print "find starting node: " + str(edges)
    print "degrees: " + str(degrees)

    max_degree = (0, 0)
    for node, degree in degrees.iteritems():
        if degree % 2 == 1: return node
        if degree > max_degree[0]: max_degree = (degree, node)
    #return edges[0][0]
    return max_degree[1]

def check_edge(t, b, nodes):
    """
    t: tuple representing an edge
    b: origin node
    nodes: set of nodes already visited

    if we can get to a new node from `b` following `t`
    then return that node, else return None
    """
    if t[0] == b:
        if t[1] not in nodes:
            return t[1]
    elif t[1] == b:
        if t[0] not in nodes:
            return t[0]
    return None

def connected_nodes(tour):
    """return the set of nodes reachable from
    the first node in `tour`"""
    a = tour[0][0]
    nodes = set([a])
    explore = set([a])
    while len(explore) > 0:
        # see what other nodes we can reach
        b = explore.pop()
        for t in tour:
            node = check_edge(t, b, nodes)
            if node is None:
                continue
            nodes.add(node)
            explore.add(node)
    return nodes

def bfs_graph(edges):
    """Takes in all the edges of the graph and visits all the nodes at least once
    """
    a = edges[0]
    traversal = []
    explore = set(a)
    while len(explore) > 0:
        here = explore.pop()
        for edge in edges:
            # see if this node is reachable from where we are
            node = check_edge(edge, here, traversal)
            if node is None:
                # if so, add it to the explore list
                #traversal.add(node)
                explore.add(node)
            else:
                continue
        traversal.append(b)
    return nodes

def bfs_recursive(position, traversed, edges):
    if not edges:
        return traversed
    potentials = get_potentials(position, edges)
    next_edge = get_highest_degree(potentials)
    new_pos = get_destination(position, next_edge)
    traversed.append(new_pos)
    edges.remove(next_edge)
    return bfs_recursive(new_pos, traversed, edges)

def bfs(edges):
    return bfs_recursive(edges[0][0], [], edges)

