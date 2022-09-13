# Unique In Order
# def unique_in_order(iterable):
#     newList = []
#     for item in iterable:
#         if len(newList) < 1 or not item == newList[len(newList) - 1]:
#             newList.append(item)
#     return newList
#
# print(unique_in_order('A'))

# Enough is enough!

list1 = [1, 1, 3, 3, 7, 2, 2, 2, 2]
numb = 3

def delete_nth(order, max_e):
    result = []
    occurrences = {}

    for n in order:
        count = occurrences.setdefault(n, 0)
        if count >= max_e:
            continue
        result.append(n)
        occurrences[n] += 1

    return result
