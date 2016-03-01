from collections import Container

class Heap(Container):
    array = []

    def __contains__(self, item):
        return self._contains(item, 1)

    def _contains(self, item, index):
        if item > self.array[index-1]:
            return False
        elif item < self.array[index-1]:
            if len(self.array) > index * 2:
                return self._contains(item, index*2) or self.contains(item, index*2+1)
            elif len(self.array) > index * 2 + 1:
                return self._contains(item, index*2)
            else:
                return False
        else:
            return True

    def _bubble(self, index):
        index = index-1
        if self.array[index] > self.array[index//2]:
            tmp = self.array[index]
            self.array[index] = self.array[index//2]
            self.array[index] = tmp
            self._bubble(index//2)

    def add(self, item):
        self.array.append(item)
        self._bubble(len(self.array)-1)

if __name__=='__main__':
    heap_a = Heap()
    for i in [23,1,45,22,56]:
        heap_a.add(i)
    print(heap_a.array)
