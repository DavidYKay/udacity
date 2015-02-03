import unittest

# Write partition to return a new array with
# all values less then `v` to the left
# and all values greater then `v` to the right
#

def partition(L, v):
    less = []
    more = []
    for i in L:
        if i > v:
            more.append(i)
        elif i < v:
            less.append(i)

    P = less + [v] + more
    # your code here
    return P

def rank(L, v):
    pos = 0
    for val in L:
        if val < v:
            pos += 1
    return pos


class TestSequenceFunctions(unittest.TestCase):
  def test_choice(self):
    before = [3,1,2,4,5]
    after = partition(before, 3)

    self.assertEqual(after, [])

if __name__ == '__main__':
  unittest.main()
