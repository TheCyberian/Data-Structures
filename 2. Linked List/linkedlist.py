#!/usr/bin/env python

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def insert_after(self, after, data):
        if not after:
            print("node not found...")
            return

        new_node = Node(data)
        new_node.next = after.next
        after.next = new_node


    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def delete_node(self, node):
        cur_node = self.head
        # if node == self.head.data:
        #     self.head = self.head.next
        #     return
        if cur_node and cur_node.data == node:
            self.head = cur_node.next
            cur_node = None
            return

        prev_node = None
        while cur_node and cur_node.data != node:
            prev_node = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev_node.next = cur_node.next
        cur_node = None
        return

    def delete_node_position(self, position):
        cur_node = self.head
        if position == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev_node = None
        count = 0

        while cur_node and count != position:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1
            # if position == count:
            #     prev_node.next = cur_node.next
            #     cur_node = None
            #     return
        if cur_node is None:
            return

        prev_node.next = cur_node.next
        cur_node = None



l = LinkedList()
l.append("A")
l.append("b")
l.prepend("E")
l.insert_after(l.head, "D")
l.print_list()
l.delete_node("E")
l.delete_node("A")
l.print_list()
