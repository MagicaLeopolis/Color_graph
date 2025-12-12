def read_file(file_path):
    dic = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line_split = line.split(',')
            name = line_split[0]
            conected_name = line_split[1].strip()
            if not name in dic:
                dic[name] = []
            dic[name].append(conected_name)
            if not conected_name in dic:
                dic[conected_name] = []
            dic[conected_name].append(name)
    return dic
#print(read_file(('big_correct_graph.csv')))


def backtrack_color(start: int, dic: dict, colors: list) -> dict | bool:
    keys = list(dic.keys())

    if start == len(keys):
        return dict(correct_color)
    our_point = keys[start]

    for color in colors:
        mist = False
        for element in dic[our_point]:
            if element in correct_color and correct_color[element] == color:
                mist = True
                break
        if mist:
            continue

        correct_color[our_point] = color

        result = backtrack_color(start + 1, dic, colors)
        if result is not None:
            return result

        del correct_color[our_point]


    return None



# print(backtrack_color(0,{'a': ['b', 'c', 'e', 'f', 'h'], 'b': ['a', 'c', 'd', 'f', 'g', 'i'], 'c': ['a', 'b', 'e', 'g', 'h', 'j'], 'e': ['a', 'c', 'd', 'f', 'g', 'j'], 'f': ['a', 'b', 'd', 'e', 'h', 'i'], 'h': ['a', 'c', 'd', 'f', 'g', 'i', 'j'], 'd': ['b', 'e', 'f', 'h', 'i'], 'g': ['b', 'c', 'e', 'h', 'i', 'j'], 'i': ['b', 'd', 'f', 'g', 'h', 'j'], 'j': ['c', 'e', 'g', 'h', 'i']} , ['red', 'green', 'blue']))


def write_color_graph(result: dict):
    '''
    write out graph to a new file with correct colors
    '''
    with open('corect_colors.txt', 'w', encoding='utf-8') as file:
        for key, val in result.items():
            file.write(f'{key} -> {val}\n')


correct_color = {}

dic = read_file('big_correct_graph.csv')
start = 0
colors = ['red', 'green', 'blue']

result = backtrack_color(0, dic, colors)


if result is not None:
    print('Your graph is valid and we can colored it, in that way')
    print(result)
    write_color_graph(result)
else:
    print('Graph can not be colored correctly')
