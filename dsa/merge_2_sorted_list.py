# Question
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

def mergeTwoLists(list1, list2):
    i = 0
    j = 0
    result = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            result.append(list2[j])
            j += 1
        else:
            result.append(list1[i])
            result.append(list2[j])
            i += 1
            j += 1

    while i < len(list1):
        result.append(list1[i])
        i += 1

    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result


# Test case
list1 = [1, 2, 4]
list2 = [1, 3, 4]
print(mergeTwoLists(list1, list2))  # Output: [1, 1, 2, 3, 4, 4]

list1 = []
list2 = [1]
print(mergeTwoLists(list1, list2))  # Output: [1]

list1 = [1]
list2 = []
print(mergeTwoLists(list1, list2))  # Output: [1]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(mergeTwoLists(list1, list2))  # Output: [1, 2, 3, 4, 5, 6]

list1 = [1, 2, 6, 7, 8, 9]
list2 = [1, 3, 4, 5, 10, 11]
print(mergeTwoLists(list1, list2))
