import unittest

from classes import Node, Stack


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
