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
        pq = PriorityQueue([(1, 'A'), (2, 'B'), (3, 'C')])
        assert pq.front() == (1, 'A')
        assert pq.length() == 3
        assert pq.is_empty() is False

    def test_length(self):
        pq = PriorityQueue()
        assert pq.length() == 0
        pq.enqueue('A', 1)
        assert pq.length() == 1
        pq.enqueue('B', 2)
        assert pq.length() == 2
        assert pq.dequeue() == (1, 'A')
        assert pq.length() == 1
        assert pq.dequeue() == (2, 'B')
        assert pq.length() == 0

    def test_enqueue(self):
        pq = PriorityQueue()
        pq.enqueue('B', 2)
        assert pq.front() == (2, 'B')
        assert pq.length() == 1
        pq.enqueue('A', 1)
        assert pq.front() == (1, 'A')
        assert pq.length() == 2
        pq.enqueue('C', 3)
        assert pq.front() == (1, 'A')
        assert pq.length() == 3
        assert pq.is_empty() is False

    def test_front(self):
        pq = PriorityQueue()
        assert pq.front() is None
        pq.enqueue('A', 1)
        assert pq.front() == (1, 'A')
        pq.enqueue('B', 2)
        assert pq.front() == (1, 'A')
        pq.dequeue()
        assert pq.front() == (2, 'B')
        pq.dequeue()
        assert pq.front() is None

    def test_dequeue(self):
        pq = PriorityQueue([(1, 'A'), (2, 'B'), (3, 'C')])
        assert pq.dequeue() == (1, 'A')
        assert pq.length() == 2
        assert pq.dequeue() == (2, 'B')
        assert pq.length() == 1
        assert pq.dequeue() == (3, 'C')
        assert pq.length() == 0
        assert pq.is_empty() is True
        with self.assertRaises(ValueError):
            pq.dequeue()


if __name__ == '__main__':
    unittest.main()
