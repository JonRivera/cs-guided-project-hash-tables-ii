# https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1
# Given a linked list of integers, remove any nodes from the linked list that have values that have previously occurred in the linked list. Your function should return a reference to the head of the updated linked list.
#
# Example:
# Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
# Output: (3) -> (4) -> (2) -> (6) -> (1) -> N
# Explanation: The input list contains redundant nodes (3), (6), and (2), so those should be removed from the list.
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def condense_linked_list(head):
    # base case of empty list or list with only one element
    if head is None or head.next is None:
        return head

    hash = set()

    walk = head
    hash.add(head.value)

    while walk.next is not None:

        if walk.next.value in hash:
            walk.next = walk.next.next

        else:
            hash.add(walk.next.value)

            walk = walk.next

    return head

    # given
    # linked list (of) int
    # remove nodes form LL that have already occured (the nodes who first had vals --- keep them)

    # want
    # return head of new_LL

    # plan
    # iterate over the node

    # have variable that stores node.val in a dict
    # if when iterating we encounter a node with a val in dict then remove it
    # continue iterating over the node
    # when self.next == None stop


# def condense_linked_list(node):
#     global new
#     dictionary = set()
#     current = node
#     next = None
#     while current:
#         next_node = current.next
#         print(current.value)
#         print(dictionary)
#         if current.value in dictionary:
#             current = current.next
#         elif current.value not in dictionary:
#             dictionary.add(current.value)
#             new = ListNode(current.value)
#             print(new.value)
#             new.next = next
#             next = new
#             current = current.next
#
#         return new


#
def first_not_repeating_character(string):
    # Understand
    # we want the first non repeating character
    # in other words, we want the first character that didn't repeated itself for the first n characters
    # Plan
    # Split string into individual characters
    # run a for loop that keeps saves the counts of the chars in the string
    # run another loop that references this counts
    # when the first count is === then that represents our first non repeating number
    # else return "_"

    counts = {}
    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for index, char in enumerate(string):
        if counts[char] == 1:
            return char
    return "_"


# given
# city state of n people
# spy doesn't trust anyone
# trusted by everyone
# also given some graph(or a list) containing relationships btw different people regarding trust

# plan
# have one array with n elements of 0 (represents trust me)
# the othe array(I trust array) will alson contain 0s
# loop over the trust array
# in this loop I am updating truster and trustee
#


# In a city-state of n people, there is a rumor going around that one of the n people is a spy for
# the neighboring city-state.
#
# The spy, if it exists:
#
# Does not trust anyone else.
# Is trusted by everyone else (he's good at his job).
# Works alone; there are no other spies in the city-state.
# You are given a list of pairs, trust. Each trust[i] = [a, b] represents the fact that person a trusts person b.
#
# If the spy exists and can be found, return their identifier. Otherwise, return -1.
#
# Example 1:
#
# Input: n = 2, trust = [[1, 2]]
# Output: 2
# Explanation: Person 1 trusts Person 2, but Person 2 does not trust Person 1, so Person 2 is the spy.


def uncover_spy(n, trust):
    trust_me = (n + 1) * [0]  # we do this b/c a person will be labeled btw numbers 1 through n+1,
    i_trust = (n + 1) * [0]  # we want person trusts arrays based on there labels
    for truster, trustee in trust:  # note that trust[0] corresponds to trustee and and trust[1] corresponsd to trusteee
        trust_me[trustee] += 1
        i_trust[truster] += 1  # update i trust at index corresponding to trusteer #note the spy trusts noboy

    for person, trust_counts in enumerate(trust_me):  # spy should be trusted by N-1 people (not including himself)
        if trust_counts == n - 1 and i_trust[person] == 0:  # perons being the index or label corresponding to person
            return person
    else:
        return -1
