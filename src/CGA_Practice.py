# Given an integer n and an array a of length n, your task is to apply the following mutation to a:
# Array a mutates into a new array b of length n.
# For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
# If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0.
# For example, b[0] should be equal to 0 + a[0] + a[1].
# Example
#
# For n = 5 and a = [4, 0, 1, -2, 3], the output should be mutateTheArray(n, a) = [4, 5, -1, 2, 1].
#
# b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
# b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
# b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
# b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
# b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1
# So, the resulting array after the mutation will be [4, 5, -1, 2, 1].

# given
# array a, with length of n
# want
# convert a into array b of length n
# i is within  0 and n-1
# each element has value given by b[i] = a[i - 1] + a[i] + a[i + 1]
# if i not in 0<= i <= n-1 then i =0
# plan
# for every element in array a convert that element into b[i] = a[i - 1] + a[i] + a[i + 1]
# have 3 variables that are equal to var1 = i -1, var2 = i, var = i+1
# if var1,var2,var3 not in range(0,n-1) then var
# iterate over a and save each element into some variable new_element =

def mutateTheArray(n, a):
    indexs = set(range(0, n))
    new_array = []
    for i, element in enumerate(a):
        print(f'index{i}')
        var1 = i - 1
        var2 = i
        var3 = i + 1
        temp = [None, None, None]
        if var1 not in indexs:
            temp[0] = 0
        else:
            temp[0] = a[var1]
        if var2 not in indexs:
            temp[1] = 0
        else:
            temp[1] = a[var2]
        if var3 not in indexs:
            temp[2] = 0
        else:
            temp[2] = a[var3]
        el1, el2, el3 = tuple(temp)
        print(el1, el2, el3)
        new_array.append(el1 + el2 + el3)
        print(new_array)
    return new_array


"""ARRAY PROB"""


#
# For n = 5 and a = [4, 0, 1, -2, 3], the output should be mutateTheArray(n, a) = [4, 5, -1, 2, 1].
#
# b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
# b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
# b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
# b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
# b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1
# So, the resulting array after the mutation will be [4, 5, -1, 2, 1].
# 120min

# GOOGLE MOCK EXAM
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        k = 0
        reformated_license = ""

        for key in S[::-1]:
            if key == "-":
                continue

            if k == K:
                k = 0
                reformated_license = '-' + reformated_license

            reformated_license = key.upper() + reformated_license
            k += 1

        return reformated_license


# Test
# Input: S = "2-5g-3-J", K = 2
#
# Output: "2-5G-3J"
#
# Explanation: The string S has been split into three parts, each
# part has 2 characters except the first part as it could be shorter as mentioned above.
S = "2-5g-3-J"
K = 2
s = Solution()
s.licenseKeyFormatting(S, K)

"""LINKED LIST"""


# 2. Add Two Numbers
# Definition for singly-linked list.
#
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# plan
# reverse L1, reverse L2
# append the numbers in L1 into list1 and do the same for L2 into list 2
# take the sum of list1 and sum of list2 => reverse it again
# add these two numbers together
# convert back into linked list with helper function
class Solution:
    def lst2link(self, lst):
        cur = dummy = ListNode(0)
        for e in lst:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = []
        list2 = []
        current1 = l1
        current2 = l2
        while current1:
            list1.append(current1.val)
            current1 = current1.next
        while current2:
            list2.append(current2.val)
            current2 = current2.next
        list1 = list1[::-1]
        list2 = list2[::-1]
        print(list1)
        print(list2)
        # concatenate numbers into one
        num1 = int("".join(str(num) for num in list1))
        num2 = int("".join(str(num) for num in list2))
        num3 = num1 + num2
        print(num3)
        # convert back into list
        new_list = [int(num) for num in str(num3)[::-1]]
        print(new_list)
        return self.lst2link(new_list)


"""GRAPH PROBLEMS"""


