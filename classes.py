class Node:
    """Класс узла:
    data: данные, которые содержит узел
    next_node: ссылка на следующий узел"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс стека:
    top: ссылка на верхний узел Node в стеке"""
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        """Помещает в стек данные в виде узла Node"""
        new_node = Node(data, self.top)
        self.top = new_node
