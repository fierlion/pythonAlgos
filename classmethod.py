class Pizza1(object):
    def __init__(self, size):
        self.size = size
    def get_size(self):
        return self.size

class Pizza2(object):
    size = 5
    def __init__(self, size):
        self.self_size = size
    @classmethod
    def get_size(self):
        return self.size
    @classmethod
    def inc_size(self):
        self.size += 1
    def get_self_size(self):
        return self.self_size
    def set_size_self(self):
        self.size = self.self_size

if __name__=='__main__':
    pizza1 = Pizza1(10)
    pizza2 = Pizza2(23)
    pizza3 = Pizza2(26)
    print(pizza1)
    print(pizza1.get_size())
    print(pizza2)
    print(pizza2.get_size())
    print(pizza2.get_self_size())
    print(pizza3.get_size())
    print(pizza3.get_self_size())
    pizza3.inc_size()
    print(pizza2.get_size())
    pizza3.set_size_self()
    print(pizza3.get_size())