# https://leetcode.com/problems/number-of-islands/discuss/890466/DFS-and-BFS-with-Easy-Explanation
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        q, visit = collections.deque(), set()
        islands = 0

        def bfs(r, c):
            q.append((r, c))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and
                            grid[r][c] == "1" and (r, c) not in visit
                    ):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands


# test it
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c

d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
d.next = e
e.next = f

"""TREES"""
from collections import deque


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        level = {}  # dictionary
        q = deque()  # save things here to do the level order search
        q.append((root, 0))  # append a tuple with the root node and its level # we start at level 0 the root
        while q:  # do a while loop to iterate of queue until its empty
            a, b = q.popleft()  # access the root and level, were also shrinking the queue
            level[b] = level.get(b, []) + [
                a.val]  # b corresponds to the level, it we start a 0, level will currently empty so just retun an empty list and add it to the root.value, so at level[0] we have value a.val

            # Note: [1] + [12] = [1,12] so when we do level.get, we get some [number ] => + [number] + [a.va] = [number,a.val], for some level
            if a.left:  # look at the left node/child
                q.append(
                    (a.left, b + 1))  # append the left node and with its corresponding leve (ex after we have level1)
            if a.right:  # do the same to the right with its corresponding level
                q.append((a.right, b + 1))
        ans = []  # ??? # were going to save the max values for each level here
        for i in range(max(
                level) + 1):  # if theres 2 levels then max(level) == 1 so range(0,1) => will only append the max value of root, so we need to add 1 so that it appends all the max values for all the levels levels
            ans.append(max(level[i]))
        return ans


"""OTHER"""


# given
# i goes from 0 to n-1
# fucntion that matates element b[i] , i is index to become a[i - 1] + a[i] + a[i + 1]
# i-1, i, i+1 have to be within bonuds
# if  index< 0 or index > n-1 then just return 0 for that element at a[index]
# create new_list based on the element produced by a[i - 1] + a[i] + a[i + 1]

# plan
# create function
def mutateTheArray(n, a):
    new_list = []
    for index in range(n):
        temp = 0
        for new_element in [index - 1, index, index + 1]:
            if new_element < 0 or new_element > n - 1:
                new_element = 0
                temp += 0
            else:
                temp += a[new_element]
        new_list.append(temp)
    return new_list


# TESTS
# For n = 5 and a = [4, 0, 1, -2, 3], the output should be mutateTheArray(n, a) = [4, 5, -1, 2, 1]
#

# prob2
# two lists a,b of integers, same length L
# int k
# iterate and get groups (xy) from list a and b
# tiny if new number xy < k

# return tiny parys
# two lists a,b of integers, same length L
# int k
# iterate and get groups (xy) from list a and b
# tiny if new number xy < k

# return tiny parys
def countTinyPairs(a, b, k):
    b = b[
        ::-1]  # were iterating from left to right so reverse b so when we iterate we are starting from right and going to left
    pairs = []
    for x, y in zip(a, b):
        tiny = int(str(x) + str(y))

        if tiny < k:
            pairs.append(tiny)
        else:
            continue
    return len(pairs)


# For a = [1, 2, 3], b = [1, 2, 3], and k = 31, the output should be
# countTinyPairs(a, b, k) = 2.

a = [1, 2, 3]
b = [1, 2, 3]
k = 31


# TESTS
# For a = [1, 2, 3], b = [1, 2, 3], and k = 31, the output should be
# countTinyPairs(a, b, k) = 2.
#
# We're considering the following pairs during iteration:
#
# (1, 3). Their concatenation equals 13, which is less than 31, so the pair is tiny;
# (2, 2). Their concatenation equals 22, which is less than 31, so the pair is tiny;
# (3, 1). Their concatenation equals 31, which is not less than 31, so the pair is not tiny.
# As you can see, there are 2 tiny pairs during the iteration, so the answer is 2.


