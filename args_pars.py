'''
main
python main.py --file testing3(edges).csv --img my_graph.png
or :
python main.py --file testing3(edges).csv --img my_graph.png --with_colors correct_colors.csv
'''

import argparse
from visualisation import visualize_adjacency_list_graph
import backtracking_without_color as f
import backtrack_with_colors as extra


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Graph 3-coloring tool")

    parser.add_argument("--file", required=True, help="CSV файл з ребрами графа")
    parser.add_argument("--img", default="graph.png", help="Куди зберегти зображення графа")
    parser.add_argument("--with_colors", help="CSV файл із початковими кольорами (опціонально)")

    args = parser.parse_args()

    dic = f.read_file(args.file)
    print("\n Словник суміжності:")
    print(dic)

    f.correct_color = {}

    print("\n Виконуємо backtracking (стандартний)")
    result = f.backtrack_color(0, dic, ["red", "green", "blue"])

    if result is None:
        print("\n Граф неможливо розфарбувати.")
        exit()

    print("\n Результат розфарбування (основний):")
    print(result)

    f.write_color_graph(result)
    print("\n Кольори збережено у corect_colors.txt")

    visualize_adjacency_list_graph(result, dic, args.img)
    print("\n Граф збережено у:", args.img)


    if args.with_colors:
        print("\n==========================")
        print(" РЕЖИМ З КОРЕКТНИМИ КОЛЬОРАМИ")
        print("==========================")

        start_colors = extra.color_start(args.with_colors)
        print("\n Початкові (неправильні) кольори:")
        print(start_colors)

        print("\n Виконуємо backtracking_with_colors ...")

        result2 = extra.backtrack_color(dic=dic,d=start_colors,colors=["red", "green", "blue"],\
                                        correct_colar={},start=0)

        if result2 is None:
            print("\n Другий backtracking: неможливо знайти розфарбування.")
        else:
            print("\n Результат другого алгоритму (виправлені кольори):")
            print(result2)

        print("\n РЕЖИМ З КОЛЬОРАМИ ЗАВЕРШЕНО.")
