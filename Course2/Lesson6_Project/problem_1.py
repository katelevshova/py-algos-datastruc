"""
TASK1:
For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache.
An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory
reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

    In case of a cache hit, your get() operation should return the appropriate value.
    In case of a cache miss, your get() should return -1.
    While putting an element in the cache, your put() / set() operation must insert the element.
    If the cache is full, you must write code that removes the least recently used entry first
    and then insert the element.

All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.
"""
from collections import OrderedDict


class LRU_Cache(object):

    def __init__(self, size: int):
        # Initialize class variables
        self.cache = OrderedDict()
        self.size = size
        pass

    '''
    Returns the value of the key in O(1) and returns -1 if the key does not exist in the cache.
    Also moves he key to the end to show that it was recently used.
    ARGS:
        self (LRU_Cache) - is a reference to the current instance of the class.
        key (int) - unique key
    '''

    def get(self, key: int) -> int:
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
        pass

    '''
    Adds or updates the value by key.
    Moves the key to the end to show that it was recently used.
    Checks if the size of ordered dictionary is reached. If yes - removes the first key which is least recently used.
    '''

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key is None or value is None:
            return

        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)  # FIFO order if false.
        pass


# TEST CASES: start----------------------------------------------
our_cache = LRU_Cache(5)

print("TEST ADD VALUES --------------------------------------------------")
our_cache.set(1, 1);
print("->set: our_cache.cache={}".format(our_cache.cache))
assert len(our_cache.cache.items()) == 1
assert our_cache.cache[1] == 1

our_cache.set(2, 2);
print("->set: our_cache.cache={}".format(our_cache.cache))
assert len(our_cache.cache.items()) == 2
assert our_cache.cache[2] == 2

our_cache.set(3, 3);
print("->set: our_cache.cache={}".format(our_cache.cache))
assert len(our_cache.cache.items()) == 3
assert our_cache.cache[3] == 3

our_cache.set(4, 4);
print("->set: our_cache.cache={}".format(our_cache.cache))
assert len(our_cache.cache.items()) == 4
assert our_cache.cache[4] == 4

print("TEST GET VALUES --------------------------------------------------")
our_cache.get(1)  # returns 1
print("->get: our_cache.get(1)={}".format(our_cache.get(1)))
assert our_cache.get(1) == 1
print("our_cache.cache={}".format(our_cache.cache))

our_cache.get(2)  # returns 2
print("->get: our_cache.get(2)={}".format(our_cache.get(2)))
assert our_cache.get(2) == 2
print("our_cache.cache={}".format(our_cache.cache))

our_cache.get(9)  # returns -1 because 9 is not present in the cache
assert our_cache.get(9) == -1

print("TEST REACH CAPACITY --------------------------------------------------")
our_cache.set(5, 5)
print("->set: our_cache.cache={}".format(our_cache.cache))
assert len(our_cache.cache.items()) == 5

our_cache.set(6, 6)  # after this 3 must be deleted
print("->set: our_cache.cache={}".format(our_cache.cache))
assert len(our_cache.cache.items()) == 5, "Size must be equal 5, actual={}".format(len(our_cache.cache.items()))

our_cache.get(3)  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
assert our_cache.get(3) == -1

print("TEST CACHE MISS --------------------------------------------------")
our_cache.set(None, None)
assert our_cache.get(None) == -1
print("->set: our_cache.cache={}".format(our_cache.cache))
# TEST CASES: end----------------------------------------------------------
