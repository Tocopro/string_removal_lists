# removing elements chosen

def removing_elements():
    list1 = ['mike', '', 'emma', 'kelly', '', 'brad']
    list_len = len(list1)
    list2 = []
    for i in range(list_len):
        if list1[i] == '':
            continue
        else:
            list2.append(list1[i])
    print(list2)

removing_elements()
