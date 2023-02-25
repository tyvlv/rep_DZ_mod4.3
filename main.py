from classes import Node, Stack
from custom_queue import Queue


def main():
    queue = Queue()
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')

    print(queue.head.data)
    print(queue.head.next_node.data)
    print(queue.tail.data)
    print(queue.tail.next_node)
    print(queue.tail.next_node.data)


if __name__ == '__main__':
    main()
