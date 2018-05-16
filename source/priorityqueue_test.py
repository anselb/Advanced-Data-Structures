#!python

from priorityqueue import PriorityQueue
import unittest


class PriorityQueueTest(unittest.TestCase):

    def test_init(self):
        pq = PriorityQueue()
        assert pq.front() is None
        assert pq.length() == 0
        assert pq.is_empty() is True

    def test_init_with_list(self):
        pq = PriorityQueue([(3, 'A'), (2, 'B'), (1, 'C')])
        assert pq.front() == (1, 'C')
        assert pq.length() == 3
        assert pq.is_empty() is False

    def test_length(self):
        pq = PriorityQueue()
        assert pq.length() == 0
        pq.enqueue('A', 1)
        assert pq.length() == 1
        pq.enqueue('B', 2)
        assert pq.length() == 2
        assert pq.dequeue() == ((1, 'A'))
        assert pq.length() == 1
        assert pq.dequeue() == ((2, 'B'))
        assert pq.length() == 0

    def test_enqueue(self):
        pq = PriorityQueue()
        pq.enqueue('A')
        assert pq.front() == 'A'
        assert pq.length() == 1
        pq.enqueue('B')
        assert pq.front() == 'A'
        assert pq.length() == 2
        pq.enqueue('C')
        assert pq.front() == 'A'
        assert pq.length() == 3
        assert pq.is_empty() is False

    def test_front(self):
        pq = PriorityQueue()
        assert pq.front() is None
        pq.enqueue('A')
        assert pq.front() == 'A'
        pq.enqueue('B')
        assert pq.front() == 'A'
        pq.dequeue()
        assert pq.front() == 'B'
        pq.dequeue()
        assert pq.front() is None

    def test_dequeue(self):
        pq = PriorityQueue(['A', 'B', 'C'])
        assert pq.dequeue() == 'A'
        assert pq.length() == 2
        assert pq.dequeue() == 'B'
        assert pq.length() == 1
        assert pq.dequeue() == 'C'
        assert pq.length() == 0
        assert pq.is_empty() is True
        with self.assertRaises(ValueError):
            pq.dequeue()


if __name__ == '__main__':
    unittest.main()
