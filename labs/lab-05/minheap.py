class MinHeap:
    def __init__(self, data=None):
        if data is None:
            self.heap = []
        else:
            self.heap = data.copy()
            self.make_heap()

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def push(self, data):
        self.heap.append(data)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.is_empty():
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return minimum

    def min(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def make_heap(self):
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index],
                )
                index = parent
            else:
                break

    def _heapify_down(self, index):
        size = len(self.heap)

        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[index],
                )
                index = smallest
            else:
                break
#Test
h = MinHeap([5, 8, 3, 10, 1, 7])

print(h.min())
print(h.pop())
print(h.min())