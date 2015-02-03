import unittest

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    #if node2 not in G:
    #    G[node2] = {}
    #(G[node2])[node1] = 1
    return G



def centrality(G, v):
  #distance_from_start = {}
  distance_from_start = {v: 0}
  open_list = [v]
  def get_distance(v):
    return distance_from_start.get(v, 0)
  while len(open_list) > 0:
    current = open_list[0]
    del open_list[0]
    for neighbor in G[current].keys():
      if neighbor not in distance_from_start:
        print "distance:", distance_from_start
        distance_from_start[neighbor] = distance_from_start[current] + 1
        open_list.append(neighbor)
  return (sum(distance_from_start.values())+0.0) / len(distance_from_start)

def is_actor(k):
  return isinstance(k, basestring)

def import_movies():
  f = open('movies.csv', 'r')
  G = {}

  for line in f:
    line = line.rstrip()
    actor, movie, year = line.split("\t")
    make_link(G, actor, (year, movie))

  return G


class TestSequenceFunctions(unittest.TestCase):
  def test_import(self):
    G = import_movies()
    #print G

    #movies = set()
    total_count = 0
    for actor in G:
      assert is_actor(actor), "Was not an actor: %s" % actor
      for movie in G[actor]:
        assert not is_actor(movie)
        total_count += 1
    self.assertEqual(total_count, 31383)

    names = [
      'Sedaris, Amy',
      'McClure, Marc (I)',
      'Darshi, Agam',
      'Jolie, Angelina',
    ]

    for name in names:
      self.assertTrue(G[name])

    #first = G.items()[0]
    #print first

  def test_top_central(self):
    G = import_movies()

    centralities = {}
    for k,v in G.items():
      if is_actor(k):
        centralities[k] = centrality(G, k)

    best = max(centralities, key=lambda x: centralities[x])

    self.assertEqual(best, "John Smith")
    self.assertEqual(1, 2)

if __name__ == '__main__':
    unittest.main()
