import math
#
# write up_heapify, an algorithm that checks if
# node i and its parent satisfy the heap
# property, swapping and recursing if they don't
#
# L should be a heap when up_heapify is done
#

def up_heapify(L, i):

  node = L[i]
  #print "up_heapify: value %s at %s in %s" % (node, i, L)
  #print print_heap(L)

  parentIndex = parent(i)

  if parentIndex < 0: return

  parentNode = L[parentIndex]
  if node > parentNode: return

  #print "Swapping %s and %s!" % (node, parentNode)
  temp = parentNode
  L[parentIndex] = node
  L[i] = temp

  up_heapify(L, parent(i))


# if i has two children
# check heap property

# if it fails, see which child is the smaller
# and swap i's value into that child
# afterwards, recurse into that child, which might violate

def parent(i):
  return (i-1)/2
def left_child(i):
  return 2*i+1
def right_child(i):
  return 2*i+2
def is_leaf(L,i):
  return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i):
  return (left_child(i) < len(L)) and (right_child(i) >= len(L))

def print_heap(L):
  """
  0
  1 2
  3 4 5 6
  7 8 9 10 11 12 13 14
  15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
  31 ...
  63 ...
  """
  accum = ""
  powToBeat = -1
  for index, item in enumerate(L):
    log = math.log(index + 1, 2)
    if int(log) > powToBeat:
      #print accum
      accum += "\n"
      #powToBeat = int(log)
      powToBeat += 1
    else:
      pass
    #accum += " " + str(item)
    accum += " " + str(item)
  return accum


def test():
  L = [2, 4, 3, 5, 9, 7, 7]
  L.append(1)
  up_heapify(L, 7)
  print "result:", L
  print print_heap(L)
  assert 1 == L[0]
  assert 2 == L[1]

test()
