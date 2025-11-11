class PriorityQueue:

    def __init__(self, coda=None):

        self.coda = coda if coda else []

    def enqueue(self, x, priority):

        # Inefficiente
        # O(n logn), si può fare almeno in O(n)
        self.coda.append((x, priority))
        self.coda.sort(key=lambda tup: tup[1], reverse=True)

    def dequeue(self):

        return self.coda.pop(0)

    def is_empty(self):
        return len(self.coda) == 0

    def size(self):
        return len(self.coda)


if __name__ == "__main__":

    coda = PriorityQueue([])

    coda.enqueue("a", 1)
    coda.enqueue("z", 6)
    coda.enqueue("b", 2)

    for _ in range(coda.size()):
        print(coda.dequeue())
