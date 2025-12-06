import matplotlib.pyplot as plt
import networkx as nx

edge_color1= {'v1': 'green', 'v2': 'red', 'v3': 'blue'}
nodes = {'v1' : ['v2'], 'v2': ['v1'], 'v3': []}

G = nx.from_dict_of_lists(nodes)
nx.set_node_attributes(G, edge_color1, 'color') 



def visualize_adjacency_list_graph(G, filename):

    # Визначення позицій
    pos = nx.spring_layout(G, k=0.8, iterations=50)

    plt.figure(figsize=(12, 8))
    nx.draw_networkx(
        G,
        pos,
        with_labels=True,
        node_color=['green', 'red', 'blue'],
        node_size=300,
        font_weight='bold',
        edge_color='dimgray',
        edgecolors='black'
        )


    plt.title("Візуалізація Трикольорового Графа", size=18)
    plt.axis('off') #вимикаємо осі координат

    plt.savefig(filename, format="png", bbox_inches="tight") 
    print(f"\n Граф збережено у файл: {filename}")

    # plt.show() якщо хочете побачити зображення на екрані

visualize_adjacency_list_graph(G)
