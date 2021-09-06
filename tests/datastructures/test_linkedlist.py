import unittest
from unittest import result
from datastructures.linkedlist import (
    Node,
    LinkedList
)
import random


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.sample_list = random.sample(range(1000), 10)
        self.sample_linkedlist = LinkedList(list=self.sample_list)
        self.empty_linkedlist = LinkedList()
        
    def test_len(self):
        result_sample = len(self.sample_linkedlist)
        result_empty = len(self.empty_linkedlist)
        self.assertEqual(result_sample, len(self.sample_list))
        self.assertEqual(result_empty, 0)
    
    def test_push(self):
        rand = random.randint(0, 1000)
        
        self.sample_linkedlist.push(rand)
        self.sample_list.insert(0, rand)
        self.assertListEqual(list(self.sample_linkedlist), self.sample_list)
        self.assertEqual(len(self.sample_linkedlist), len(self.sample_list))

        self.empty_linkedlist.push(rand)
        self.assertListEqual(list(self.empty_linkedlist), [rand])
        self.assertEqual(len(self.empty_linkedlist), 1)

    def test_insert_after(self):
        node = self.sample_linkedlist.find_index(2)
        rand = random.randint(-1000, 0)
        self.sample_linkedlist.insert_after(node, rand)
        self.sample_list.insert(3, rand)
        self.assertListEqual(list(self.sample_linkedlist), self.sample_list)

        with self.assertRaises(RuntimeError):
            new_node = Node(-2000)
            self.sample_linkedlist.insert_after(new_node, -3000)
            self.empty_linkedlist.insert_after(new_node, -3000)
            self.empty_linkedlist.insert_after(None, -3000)
        

    def test_insert_index(self):
        rand = random.randint(-1000, 0)
        self.sample_linkedlist.insert_index(2, rand)
        self.sample_list.insert(2, rand)
        self.assertListEqual(list(self.sample_linkedlist), self.sample_list)

        with self.assertRaises(ValueError):
            self.sample_linkedlist.insert_index(-1, -2000)
            self.sample_linkedlist.insert_index(len(self.sample_linkedlist), -2000)
            self.sample_linkedlist.insert_index(len(self.sample_linkedlist) + 1, -2000)
            self.empty_linkedlist.insert_index(0, -2000)
            self.empty_linkedlist.insert_index(1, -2000)

    def test_append(self):
        rand = random.randint(0, 1000)
        
        self.sample_linkedlist.append(rand)
        self.sample_list.append(rand)
        self.assertListEqual(list(self.sample_linkedlist), self.sample_list)
        self.assertEqual(len(self.sample_linkedlist), len(self.sample_list))

        self.empty_linkedlist.append(rand)
        self.assertListEqual(list(self.empty_linkedlist), [rand])
        self.assertEqual(len(self.empty_linkedlist), 1)

    def test_fast_append(self):
        rand = random.randint(0, 1000)
        
        self.sample_linkedlist.append(rand)
        self.sample_list.append(rand)
        self.assertListEqual(list(self.sample_linkedlist), self.sample_list)
        self.assertEqual(len(self.sample_linkedlist), len(self.sample_list))

        self.empty_linkedlist.append(rand)
        self.assertListEqual(list(self.empty_linkedlist), [rand])
        self.assertEqual(len(self.empty_linkedlist), 1)

    def test_peek(self):
        result_sample = self.sample_linkedlist.peek()
        result_empty = self.empty_linkedlist.peek()
        self.assertEqual(result_sample, self.sample_list[0])
        self.assertIsNone(result_empty)

    def test_peek_last(self):
        result_sample = self.sample_linkedlist.peek_last()
        result_empty = self.empty_linkedlist.peek_last()
        self.assertEqual(result_sample, self.sample_list[len(self.sample_list) - 1])
        self.assertIsNone(result_empty)
    
    def test_remove_first(self):
        with self.assertRaises(RuntimeError):
            self.empty_linkedlist.remove_first()

        result = self.sample_linkedlist.remove_first()
        self.assertEqual(result, self.sample_list[0])
        self.sample_list.pop(0)
        self.assertEqual(len(self.sample_linkedlist), len(self.sample_list))
        self.assertListEqual(list(self.sample_linkedlist), self.sample_list)

    def test_remove_last(self):
        with self.assertRaises(RuntimeError):
            self.empty_linkedlist.remove_last()

        result = self.sample_linkedlist.remove_last()
        self.assertEqual(result, self.sample_list[len(self.sample_list) - 1])
        self.sample_list.pop(len(self.sample_list) - 1)
        self.assertEqual(len(self.sample_linkedlist), len(self.sample_list))
        self.assertListEqual(list(self.sample_linkedlist), self.sample_list)

    def test_remove(self):
        for i in range(3):
            result = self.sample_linkedlist.remove(self.sample_list[2])
            self.assertEqual(result, self.sample_list[2])
            self.sample_list.pop(2)
            self.assertListEqual(list(self.sample_linkedlist), self.sample_list)

        result = self.sample_linkedlist.remove(self.sample_list[0])
        self.assertEqual(result, self.sample_list[0])
        self.sample_list.pop(0)
        self.assertListEqual(list(self.sample_linkedlist), self.sample_list)

        result = self.sample_linkedlist.remove(self.sample_list[len(self.sample_list) - 1])
        self.assertEqual(result, self.sample_list[len(self.sample_list) - 1])
        self.sample_list.pop(len(self.sample_list) - 1)
        self.assertListEqual(list(self.sample_linkedlist), self.sample_list)

        with self.assertRaises(RuntimeError):
            self.sample_linkedlist.remove(-1)
            self.empty_linkedlist.remove(-1)

    def test_remove_index(self):
        for i in range(1):
            result = self.sample_linkedlist.remove_index(2)
            self.assertEqual(result, self.sample_list[2])
            self.sample_list.pop(2)
            self.assertListEqual(list(self.sample_linkedlist), self.sample_list)

        result = self.sample_linkedlist.remove_index(0)
        self.assertEqual(result, self.sample_list[0])
        self.sample_list.pop(0)
        self.assertListEqual(list(self.sample_linkedlist), self.sample_list)

        result = self.sample_linkedlist.remove_index(len(self.sample_list) - 1)
        self.assertEqual(result, self.sample_list[len(self.sample_list) - 1])
        self.sample_list.pop(len(self.sample_list) - 1)
        self.assertListEqual(list(self.sample_linkedlist), self.sample_list)

        with self.assertRaises(ValueError):
            self.sample_linkedlist.remove_index(-1)
            self.empty_linkedlist.remove_index(-1)
            self.empty_linkedlist.remove_index(0)
            self.empty_linkedlist.remove_index(1)
            self.sample_linkedlist.remove_index(len(self.sample_linkedlist))
            self.sample_linkedlist.remove_index(len(self.sample_linkedlist) + 1)

    def test_find(self):
        rand = random.randint(-1000, 0)
        self.assertIsNone(self.sample_linkedlist.find(rand))
        self.assertIsNone(self.empty_linkedlist.find(rand))

        for index, element in enumerate(self.sample_list):
            result_index, result_element = self.sample_linkedlist.find(element, True)
            self.assertEqual(result_index, index)
            self.assertEqual(result_element.data, element)

    def test_find_index(self):
        with self.assertRaises(ValueError):
            self.sample_linkedlist.find_index(len(self.sample_linkedlist))
            self.sample_linkedlist.find_index(len(self.sample_linkedlist) + 1)
            self.sample_linkedlist.find_index(-1)
            self.empty_linkedlist.find_index(0)
            self.empty_linkedlist.find_index(1)
        
        for index in range(len(self.sample_list)):
            self.assertEqual(self.sample_linkedlist.find_index(index).data, self.sample_list[index])

    def test_distance(self):
        start, end = self.sample_linkedlist.find(self.sample_list[1]),\
             self.sample_linkedlist.find(self.sample_list[2])
        self.assertEqual(self.sample_linkedlist.distance(start, end), 1)

        start, end = self.sample_linkedlist.find(self.sample_list[2]),\
             self.sample_linkedlist.find(self.sample_list[5])
        self.assertEqual(self.sample_linkedlist.distance(start, end), 3)

        with self.assertRaises(RuntimeError):
            start = self.sample_linkedlist.find(self.sample_list[1])
            node = Node(-1)
            self.assertRaises(self.sample_linkedlist.distance(start, node))

    def test_has_loop(self):
        self.assertFalse(self.sample_linkedlist.has_loop())
        self.assertFalse(self.empty_linkedlist.has_loop())
        
        loop_linkedlist = LinkedList([1, 2, 3, 4])
        new_node = Node(5)
        new_node.next = loop_linkedlist.find(3)
        loop_linkedlist.find(4).next = new_node

        result, distance = loop_linkedlist.has_loop(False)
        self.assertTrue(result)
        self.assertEqual(distance, 3)

    def test_reverse(self):
        self.empty_linkedlist.reverse()
        self.sample_linkedlist.reverse()
        self.sample_list.reverse()
        
        self.assertListEqual(list(self.sample_linkedlist), self.sample_list)
        self.assertListEqual(list(self.empty_linkedlist), [])

    def test_iteration(self):
        for index, element in enumerate(self.sample_linkedlist):
            self.assertEqual(element, self.sample_list[index])

        iterator = iter(self.sample_linkedlist)
        for i in range(len(self.sample_linkedlist)):
            next(iterator)
        self.assertRaises(StopIteration, next, iterator)

        iterator_empty = iter(self.empty_linkedlist)
        self.assertRaises(StopIteration, next, iterator_empty)

