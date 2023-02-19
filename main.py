from classes import Node, Stack


def main():
    stack = Stack()
    stack.push('data1')
    data = stack.pop()

    # стек стал пустой
    print(stack.top)
    # pop() удаляет элемент и возвращает данные удаленного элемента
    print(data)
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    data = stack.pop()

    # теперь последний элемента содержит данные data1
    print(stack.top.data)

    # данные удаленного элемента
    print(data)


if __name__ == '__main__':
    main()
