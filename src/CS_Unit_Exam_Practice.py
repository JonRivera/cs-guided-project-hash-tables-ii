"""General"""


def countVowelConsonant(s):
    # want two filter out the characters that are vowel and consontant and
    # keep track of them by adding a 1 or 2 two some variables in the for foor lop
    vowels = ['a', 'e', 'i', 'o', 'u']
    one = 0
    two = 0
    for x in s:
        if x in vowels:
            one += 1
        else:
            two += 2
    return one + two


# Data Structure: List
# Two pointer approach


def digitsManipulations(n):
    # we want the difference btw the product of digits and the sum of digits
    # like other problems requiring us to work witht the digits in the number
    # we need to split the number into its digits

    # perform a for loop and keep track of product and sum
    # product can start as 1
    # sum will start at 0
    list = [int(x) for x in str(n)]
    print(list)
    product = 1
    sum = 0
    for x in list:
        sum += x
        product = product * x
    return product - sum


# DT: list to to save #rs,
# SY: convert # to string and use a list comprehension to manipulate it


"""LINKED LIST PROBLEMS"""

"""S2-M1"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# given two sorted linked lists
# want
# merge two linked lists, in sorted fashion
# plan
# check head of node to see which node has the bigger node
# iterate over

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # a dummy first node to hang the result on
        dummy = ListNode(0)

        # tail points to the last result node
        tail = dummy

        while l1 is not None and l2 is not None:
            # Compare the data of the two
            # lists whichever lists' data is
            # smaller, append it into tail and
            # advance the head to the next Node
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next;

            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next;

            # inlcuding remaining nodes
        if l1 is None:
            tail.next = l2
        if l2 is None:
            tail.next = l1

        return dummy.next


LK1 = None
LK2 = ListNode(0)
Sol = Solution()
print(Sol.mergeTwoLists(LK1, LK2))


# DT: Linked List
# SY: Dummy Node, save the next value for a given linked list, depending on who was lower to dummy Node
# The dummy node serves as a pointer that is saving things in order
# Return dummy.next which is the ordered-merged linked list


# SORT grom smallest to greatest"""
def sortList(self, head: ListNode) -> ListNode:
    # append the given values inside a list then sort that list and make
    # a new linked list with the help of sorted list and return the head

    if not head:
        return

    l = []
    while head is not None:
        l.append(head.val)
        head = head.next

    l.sort()
    nxt = None
    i = 1

    while l:
        val = l.pop()
        node = ListNode(val)
        node.next = nxt
        nxt = node

    return node


# other sol (harder to understand)
# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#
#         p, slow, fast = None, head, head
#         while fast and fast.next:
#             p = slow
#             slow = slow.next
#             fast = fast.next.next
#         p.next = None
#
#         return self.merge(self.sortList(head), self.sortList(slow))
#
#     def merge(self, l1, l2):
#         dummy = ListNode(None)
#         curr = dummy
#
#         while l1 and l2:
#             if l1.val > l2.val:
#                 curr.next, l2 = l2, l2.next
#             else:
#                 curr.next, l1 = l1, l1.next
#             curr = curr.next
#
#         if l1:
#             curr.next = l1
#         elif l2:
#             curr.next = l2
#
#         return dummy.next


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
# Given a sorted singly linked list and a data, your task is to insert
# the data in the linked list in a sorted way i.e. order of the list doesn't change.

def insertValueIntoSortedLinkedList(l, value):
    new_node = ListNode(value)

    if l is None or l.value >= value:
        # if new node is needed at the start of list
        new_node.next = l
        return new_node

    current = l

    while (current.next is not None) and current.next.value < value:
        current = current.next;
        # traversing over the internal nodes
        # finding a node which has lesser value than new_node
        # but its successor should have greater (or equal) value

    # inserting new_node after current node
    # everything else following current save it into new_node.next
    # => the new_node pointer, points at the  current.next
    new_node.next = current.next;

    # the current.next(in L) now points at the new node
    current.next = new_node;
    # Notice that we aren't returning current but rather were returning l(inside of l current exists)
    return l


