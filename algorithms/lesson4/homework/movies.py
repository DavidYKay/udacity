import unittest
import operator
import math
from joblib import Parallel, delayed

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
       G[node2] = {}
    (G[node2])[node1] = 1
    return G



def centrality(G, v):
  print "finding centrality for:", v
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
        #print "distance:", distance_from_start
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

def setItem(d, k, v):
  print "setItem: %s[%s] = %s" % (d, k, v)
  d[k] = v

#def make_centrality(G, k):


class TestSequenceFunctions(unittest.TestCase):
  def test_import(self):
    G = import_movies()
    #print G

    #movies = set()
    total_count = 0
    for actor in G:
      #assert is_actor(actor), "Was not an actor: %s" % actor
      for movie in G[actor]:
        #assert not is_actor(movie)
        total_count += 1
    self.assertEqual(total_count, 31383 * 2)

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

  def test_top_central_subset(self):
    G = import_movies()

    centralities = {}

    names = [
        'Jackson, Samuel L.',
        'Hoffman, Dustin',
        'De Niro, Robert',
        'Morrison, Rana',]

    for k in names:
      centralities[k] = centrality(G, k)

    best = max(centralities, key=lambda x: centralities[x])
    print centralities

    self.assertEqual(best, "De Niro, Robert")
    #self.assertEqual(centralities[best], 2)


  def test_top_central_all(self):
    G = import_movies()

    counter = 0
    centralities = {}


    # for k,v in G.items():
    #   if is_actor(k):
    #     print "checking actor %s" % counter
    #     centralities[k] = centrality(G, k)
    #     counter += 1
    centralities = {k:centrality(G,k) for k,v in G.items() if is_actor(k)}

    #centralities = Parallel(n_jobs=6)(delayed(math.sqrt)(i ** 2) for i in range(10))
    #centralities = Parallel(n_jobs=6)(delayed(math.sqrt)(i ** 2) for i in range(10))

    #results = Parallel(n_jobs=6)(delayed(setItem)(centralities, i, 9) for i in range(10))
    #results = Parallel(n_jobs=2)(delayed(centrality)(G, k) for k,v in G.items() if is_actor(k))
    #results = Parallel(n_jobs=1, backend="threading")(delayed(centrality)(G, k) for k,v in G.items() if is_actor(k))

    #centralities = Parallel(n_jobs=6)(delayed(i) for i in range(10))
    #centralities = Parallel(n_jobs=6)[i for i in range(10)]
    #print "results:", results

    print "centralities:", centralities

    sorted_x = sorted(centralities.items(), key=operator.itemgetter(1))
    target_a = sorted_x[19:20]
    target_b = sorted_x[-20:-19]

    print "# actors:", len(centralities)

    print "target A:", target_a
    print "target B:", target_b

    best = max(centralities, key=lambda x: centralities[x])
    print "best:", best


    self.assertEqual(best, "John Smith")
    self.assertEqual(centralities[best], 2)
    self.assertEqual(len(centralities), 2)

if __name__ == '__main__':
    unittest.main()
