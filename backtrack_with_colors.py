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
#print(read_file(('graph.csv')))


def color_start(file_path):
    with open(file_path, 'r', encoding= 'utf-8') as file:
        dic = {}
        for line in file:
            line_split = line.split(',')
            point = line_split[0]
            color = line_split[1].strip()
            if not point in dic:
                dic[point] = color
    return dic
#print(color_start(('correct_color.csv')))

def backtrack_color( dic: dict, d: dict, colors: list, correct_colar: dict, start: int = 0) -> dict | bool:
    keys = list(dic.keys())

    if start == len(keys):
        final_result = d.copy()
        final_result.update(correct_colar)
        print(f"Знайдене розфарбування: {final_result}")
        return final_result


    our_point = keys[start]

    if our_point in d:
        current_color = d[our_point]
        for element in dic.get(our_point, []):
            if element in d and d[element] == current_color:
                if start == 0:
                    print(f'Розфарбування неможливе через вершини {our_point} та {element} мають один і той самий колір {current_color}.')
                return None
        return backtrack_color(dic, d, colors, correct_colar, start+1)

    for color in colors:
        mist = False
        for element in dic.get(our_point, []):
            if (element in d and d[element] == color) or (element in correct_colar and correct_colar[element] == color):
                mist = True
                break

        if mist:
            continue

        correct_colar[our_point] = color

        result = backtrack_color(dic, d, colors, correct_colar, start + 1)
        if result is not None:
            return result

        del correct_colar[our_point]
    if start == 0:
        print('Розвязку знайти не вдялося')

    return None


#print(backtrack_color({'a': ['b', 'e'], 'b': ['a', 'd', 'c'], 'e': ['a', 'c', 'd'], 'd': ['b', 'c', 'e'], 'c': ['b', 'e', 'd']}, {'a': 'red', 'b': 'red', 'c': 'blue', 'd': 'green', 'e': 'green'}, ['red', 'green', 'blue'], {}, 0))


def write_color_graph(result: dict):
    '''
    write out graph to a new file with correct colors
    '''
    try:
        with open('corect_colors.txt', 'w', encoding='utf-8') as file:
            for key, val in result.items():
                file.write(f'{key} -> {val}\n')
    except Exception:
        print('Цей граф неможливо розфарбувати коректно')


if __name__ == '__main__':
    COLORS = ['red', 'green', 'blue']
