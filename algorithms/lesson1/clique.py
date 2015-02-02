import unittest

def clique(n):
    print "in a clique..."
    for j in range(n):
        for i in range(j):
            print i, "is friends with", j

def count(n):
    # Your code here to count the units of time
    # it takes to execute clique
    intro = 1
    edges = (n * (n-1)) / 2
    jRange = 1
    iRange = n
    return edges + intro + jRange + iRange

    n + 2
    (n * (n-1)) / 2


    n^2/2 - n/2

def triangular_recursive(n):
    if n == 1: return 1
    return triangular_recursive(n-1) + n

def triangular(n):
    return (n * (n+1)) / 2

def clique(n):
    print "in a clique..."
    for j in range(n):
        for i in range(j):
            print i, "is friends with", j


# clique(4)

class TestSequenceFunctions(unittest.TestCase):
    def test_choice(self):
        self.assertEqual(count(4), 12)
        self.assertEqual(count(5), 17)

    def test_triangular(self):
        self.assertEqual(triangular(1), 1)
        self.assertEqual(triangular(2), 3)
        self.assertEqual(triangular(3), 6)
        self.assertEqual(triangular(4), 10)
        self.assertEqual(triangular(5), 15)
        self.assertEqual(triangular(6), 21)
        self.assertEqual(triangular(7), 28)
        self.assertEqual(triangular(8), 36)
        self.assertEqual(triangular(9), 45)
        self.assertEqual(triangular(10), 55)

if __name__ == '__main__':
    unittest.main()

# count(4)
# 6 + intro + jRange + iRange
# 6 + 1 + 1 + 4

# count(5)
# 12 + 1 + 1 + 5?
