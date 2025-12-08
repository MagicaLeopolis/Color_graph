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
print(read_file(('graph.csv')))



def write_matrix(dic):
    matrix = []
    n = len(dic.keys())
    for i in range(n):
        line =[]
        for j in range(n):
            line.append(0)
        matrix.append(line)
    keys = sorted(dic.keys())
    for i , key in enumerate(keys):
        for connected in dic[key]:
            i_2 = keys.index(connected)
            matrix[i][i_2] = 1
    return matrix
print(write_matrix({'a': ['b', 'e'], 'b': ['a', 'c'], 'c': ['b', 'd'], 'd': ['c', 'e'], 'e': ['d', 'a']}))
