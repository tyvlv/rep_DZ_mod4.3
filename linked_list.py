from classes import Node


class LinkedList:
    """Класс односвязанного списка:
    head: ссылка на начало (голову) списка
    tail: ссылка на конец (хвост) списка"""

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_beginning(self, data):
        """Добавляет узел Node с данными в начало односвязанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data):
        """Добавляет узел Node с данными в конец односвязанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def print_ll(self):
        """Выводит в консоль данные из односвязанного списка"""
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)
