from classes import Node


class Queue:
    """Класс очереди:
    head: ссылка на начало (голову) очереди
    tail: ссылка на конец (хвост) очереди"""
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        """Помещает в очередь данные в виде узла Node"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node

    def dequeue(self):
        """Удаляет из очереди первый добавленный узел Node и возвращает его данные"""
        if self.head is None:
            return None
        del_node = self.head
        self.head = self.head.next_node
        return del_node.data
