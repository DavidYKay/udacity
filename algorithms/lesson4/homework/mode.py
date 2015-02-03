#
# Given a list L of n numbers, find the mode
# (the number that appears the most times).
# Your algorithm should run in Theta(n).
# If there are ties - just pick one value to return
#
from operator import itemgetter


def mode(L):
  counts = {}
  def record(item):
    print "counting item:", item
    if item in counts:
      counts[item] += 1
    else:
      counts[item] = 1

  for item in L:
    record(item)

  record = (0, 0)
  for item in L:
    count = counts[item]
    if count > record[0]:
      print "new high count found. %s for %s" % (count, item)
      high = count
      record = (count, item)
  return record[1]

####
# Test
#
import time
from random import randint

def test():
    result = mode([1, 5, 2, 5, 3, 5])
    assert 5 == result, "Mode was %s but should have been %s" % (result, 5)
    iterations = (10, 20, 30, 100, 200, 300, 1000, 5000, 10000, 20000, 30000)
    times = []
    for i in iterations:
        L = []
        for j in range(i):
            L.append(randint(1, 10))
        start = time.clock()
        for j in range(500):
            mode(L)
        end = time.clock()
        print start, end
        times.append(float(end - start))
    slopes = []
    for (x1, x2), (y1, y2) in zip(zip(iterations[:-1], iterations[1:]), zip(times[:-1], times[1:])):
        print (x1, x2), (y1, y2)
        slopes.append((y2 - y1) / (x2 - x1))
    # if mode runs in linear time,
    # these factors should be close (kind of)
    print slopes

test()

