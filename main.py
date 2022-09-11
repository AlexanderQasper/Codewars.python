# Unique In Order

def unique_in_order(iterable):
    list1 = list(iterable)
    list2 = []
    for i in range(len(list1)):
        if len(list1) == 1:
            return list1
        else:
            if list1[i] != list1[i - 1]:
                list2.append(list1[i])
            return list2


print(unique_in_order('AAAABBBCCDAABBB'))
