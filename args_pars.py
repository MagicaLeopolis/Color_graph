import argparse

from create_dict_right_color import create_dict_right_color
from read_file import read_file, write_matrix
from Our_main_cod_without_color import backtrack_color
from visualisation import visualize_adjacency_list_graph


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--file", required=True, help="CSV файл графа")
    parser.add_argument("--img", default="graph.png", help="Куди зберегти зображення")

    args = parser.parse_args()

    dic = read_file(args.file)
    print("Словник суміжності:", dic)

    matrix, keys = write_matrix(dic)
    print("Матриця:", matrix)

    result = backtrack_color(0, dic, ['red', 'green', 'blue'])
    print("Backtracking:", result)

    index_colors = {i: result[key] for i, key in enumerate(keys)}
    fixed = create_dict_right_color(index_colors, matrix)

    if fixed is None:
        print("Граф неможливо розфарбувати")
        exit()

    final_colors = {keys[i]: fixed[i] for i in range(len(keys))}
    print(dic)

    visualize_adjacency_list_graph(final_colors, dic, args.img)
