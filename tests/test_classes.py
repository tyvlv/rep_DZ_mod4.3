import unittest

from classes import Node, Stack
from custom_queue import Queue
from linked_list import LinkedList


class TestNode(unittest.TestCase):
    """Тест класса Node"""

    def setUp(self) -> None:
        self.n1 = Node(5, None)
        self.n2 = Node('a', self.n1)

    def test_node_init(self):
        assert self.n1.data == 5
        assert self.n1.next_node is None
        assert self.n2.next_node is self.n1


class TestStack(unittest.TestCase):
    """Тест класса Stack"""

    def setUp(self) -> None:
        self.stack = Stack()
        self.stack.push('data1')
        self.stack.push('data2')
        self.stack.push('data3')

    def test_stack_push(self):
        assert self.stack.top.data == 'data3'
        assert self.stack.top.next_node.data == 'data2'
        assert self.stack.top.next_node.next_node.next_node is None

    def test_stack_pop(self):
        data = self.stack.pop()
        assert data == 'data3'
        assert self.stack.top.data == 'data2'
        assert self.stack.top.next_node.data == 'data1'
        assert self.stack.top.next_node.next_node is None


class TestQueue(unittest.TestCase):
    """Тест класса Queue"""

    def setUp(self) -> None:
        self.queue = Queue()
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')

    def test_queue_enqueue(self):
        assert self.queue.head.data == 'data1'
        assert self.queue.head.next_node.data == 'data2'
        assert self.queue.tail.data == 'data3'
        assert self.queue.tail.next_node is None

    def test_queue_dequeue(self):
        data = self.queue.dequeue()
        assert data == 'data1'
        assert self.queue.head.data == 'data2'
        assert self.queue.head.next_node.data == 'data3'
        assert self.queue.head.next_node.next_node is None
        assert self.queue.tail.data == 'data3'


class TestLinkedList(unittest.TestCase):
    """Тест класса LinkedList"""

    def setUp(self) -> None:
        self.ll = LinkedList()
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_beginning({'id': 0})
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})

    def test_linked_list_insert_beginning(self):
        assert self.ll.head.data == {'id': 0}
        assert self.ll.head.next_node.data == {'id': 1}
        assert self.ll.head.next_node.next_node.data == {'id': 2}

    def test_linked_list_insert_at_end(self):
        assert self.ll.tail.data == {'id': 3}
        assert self.ll.tail.next_node is None

    def test_print_ll(self):
        assert self.ll.print_ll() == print("{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

    def test_linked_to_list(self):
        assert self.ll.to_list() == [{'id': 0}, {'id': 1}, {'id': 2}, {'id': 3}]

    def test_get_data_by_id(self):
        assert self.ll.get_data_by_id(1) == {'id': 1}
        assert self.ll.get_data_by_id(5) == "Словарь с 'id'=5 отсутствует"