# Each group should contain a set of indices (i, j, etc), such that the corresponding arrays (a[i], a[j], etc)
# all have the same mean. Return the set of groups as an array of arrays, where the indices within each group are
# sorted in ascending order, and the groups are sorted in ascending order of their minimum element.
#
# Example
#
# For
#
# a = [[3, 3, 4, 2],
#      [4, 4],
#      [4, 0, 3, 3],
#      [2, 3],
#      [3, 3, 3]]
# the output should be
#
# meanGroups(a) = [[0, 4],
#                  [1],
#                  [2, 3]]
# mean(a[0]) = (3 + 3 + 4 + 2) / 4 = 3;
# mean(a[1]) = (4 + 4) / 2 = 4;
# mean(a[2]) = (4 + 0 + 3 + 3) / 4 = 2.5;
# mean(a[3]) = (2 + 3) / 2 = 2.5;
# mean(a[4]) = (3 + 3 + 3) / 3 = 3.
# There are three groups of means: those with mean 2.5, 3, and 4. And they form the following groups:
#
# Arrays with indices 0 and 4 form a group with mean 3;
# Array with index 1 forms a group with mean 4;
# Arrays with indices 2 and 3 form a group with mean 2.5.


# given
# list a conisting of other lists
# group by mean values
# lists with == mean values are in same group
# lists w/ different mean vals are in diff groups
# the groups will contain list of labels(based on there index of the original list)

def meanGroups(a):
    groups = []
    dictionary = {}
    dictionary2 = {}  # key represents mean, and val represent list of indexs
    for index, array in enumerate(a):
        mean = sum(array) / len(array)
        dictionary[index] = mean
    for key, index in dictionary.items():
        if index not in dictionary2:
            dictionary2[index] = [key]  # the problem I was encountering was not updating dictionary2 correctly
        else:
            dictionary2[index].append(key)
    for key, value in dictionary2.items():
        groups.append(value)
    return groups


a = [[3, 3, 4, 2],
     [4, 4],
     [4, 0, 3, 3],
     [2, 3],
     [3, 3, 3]]

print(meanGroups(a))

# In the begging we made a basic logistic regression model, and that was used by the front end to make there erratic app.
#
# Here is the mockup app.
#
# Allan will take it from here and talk about the fast api
#
# Example
#
# For
# a = [10, 2], the output should be
# concatenationsSum(a) = 1344.
#
# a[0] ∘ a[0] = 10 ∘ 10 = 1010,
# a[0] ∘ a[1] = 10 ∘ 2 = 102,
# a[1] ∘ a[0] = 2 ∘ 10 = 210,
# a[1] ∘ a[1] = 2 ∘ 2 = 22.
# So
# the
# sum is equal
# to
# 1010 + 102 + 210 + 22 = 1344.
#
# For
# a = [8], the
# output
# should
# be
# concatenationsSum(a) = 88.
#
# There is only
# one
# number in a, and a[0] ∘ a[0] = 8 ∘ 8 = 88, so
# the
# answer is 88.
#
# For
# a = [1, 2, 3], the
# output
# should
# be
# concatenationsSum(a) = 198.
#
# a[0] ∘ a[0] = 1 ∘ 1 = 11,
# a[0] ∘ a[1] = 1 ∘ 2 = 12,
# a[0] ∘ a[2] = 1 ∘ 3 = 13,
# a[1] ∘ a[0] = 2 ∘ 1 = 21,
# a[1] ∘ a[1] = 2 ∘ 2 = 22,
# a[1] ∘ a[2] = 2 ∘ 3 = 23,
# a[2] ∘ a[0] = 3 ∘ 1 = 31,
# a[2] ∘ a[1] = 3 ∘ 2 = 32,
# a[2] ∘ a[2] = 3 ∘ 3 = 33.
# The
# total
# result is 11 + 12 + 13 + 21 + 22 + 23 + 31 + 32 + 33 = 198
