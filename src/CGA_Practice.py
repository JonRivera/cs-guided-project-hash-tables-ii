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
#
# For n = 5 and a = [4, 0, 1, -2, 3], the output should be mutateTheArray(n, a) = [4, 5, -1, 2, 1].
#
# b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
# b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
# b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
# b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
# b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1
# So, the resulting array after the mutation will be [4, 5, -1, 2, 1].
#120min

#GOOGLE MOCK EXAM
#    def licenseKeyFormatting(self, S: str, K: int) -> str:
def licenseKeyFormatting(self, S: str, K: int) -> str:
    S = S.split("-")
    new_word = "".joing(char for char in S)
    print(S)
S = "5F3Z-2e-9-w"
K = 4
licenseKeyFormatting(S,K)

