class BinarySearchTree:
    '''Class implementing a binary search tree'''

    def __init__(self, key, datum):
        self._datum = datum
        self._key = key
        self._left = None
        self._right = None

    def get_key(self):
        return self._key

    def get_datum(self):
        return self._datum

    def left(self):
        return self._left

    def right(self):
        return self._right

    def search(self, key):
        if self._key != key and self._left == None and self._right == None:
            return False
        elif self._key == key:
            return True
        elif self._key > key:
            return self._left.search(key)
        else:
            return self._right.search(key)

    def add(self, key, datum):
        if self._left == None and self._right == None:
            if key > self._key:
                self._right = BinarySearchTree(key, datum)
            else:
                self._left = BinarySearchTree(key, datum)
        else:
            if key > self._key:
                if self._right == None:
                    self._right = BinarySearchTree(key, datum)
                else:
                    self._right.add(key, datum)
            else:
                if self._left == None:
                    self._left = BinarySearchTree(key, datum)
                else:
                    self._left.add(key, datum)
        
