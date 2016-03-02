class HashTable(object):
    def __init__(self, size=10):
        self.hashlist = [[] for i in range(size)]
        self.bucket_use = 0
        self.size = size

    def set(self, key, value):
        """check for value, if exists, update else add (key,value)"""
        hashed = hash(key) % self.size
        bucket_list = self.hashlist[hashed]
        if bucket_list:
            for i in bucket_list:
                if i[0] == key:
                    bucket_list.remove(i)
                    break
        bucket_list.append((key,value))

    def get(self, key):
        """key in hashed bucket, return value, if no key, return None"""
        hashed = hash(key) % self.size
        bucket_list = self.hashlist[hashed]
        if bucket_list:
            for i in bucket_list:
                if i[0] == key:
                    return i[1]
                    break
        return None

if __name__=='__main__':
    hasher = HashTable(100)
    hasher.set('four', 4)
    hasher.set('five', 5)
    hasher.set('ten', 10)
    
    print(hasher.get('four'))
    print(hasher.get('five'))
    print(hasher.get('ten'))

    hasher.set('four', 'four')
    print(hasher.get('four'))
    print(hasher.get('none') is None)
