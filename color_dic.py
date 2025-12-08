def color_start(file_path):
    with open(file_path, 'r', encoding= 'utf-8') as file:
        dic = {}
        for line in file:
            line_split = line.split(',')
            point = line_split[0]
            color = line_split[1].strip()
            if not point in dic:
                dic[point] = []
            dic[point].append(color)
    return dic
print(color_start('color_start.csv'))


def backtrack_right_color(dic: dict) -> dict:
    '''
    Docstring for backtrack_right_color

    :type dic: dict
    :type return: dict
    return correct dictionary with correct colors
    '''
    correct_dct = {}
    key = list(dic.keys())
    colors = ['green', 'red', 'blue']


    for num, point in enumerate(key):
        our_color = dic[point]

        next_color = None
        if  num < len(key) - 1:
            next_point = key[num + 1]
            next_color = dic[next_point]

        if next_color != our_color and next_color is None:
            for point, val in dic.items():
                if point not in correct_dct:
                    correct_dct[point] = val

        elif next_color == our_color:
            def backtracking(col_ind: int):
                if col_ind == len(colors):
                    return 'Нема відповідного кольору'
                approve_color = colors[col_ind]

                if num > 0:
                    last_point = key[num-1]
                    if approve_color == dic[last_point]:
                        return backtracking(col_ind + 1)

                if num < len(key) - 1:
                    next_point = key[num+1]
                    if dic[next_point] == approve_color:
                        return backtracking(col_ind + 1)

                return approve_color
            new_color = backtracking(0)
            dic[point] = new_color
            for point, val in dic.items():
                if point not in correct_dct:
                    correct_dct[point] = [val]

    return correct_dct
print(backtrack_right_color({'0': ['green'], '1': ['red'], '3': ['blue'], '4': ['blue'], '5': ['red']}))


def write_color_graph(correct_dct: dict):
    '''
    write out graph to a new file with correct colors
    '''
    with open('corect_colors', 'w', encoding='utf-8') as file:
        for key, val in correct_dct.items():
            file.write(f'{key} -> {val}\n')

result = backtrack_right_color({'0': 'green', '1': 'red', '3': 'blue', '4': 'blue', '5': 'red'})
write_color_graph(result)
