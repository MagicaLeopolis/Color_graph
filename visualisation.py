import matplotlib.pyplot as plt
import networkx as nx

def visualize_adjacency_list_graph(nodes_color: dict, edges: dict, filename):
  """
  param nodes: dictionary with nodes and their colors
  param edges: dictionary, where key is a vertice and value is a list of adjacent vertices
  param filename: filename to which the image will be saved
  """
    G = nx.from_dict_of_lists(edges)
    nx.set_node_attributes(G, nodes_color, 'color')
    color_map = nx.get_node_attributes(G, 'color')

    node_color_list = [color_map[node] for node in G.nodes()]
    num_nodes = G.number_of_nodes()
    node_size = 600 if num_nodes <= 10 else 250
    pos = nx.spring_layout(G, k=0.8, iterations=50)

    plt.figure(figsize=(12, 8))
    nx.draw_networkx(
        G,
        pos,
        with_labels=True,
        node_color=node_color_list,
        node_size=node_size,
        font_weight='bold',
        edge_color='dimgray',
        edgecolors='black'
        )
    
    plt.title("Візуалізація Трикольорового Графа", size=18)
    plt.axis('off')
    plt.savefig(filename, format="png", bbox_inches="tight") 
    print(f"\n✅ Граф успішно збережено у файл: {filename}")

   
