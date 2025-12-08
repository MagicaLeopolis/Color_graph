import random
def create_dict_right_color(dic: dict, matrix: list):
    colors = ['green','red','blue']
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if matrix[i][j] == 1:
                if dic[i] == dic[j]:
                    while True:
                        if dic[i] != dic[j]:
                            break
                        result = random.choice(colors)
                        dic[j] = result
    if dic[0] == dic[len(dic.keys()) - 1]:
        print('Цей граф не можна розмалювати')
        return None
    for i in range(len(dic.keys()) - 1):
        if dic[i] == dic[i + 1]:
            print('Цей граф не можна розмалювати')
            return None
    return dic
print(create_dict_right_color({0 : 'green', 1 : 'green', 2 : 'green', 3 : 'green', 4: 'red'},[[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]))
    # new_dict = {}
    # visited = []

    # for point, related in dic.items():
    #     if not point in new_dict:
    #         new_dict[point] = 'red'
    #     for el in related:
#             if not el in new_dict:
#                 new_dict[el] = 'green'
#     return new_dict
# print(create_dict_right_color({'a': ['b', 'e'], 'b': ['a', 'd', 'c'], 'e': ['a', 'c', 'd'], 'd': ['b', 'c', 'e'], 'c': ['b', 'e', 'd']}))
    # colors = ['green','red','blue']
    # color = random.choice(colors)
