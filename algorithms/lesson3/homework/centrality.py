# Old impl: AVERAGE distance
# return maximum distance from node to all the other nodes it can reach

#
# Write centrality_max to return the maximum distance
# from a node to all the other nodes it can reach
#
import pdb

def dfs(G, node, marked, depth_max):
    #print "dfs: %s marked: %s depth: %s" % (node, marked, depth_max)
    #print "dfs: %s depth: %s" % (node, depth_max)
    marked[node] = True
    depths = [depth_max]
    for neighbor in G[node]:
        # pdb.set_trace()
        if neighbor not in marked:
            # print "%s is a neighbor of: %s" % (neighbor, node)
            depth = dfs(G, neighbor, marked, depth_max + 1)
            depths.append(depth)

    depth_max = max(depths)
    # print "depth_max:", depth_max
    return depth_max


def centrality_max(G, v):
    # your code here
    return dfs(G, v, {}, 0)

#################
# Testing code
#
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def test():
    chain = ((1,2), (2,3), (3,4), (4,5), (5,6))
    G = {}
    for n1, n2 in chain:
        make_link(G, n1, n2)
    assert centrality_max(G, 1) == 5
    assert centrality_max(G, 3) == 3
    tree = ((1, 2), (1, 3),
            (2, 4), (2, 5),
            (3, 6), (3, 7),
            (4, 8), (4, 9),
            (6, 10), (6, 11))
    G = {}
    for n1, n2 in tree:
        make_link(G, n1, n2)
    assert centrality_max(G, 1) == 3
    assert centrality_max(G, 11) == 6

test()
