from classes import Node, Stack
from custom_queue import Queue
from linked_list import LinkedList


def main():
    # queue = Queue()
    # queue.enqueue('data1')
    # queue.enqueue('data2')
    # queue.enqueue('data3')
    #
    # # print(queue.head.data)
    # # print(queue.head.next_node.data)
    # # print(queue.tail.data)
    # # print(queue.tail.next_node)
    # # print(queue.tail.next_node.data)
    # print(queue.dequeue())
    # print(queue.dequeue())
    # print(queue.dequeue())
    # print(queue.dequeue())

    ll = LinkedList()
    ll.insert_beginning({'id': 1})
    ll.insert_at_end({'id': 2})
    ll.insert_at_end({'id': 3})
    ll.insert_beginning({'id': 0})
    ll.print_ll()


if __name__ == '__main__':
    main()
