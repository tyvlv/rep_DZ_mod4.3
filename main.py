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
    ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
    ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
    ll.insert_beginning({'id': 0, 'username': 'serebro'})
    #ll.print_ll()
    # ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    # ll.insert_at_end('idusername')
    # ll.insert_at_end([1, 2, 3])
    # ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

    lst = ll.to_list()
    for item in lst:
        print(item)

    user_data = ll.get_data_by_id(2)
    print(user_data)


if __name__ == '__main__':
    main()