# """
# Given a reference to the head node of a singly-linked list, write a function
# that reverses the linked list in place. The function should return the new head
# of the reversed list.
#
# In order to do this in O(1) space (in-place), you cannot make a new list, you
# need to use the existing nodes.
#
# In order to do this in O(n) time, you should only have to traverse the list
# once.
#
# *Note: If you get stuck, try drawing a picture of a small linked list and
# running your function by hand. Does it actually work? Also, don't forget to
# consider edge cases (like a list with only 1 or 0 elements).*
# """


class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(head_of_list):
    current_node = head_of_list
    previous_node = None
    next_node = None

    # Until we have 'fallen off' the end of the list
    while current_node:
        # Copy a pointer to the next element
        # before we overwrite current_node.next
        next_node = current_node.next

        # Reverse the 'next' pointer
        current_node.next = previous_node

        # Step forward in the list
        previous_node = current_node  # everything that we just reveresed, used as a reference
        current_node = next_node

    return previous_node


# traverse, reverse, and update at the sime time


# SY: We using a pointer to update the internal nodes in the Linked List , b/c a pointer is simply referring to a node
# This current is traversing through the head/linked list
# The pointer is telling the code, hey look at this node and update it

""""STACKS AND QUEUES"""


# You are given an array of requests, where requests[i]
# can be "push <x>" or "pop".
# Return an array composed of the results of each "pop" operation that is performed.
# For requests = ["push 1", "push 2", "pop", "push 3", "pop"], the output should be
# queueOnStacks(requests) = [1, 2].
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        left.push(x)

    def remove():
        right.push(left.items[0])  # [5] # push the first element in the first stack fifo approach
        left.items = left.items[1:]  # at the sam etime remove that first element from stack1 by sliccing
        return right.pop()

    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans


# SY:
# # Were implementing a Queue(First In First Out) so we need to follow this order
# Use two stacks one that saves the items, and the other one(the right) is used to remove stuff
# The second stack basically removes the first item in the first stack
# And the first stack gets updated to only have [1:] the the items that came after the first saved into the left stack

# DT: stacks and queues


# Given a string sequence consisting of the characters '(', ')', '[', ']', '{', and '}'.
# Your task is to determine whether or not the sequence is a valid bracket sequence.
#
# The Valid bracket sequence is defined in the following way:
#
# An empty bracket sequence is a valid bracket sequence.
# If S is a valid bracket sequence then (S), [S] and {S} are also valid.
# If A and B are valid bracket sequences then AB is also valid.
# Example
#
# For sequence = "()", the output should be validBracketSequence(sequence) = true;
# For sequence = "()[]{}", the output should be validBracketSequence(sequence) = true;
# For sequence = "(]", the output should be validBracketSequence(sequence) = false;

# Plan:
# Convert everything into a list
# Use a stack (LIFO-approach) where

# plan
# set the brackets to have numerical representations

#
def validBracketSequence(sequence):
    dictionary = {"(": ")", "{": "}", "[": "]"}
    s = list(sequence)
    mapping = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    stack = []

    for c in s:
        if c not in mapping:
            if not stack or mapping[stack.pop()] != c:  # We want to access the earliest element inserted into the stack
                return False  # were checking if this closing bracket has a correspond element in stack that closses  this bracket c
        else:  # stack.pop() gets the last item inserted into the stack and is the first item to be removed too
            stack.append(
                c)  # this should correspond to the left brack which should close the two brackets and otherise return false
            # if you encounter a right bracket , u should encounter a left bracket in the stack as the earliest item/

    return len(stack) == 0


"""GRAPH PROBLEMS"""

from collections import deque


def numIslands(grid):
    # Your code here
    counter = 0
    # we need to find 1's
    # iterate through our matrix using a nested loop
    for row_index, row in enumerate(grid):
        for col_index, digit in enumerate(row):
            # what happens when we see a 1?
            if digit == "1":
                # increment our counter
                counter += 1
                # we also need to make sure we don't double count
                # mutate our input grid
                # if we see a 1, after we've processed it, let's just set it 0
                grid[row_index][col_index] = 0
                # figure out how far this island extends in the
                # horizontal and vertical directions
                queue = deque([(row_index, col_index)])

                # we need to process the 1's adjacent to the current 1
                while len(queue) > 0:
                    r, c = queue.popleft()
                    # check the 4 cardinal directions around the current 1
                    # if we see any other 1s, add it to queue

                    # look north
                    if r > 0 and grid[r - 1][c] == '1':
                        grid[r - 1][c] = 0
                        queue.append((r - 1, c))

                    # look south
                    if r < len(grid) - 1 and grid[r + 1][c] == '1':
                        grid[r + 1][c] = 0
                        queue.append((r + 1, c))

                    # look east
                    if c < len(row) - 1 and grid[r][c + 1] == '1':
                        grid[r][c + 1] = 0
                        queue.append((r, c + 1))

                    # look west
                    if c > 0 and grid[r][c - 1] == '1':
                        grid[r][c - 1] = 0
                        queue.append((r, c - 1))

    return counter


grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(numIslands(grid2))

# REVIEW if have time
# There are N students in a baking class together. Some of them are friends, while some are not friends.
# The students' friendship can be considered transitive. This means that if Ami is a direct friend of Bill, '
# and Bill is a direct friend of Casey, Ami is an indirect friend of Casey. A friend circle is a group of students
# who are either direct or indirect friends.Given a N*N matrix M representing the friend relationships between
# students in the class. If M[i][j] = 1,
# then the ith and jth students are direct friends with each other, otherwise not.
# You need to write a function that can output the total number of friend circles among all the students.

#
# def findCircleNum(M):
#     # len of
#     visited = [0] * len(M)
#     friend_circle = 0  # not 0 === True, 0 == False #counter
#
#     for i in range(len(M)): # going over all the friends
#         if not (visited[i]):
#             visited[i] = 1
#             friend_circle += 1
#             queue = [i]
#             while queue:
#                 popi = queue.pop(0)
#                 visited[popi] = 1
#                 for j in range(len(M)):
#                     if not (visited[j]) and M[popi][j] == 1:
#                         queue.append(j)
#                         visited[j] = 1
#
#     return friend_circle


"""
In a town, there are `N` people labelled from `1` to `N`.  There is a rumor
that one of these people is secretly the town judge.

If the town judge exists, then:

1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

You are given `trust`, an array of pairs `trust[i] = [a, b]` representing that ###NOTE: AT LOCATION I, THIS PERSON TRUSTS THAT PERSON ETC.
the person labelled `a` trusts the person labelled `b`.

If the town judge exists and can be identified, return the label of the town
judge.  Otherwise, return `-1`.

Example 1:

```plaintext
Input: N = 2, trust = [[1,2]]
Output: 2
```

Example 2:

```plaintext
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
```

Example 3:

```plaintext
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```

Example 4:

```plaintext
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
```

Example 5:

```plaintext
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
```

Constraints:

- `1 <= N <= 1000`
- `0 <= trust.length <= 10^4`
- `trust[i].length == 2`
- `trust[i]` are all different
- `trust[i][0] != trust[i][1]`
- `1 <= trust[i][0], trust[i][1] <= N`
"""

"""SOL:2 ARRAY ALGORITHIM"""

def find_judge(N, trust):
    """
    Inputs:
    N -> int
    trust -> List[List[int]]

    Output:
    int
    """
    # Your code here
    # In order for a town to exist, there needs to be one
    # node that every other node points to, and that node
    trusts_me = [0 for _ in range(
        N + 1)]  # placements for each person : Labels 1 through N => ex) label 1 current is trust by 0 persons
    # at index 0 this element is never going to get updated as there is no label with index
    # the reaon we include the 0 in range(N+1) is that we can match the labels in trustee to truts me 1:1
    # count the number of people who trust each person
    i_trust = [0 for _ in range(N + 1)]
    for truster, trustee in trust:
        trusts_me[trustee] += 1  # person(trustee) is getting trusted so add 1 to to trusts me corresponding to that label
        i_trust[truster] += 1  # we want to use the trustee labels as index to update the trusts me array

    # we can check to see if one person's `trust_count` == N - 1 # at most a person can be trusted N-1 times he can't include himself
    for person, trust_count in enumerate(trusts_me):
        if trust_count == N - 1 and i_trust[person] == 0:
            return person

            # we also need to check that this person has no outgoing arrows
    # cannot have any arrows pointing out from it
    # and there can only be one
    return -1


print(find_judge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
print(find_judge(3, [[1, 2], [2, 3]]))

#####

# Techniques: Indeph,
# Prob -> Graph
# DS: lists
# SY: Use two arrays, that keep track of who is satisfying the conditons of judge or not
# verify if conditions hold
