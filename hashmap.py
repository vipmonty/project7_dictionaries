class HashMap:
    def __init__(self, size=7):
        self.table_size = size
        self.map = [None] * self.table_size
        self.num_elements = 0

    def _hash_function(self, key):
        return hash(key) % self.table_size

    def _rehash(self):
        # Double the size of the map and rehash all elements
        self.table_size *= 2
        old_map = self.map
        self.map = [None] * self.table_size
        self.num_elements = 0

        for slot in old_map:
            if slot is not None:
                for key_val_pair in slot:
                    self.put(key_val_pair[0], key_val_pair[1])

    def put(self, key, value):
        index = self._hash_function(key)
        if self.map[index] is None:
            self.map[index] = []
        for pair in self.map[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.map[index].append([key, value])
        self.num_elements += 1

        load_factor = self.num_elements / self.table_size
        if load_factor >= 0.8:
            self._rehash()

    def get(self, key):
        index = self._hash_function(key)
        if self.map[index] is not None:
            for pair in self.map[index]:
                if pair[0] == key:
                    return pair[1]
        raise KeyError("Key not found")

    def remove(self, key):
        index = self._hash_function(key)
        if self.map[index] is not None:
            for i, pair in enumerate(self.map[index]):
                if pair[0] == key:
                    del self.map[index][i]
                    self.num_elements -= 1
                    return

    # def remove(self, key):
    #     index = self._hash_function(key)
    #     if self.map[index] is not None:
    #         for i, pair in enumerate(self.map[index]):
    #             if pair[0] == key:
    #                 del self.map[index][i]
    #                 self.num_elements -= 1
    #                 return
    #     raise KeyError("Key not found")

    def keys(self):
        key_list = []
        for slot in self.map:
            if slot is not None:
                for pair in slot:
                    key_list.append(pair[0])
        return key_list

    def size(self):
        return self.num_elements

    def set(self, key, value):
        self.put(key, value)

    def clear(self):
        self.map = [None] * self.table_size
        self.num_elements = 0

    def capacity(self):
        return self.table_size


# hash_table = HashMap()
# hash_table.set('vip', 24)
# hash_table.set('kylie', 32)
# hash_table.set('Ember', 8)
# hash_table.set('Rosemary', 24)
# print(hash_table.keys())
# print(f"Example of get(): {hash_table.get('vip')}")
# print(f"Example of hash_table.get_size():{hash_table.size()}")
# print(f"test hash_table.remove('vip'){hash_table.remove('vip')}")
# print(
#     f"Keys after removal: {hash_table.keys()} and size is: {hash_table.size()}")
# print(f"Capacity before clear {hash_table.capacity()}")
# print(f"Test the clear method{hash_table.clear()}")
# print(f"present keys after clear() call{hash_table.keys()}")
# print(f"Capacity after clear {hash_table.capacity()}")


# class ChainingHashTableItem:
#     def __init__(self, itemKey, itemValue):
#         self.key = itemKey
#         self.value = itemValue
#         self.next = None


# class ChainingHashTable(HashTable):
#     def __init__(self, initialCapacity=11):
#         self.table = [None] * initialCapacity

#     # Inserts the specified key/value pair. If the key already exists, the
#     # corresponding value is updated. If inserted or updated, True is returned.
#     # If not inserted, then False is returned.
#     def insert(self, key, value):
#         # Hash the key to get the bucket index
#         bucket_index = self.hashKey(key) % len(self.table)

#         # Traverse the linked list, searching for the key. If the key exists in
#         # an item, the value is replaced. Otherwise a new item is appended.
#         item = self.table[bucket_index]
#         previous = None
#         while item != None:
#             if key == item.key:
#                 item.value = value
#                 return True

#             previous = item
#             item = item.next

#         # Append to the linked list
#         if self.table[bucket_index] == None:
#             self.table[bucket_index] = ChainingHashTableItem(key, value)
#         else:
#             previous.next = ChainingHashTableItem(key, value)
#         return True

#     # Searches for the specified key. If found, the key/value pair is removed
#     # from the hash table and True is returned. If not found, False is returned.
#     def remove(self, key):
#         # Hash the key to get the bucket index
#         bucket_index = self.hashKey(key) % len(self.table)

#         # Search the bucket's linked list for the key
#         item = self.table[bucket_index]
#         previous = None
#         while item != None:
#             if key == item.key:
#                 if previous == None:
#                     # Remove linked list's first item
#                     self.table[bucket_index] = item.next
#                 else:
#                     previous.next = item.next
#                 return True
#             previous = item
#             item = item.next
#         return False  # key not found

#     # Searches for the key, returning the corresponding value if found, None if
#     # not found.
#     def search(self, key):
#         # Hash the key to get the bucket index
#         bucket_index = self.hashKey(key) % len(self.table)

#         # Search the bucket's linked list for the key
#         item = self.table[bucket_index]
#         while item != None:
#             if key == item.key:
#                 return item.value
#             item = item.next
#         return None  # key not found


# # OpenAddressingBucket represents a bucket with a key and a value
# class OpenAddressingBucket:
#     def __init__(self, bucket_key=None, bucket_value=None):
#         self.key = bucket_key
#         self.value = bucket_value

#     def isEmpty(self):
#         if self is OpenAddressingBucket.EMPTY_SINCE_START:
#             return True
#         return self is OpenAddressingBucket.EMPTY_AFTER_REMOVAL


# # Initialize two special bucket types: empty-since-start and empty-after-removal
# OpenAddressingBucket.EMPTY_SINCE_START = OpenAddressingBucket()
# OpenAddressingBucket.EMPTY_AFTER_REMOVAL = OpenAddressingBucket()
