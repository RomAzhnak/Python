# https://stackabuse.com/python-linked-lists/

class ListNode:
    def __init__(self, data):
        "constructor class to initiate this object"
        # store data
        self.data = data
        # store reference (next item)
        self.next = None
        # store reference (previous item)
        self.previous = None
        return

    def has_value(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False


class DoubleLinkedList:
    def __init__(self):
        "constructor to initiate this object"
        self.head = None
        self.tail = None
        return

    def list_length(self):
        "returns the number of list items"
        count = 0
        current_node = self.head
        while current_node is not None:
            # increase counter by one
            count = count + 1

            # jump to the linked node
            current_node = current_node.next
        return count

    def output_list(self):
        "outputs the list (the value of the node, actually)"
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            # jump to the linked node
            current_node = current_node.next
        return

    def unordered_search(self, value):
        "search the linked list for the node that has this value"
        # define current_node
        current_node = self.head
        # define position
        node_id = 1
        # define list of results
        results = []
        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
            # jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1
        return results

    def add_list_item(self, item):
        "add an item at the end of the list"
        if isinstance(item, ListNode):
            if self.head is None:
                self.head = item
                item.previous = None
                item.next = None
                self.tail = item
            else:
                self.tail.next = item
                item.previous = self.tail
                self.tail = item
        return

    def remove_list_item_by_id(self, item_id):
        "remove the list item with the item id"
        current_id = 1
        current_node = self.head
        while current_node is not None:
            previous_node = current_node.previous
            next_node = current_node.next
            if current_id == item_id:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = next_node
                    if next_node is not None:
                        next_node.previous = previous_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.previous = None
                # we don't have to look any further
                return
            # needed for the next iteration
            current_node = next_node
            current_id = current_id + 1
        return


# create three single nodes
node1 = ListNode(15)
node2 = ListNode(8.2)
node3 = ListNode("Berlin")
node4 = ListNode(15)
track = DoubleLinkedList()
print("track length: %i" % track.list_length())
for current_node in [node1, node2, node3, node4]:
    track.add_list_item(current_node)
    print("track length: %i" % track.list_length())
    track.output_list()
results = track.unordered_search(15)
print(results)
track.remove_list_item_by_id(4)
track.output_list()


# Creating Double-Linked Lists with deque
from collections import deque


class ListNode:
    def __init__(self, data):
        "constructor class to initiate this object"
        # store data
        self.data = data
        return


node1 = ListNode(15)
node2 = ListNode(8.2)
node3 = ListNode("Berlin")
track = deque([node1, node2, node3])
print("three items (initial list):")
for item in track:
    print(item.data)
# add an item at the beginning
node4 = ListNode(15)
track.append_left(node4)
print("four items (added as the head):")
for item in track:
    print(item.data)
# add an item at the end
node5 = ListNode("Moscow")
print("five items (added at the end):")
track.append(node5)
for item in track:
    print(item.data)


# второй вариант
# https://www.laurentluce.com/posts/least-frequently-used-cache-eviction-scheme-with-complexity-o1-in-python/
class Node(object):
    """Node containing data, pointers to previous and next node."""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        # Number of nodes in list.
        self.count = 0

    def add_node(self, cls, data):
        """Add node instance of class cls."""
        return self.insert_node(cls, data, self.tail, None)

    def insert_node(self, cls, data, prev, next):
        """Insert node instance of class cls."""
        node = cls(data)
        node.prev = prev
        node.next = next
        if prev:
            prev.next = node
        if next:
            next.prev = node
        if not self.head or next is self.head:
            self.head = node
        if not self.tail or prev is self.tail:
            self.tail = node
        self.count += 1
        return node

    def remove_node(self, node):
        if node is self.tail:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        else:
            node.prev.next = node.next
        self.count -= 1

    def get_nodes_data(self):
        """Return list nodes data as a list."""
        data = []
        node = self.head
        while node:
            data.append(node.data)
            node = node.next
        return data
