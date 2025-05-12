"""
🔷 LeetCode 146 - LRU Cache (Medium)

🧠 Task:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class with the following functions:
  - __init__(capacity): Initialize the cache with positive size capacity.
  - get(key): Return the value of the key if it exists; otherwise, return -1.
  - put(key, value): Update the value of the key if it exists. Otherwise, add the key-value pair.
    When the number of keys exceeds the capacity, evict the least recently used key.

All operations should run in O(1) average time complexity.

-----------------------------------
Example:
Input:
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output:
    [null, null, null, 1, null, -1, null, -1, 3, 4]
Explanation:
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 1);       # cache is {1=1}
    lRUCache.put(2, 2);       # cache is {1=1, 2=2}
    lRUCache.get(1);          # returns 1, cache becomes {2=2, 1=1}
    lRUCache.put(3, 3);       # LRU key was 2, evict key 2, cache is {1=1, 3=3}
    lRUCache.get(2);          # returns -1 (not found)
    lRUCache.put(4, 4);       # LRU key was 1, evict key 1, cache is {3=3, 4=4}
    lRUCache.get(1);          # returns -1 (not found)
    lRUCache.get(3);          # returns 3
    lRUCache.get(4);          # returns 4

-----------------------------------
Constraints:
    - 1 <= capacity <= 3000
    - 0 <= key <= 10^4
    - 0 <= value <= 10^5
    - At most 2 * 10^5 calls will be made to get and put.
"""

# ------------------------------
# Approach 1: Using OrderedDict
# ------------------------------
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initializes the LRU cache with given capacity.

        ⏱ Time Complexity: O(1) per operation.
        💾 Space Complexity: O(capacity)
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        """
        Returns the value of the key if the key exists in the cache, else returns -1.
        Moves the key to the end to mark it as recently used.

        ⏱ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        if key not in self.cache:
            return -1
        # Move the key to denote recent use
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        """
        Adds the key-value pair to the cache or updates the value if the key exists.
        If the cache exceeds its capacity, evicts the least recently used key.

        ⏱ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        if key in self.cache:
            # Remove old value; update it later to make it most recently used.
            self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # popitem(last=False) removes the first (least recently used) item.
            self.cache.popitem(last=False)


# ------------------------------
# Approach 2: Using Doubly Linked List & Dictionary
# ------------------------------
class DLinkedNode:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCacheDL:
    def __init__(self, capacity: int):
        """
        Initializes the LRU Cache using a doubly linked list and dictionary.
        The doubly linked list maintains the order of usage (most recent at head).
        
        ⏱ Time Complexity: O(1) per get/put.
        💾 Space Complexity: O(capacity)
        """
        self.capacity = capacity
        self.cache = {}  # key -> node
        # Create dummy head and tail nodes
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node: DLinkedNode) -> None:
        """Add node right after head."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: DLinkedNode) -> None:
        """Disconnect a node from the linked list."""
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _move_to_head(self, node: DLinkedNode) -> None:
        """Move a node to the head (mark it as recently used)."""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> DLinkedNode:
        """Remove and return the node at the tail (least recently used)."""
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        """
        Returns the value of the key if present, and moves the key to the head (most recently used).
        
        ⏱ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Inserts or updates the key-value pair in the cache.
        If adding exceeds the capacity, evict the least recently used item.
        
        ⏱ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        node = self.cache.get(key)
        if not node:
            newNode = DLinkedNode(key, value)
            self.cache[key] = newNode
            self._add_node(newNode)
            if len(self.cache) > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
        else:
            node.value = value
            self._move_to_head(node)


# 🔸 Sample Test Runs
if __name__ == "__main__":
    print("Testing OrderedDict Approach:")
    lru = LRUCache(2)
    lru.put(1, 1)      # cache: {1=1}
    lru.put(2, 2)      # cache: {1=1, 2=2}
    print(lru.get(1))  # returns 1; cache: {2=2, 1=1}
    lru.put(3, 3)      # evicts key 2; cache: {1=1, 3=3}
    print(lru.get(2))  # returns -1 (not found)
    lru.put(4, 4)      # evicts key 1; cache: {3=3, 4=4}
    print(lru.get(1))  # returns -1 (not found)
    print(lru.get(3))  # returns 3
    print(lru.get(4))  # returns 4

    print("\nTesting Doubly Linked List Approach:")
    lru_dl = LRUCacheDL(2)
    lru_dl.put(1, 1)      # cache: {1=1}
    lru_dl.put(2, 2)      # cache: {1=1, 2=2}
    print(lru_dl.get(1))  # returns 1; cache: {2=2, 1=1}
    lru_dl.put(3, 3)      # evicts key 2; cache: {1=1, 3=3}
    print(lru_dl.get(2))  # returns -1 (not found)
    lru_dl.put(4, 4)      # evicts key 1; cache: {3=3, 4=4}
    print(lru_dl.get(1))  # returns -1 (not found)
    print(lru_dl.get(3))  # returns 3
    print(lru_dl.get(4))  # returns 4

# ------------------------------------------------
# ✅ OrderedDict Approach:
#      Time Complexity: O(1) per get/put.
#      Space Complexity: O(capacity).
#
# ✅ Doubly Linked List Approach:
#      Time Complexity: O(1) per get/put.
#      Space Complexity: O(capacity).
