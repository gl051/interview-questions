from datastructures import LinkedList
import random

class LinkedListSorted(LinkedList):
    def sort(self):
        """
            This implementaion use bubble sort and switch only values,
            I am aware that complexity worst case will be O(N^2)
        """
        had_switched = True
        first_node = self.head
        second_node = first_node.next
        # if we have only one node, nothing to sort
        if second_node is None:
            return
        while had_switched:
            had_switched = False
            while first_node.next is not None:
                if first_node.value > second_node.value:
                    first_node.value, second_node.value = second_node.value, first_node.value
                    had_switched = True
                first_node = second_node
                second_node = second_node.next
            # Rewind to the beginning
            first_node = self.head
            second_node = first_node.next

    def sort2(self):
        if self.head is None or self.head.next is None:
            return
        else:
            return self._sort2(self.head, None)

    def _sort2(self, first_node, last_node):
        # If we have only one element return that
        if first_node.next is None:
            return first_node
        # Get the length of the list
        node = first_node
        len_list = 0
        while node is not last_node:
            len_list = len_list + 1
            node = node.next
        # Get the middle pos, indexing starts at zero
        middle = len_list / 2
        second_half = first_node
        for i in range (0, middle):
            second_half = second_half.next
        # Call the sort for the sub-array first, middle
        list_a = self._sort2(first_node, second_half)
        # Call the sort for the sub-array middle, last
        list_b = self._sort2(second_half, last_node)
        # Merge the two ordered sublist
        return self._merge(list_a, list_b, last_node)

    def _merge(self, nodeA, nodeB, nodeStop):
        """
            Merge in place two sub-parts of the a list already sorted.
            1st sublist: [nodeA, nodeB[
            2nd sublist: [nodeB, nodeStop[
        """
        if nodeB is None:
            return
        # use two pointer to the nodes
        posA = nodeA
        posB = nodeB
        # temp list to merge the values
        lval = []
        bMerge = True
        while bMerge:
            if posA.value <= posB.value:
                lval.append(posA.value)
                posA = posA.next
                # Stop when we end list A, reaching nodeB
                if posA == nodeB:
                    while posB is not nodeStop:
                        lval.append(posB.value)
                        posB = posB.next
                    bMerge = False
            else:
                lval.append(posB.value)
                posB = posB.next
                # stop when we reached the node stop
                if posB == nodeStop:
                    while posA != nodeB:
                        lval.append(posA.value)
                        posA = posA.next
                    bMerge = False
        # repass the list from nodeA to nodeStop to reassing
        # the ordered value from teh tmp list
        node = nodeA
        while node is not nodeStop:
            node.value = int(lval.pop(0))
            node = node.next
        # very important, return the first node to innest recursio
        return nodeA

    # Accessory method
    def printall(self, node):
        while node is not None:
            print ' ', node.value,
            node = node.next
        print ''




ll = LinkedListSorted()
for i in range(1,9):
    ll.insert(random.randint(1,100))
print ll
#merge_inplace(ll.head, ll.head.next.next)
ll.sort2()
print ll
