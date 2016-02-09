import random
class TestClass(object):
    def __init__(self, data=""):
        self.data = data

test_arr = [TestClass(x) for x in xrange(10)]
random.shuffle(test_arr)
test_results = [x.data for x in test_arr]
rand_tup = tuple(test_arr)
print test_results
list.sort(test_arr, key=lambda x: x.data)

test_results = [x.data for x in test_arr]
print test_results

sorted_tup = sorted(rand_tup, key=lambda x: x.data)
print [x.data for x in rand_tup]
print [x.data for x in sorted_tup]
