# https://stackabuse.com/linked-lists-in-detail-with-python-examples-single-linked-lists/

class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def insert_after_item(self, x, data):
        n = self.start_node
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List has no element")
            return
        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return
        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_at_index(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index - 1 and n is not None:
            n = n.ref
            i = i + 1
        if n is None:
            print("Index out of bound")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def get_count(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0
        while n is not None:
            count = count + 1
            n = n.ref
        return count

    def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("item not found")
        return False

    def make_new_list(self):
        nums = int(input("How many nodes do you want to create: "))
        if nums == 0:
            return
        for i in range(nums):
            value = int(input("Enter the value for the node:"))
            self.insert_at_end(value)

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        self.start_node = self.start_node.ref

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        # Deleting first node
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not found in the list")
        else:
            n.ref = n.ref.ref

    def reverse_linkedlist(self):
        prev = None
        n = self.start_node
        while n is not None:
            next = n.ref
            n.ref = prev
            prev = n
            n = next
        self.start_node = prev


new_linked_list = LinkedList()
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(15)
new_linked_list.traverse_list()
new_linked_list.insert_at_start(20)
new_linked_list.insert_after_item(10, 17)
new_linked_list.insert_before_item(17, 25)
new_linked_list.insert_at_index(3, 8)
new_linked_list.get_count()
new_linked_list.search_item(5)
new_linked_list.make_new_list()
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(20)
new_linked_list.delete_at_start()
new_linked_list.delete_at_end()


# второй вариант
# https://stackabuse.com/python-linked-lists/
class ListNode:
    def __init__(self, data):
        """constructor to initiate this object"""
        # store data
        self.data = data
        # store reference (next item)
        self.next = None
        return

    def has_value(self, value):
        """method to compare the value with the node data"""
        if self.data == value:
            return True
        else:
            return False


class SingleLinkedList:
    def __init__(self):
        """constructor to initiate this object"""
        self.head = None
        self.tail = None
        return

    def add_list_item(self, item):
        """add an item at the end of the list"""
        if not isinstance(item, ListNode):
            item = ListNode(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        return

    def list_length(self):
        """returns the number of list items"""
        count = 0
        current_node = self.head
        while current_node is not None:
            # increase counter by one
            count = count + 1
            # jump to the linked node
            current_node = current_node.next
        return count

    def output_list(self):
        """outputs the list (the value of the node, actually)"""
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            # jump to the linked node
            current_node = current_node.next
        return

    def unordered_search(self, value):
        """search the linked list for the node that has this value"""
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

    def remove_list_item_by_id(self, item_id):
        """remove the list item with the item id"""
        current_id = 1
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_id == item_id:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    # we don't have to look any further
                    return
            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1
        return


# create four single nodes
node1 = ListNode(15)
node2 = ListNode(8.2)
item3 = "Berlin"
node4 = ListNode(15)
track = SingleLinkedList()
print("track length: %i" % track.list_length())
for current_item in [node1, node2, item3, node4]:
    track.add_list_item(current_item)
    print("track length: %i" % track.list_length())
    track.output_list()



# третий вариант
class LinkedList:
    def __init__(self):
        self._begin = None

    def add_item(self, data):
        self._begin = [data, self._begin]

    def pop_item(self):
        if self._begin:
            data = self._begin[0]
            self._begin = self._begin[1]
            return data
        else:
            return 'Список пуст'

    def list_print(self):
        if self._begin:
            item = self._begin
            while item:
                print(item[0], end=' ')
                item = item[1]
            print()
        else:
            print('Список пуст')

    def clear(self):
        self.__init__()

    def __str__(self):
        if self._begin:
            return str(self._begin[0])
        else:
            return 'Список пуст'


if __name__ == '__main__':

    a = LinkedList()
    print(a)
    a.add_item(5)
    a.add_item(10)
    a.add_item(15)
    a.list_print()
    print(a)
    print(a.pop_item())
    print(a)
    print(a.pop_item())
    print(a.pop_item())
    print(a.pop_item())
