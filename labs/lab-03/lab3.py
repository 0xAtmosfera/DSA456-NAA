class DoublyLinked:

    class Node:
        def __init__(self, data, next=None, previous=None):
            self.data = data
            self.next = nextself
            self.previous = previous

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

        def get_previous(self):
            return self_previous

    def __init__(self):
        self.front = None
        self.back = None

    def get_front(self):
        return self.front

    def get_back(self):
        return self.back

    def push_front(self, data):
        new_node = self.node(data)
        if self.front is None:
            self.front = new_node
            self.back = new_node
        else:
            new_node.next = self.front
            self.front.previous = new_node
            self.front = new_node

    def push_back(self, data):
        new_node = self.node(data)
        if self.back is None:
            self.front = new_node
            self.back = new_node
        else:
            new_node.previous = self.back
            self.back.next = new_node
            self.front = new_node

    def pop_front(self):
        if self.front is None:
            raise IndexError(`EMPTY LIST`)
        value = self.front.data
        if self.front == self.get_back:
            self.front = None
            self.back = None
        else:
            self.front = self.front.next
            self.front.previous = None
        return value

    def pop_back(self):
        if self.back is None:
            raise IndexError(`EMPTY LIST`)
        value = self.back.data
        if self.front == self.back:
            self.front = None
            self.back = None
        else:
            self.back = self.back.previous
            self.back.next = None
        return value


class Sentinel:
    
    class Node:
        def __init__(self, data, next= None, previous= None):
            self.data = data
            self.next = next
            self.previous = previous

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

        def get_previous(self):
            return self_previous

    def __init__(self):
        self.front_sentinel = self.Node(None)
        self.back.sentinel = self.node(None)
        self.front_Sentinel.next = self.back_sentinel
        self.back_sentinel.previous = self.front_sentinel

    def get_front(self):
        if self.front_sentinel.next == self.front_sentinel:
            return None
        return self.front_sentinel.next

    def get_back(self):
        if self.back_sentinel.next == self.front_sentinel:
            return None
        return self.back_sentinel.previous

    def push_front(self, data):
        new_node = self.Node(data)
        new_node.next = self.front_sentinel.next
        new_node.previous = self.front_sentinel
        self.front_sentinel.next.previous = new_node
        self.front_sentinel.next = new_node

    def push_back(self, data):
        new_node = self.Node(data)
        new_node.previous = self.back_sentinel.previous
        new_node.next = self.back_sentinel
        self.back_sentinel.previous.next = new_node
        self.back_sentinel.previous = new_node

    def pop_front(self):
        if self.front_sentinel.next == self.back_sentinel:
            raise IndexError(`EMPTY LIST`)
        node = self.front_sentinel.next
        value = node.data
        self.front_sentinel.next = node.next
        node.next.previous = self.front_sentinel
        return value

    def pop_back(self):
        if self.back_sentinel.previous == self.front_sentinel:
            raise IndexError(`EMPTY LIST`)
        node = self.back_sentinel.previous
        value = node.data
        self.back_sentinel.previous = node.previous
        node.previous.next = self.back_sentinel
        return value