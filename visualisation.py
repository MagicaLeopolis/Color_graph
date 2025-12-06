import matplotlib.pyplot as plt
import networkx as nx

edge_color1= {'1': 'red', '2': 'green', '3': 'blue', '4':'red', '5': 'green'} #result of "" function
nodes = {'1' : ['2', '5'], '2': ['3', '1'], '3': ['4', '2'], '4':['5', '3'], '5':['1', '4']} #result of "" function


G = nx.from_dict_of_lists(nodes) 
nx.set_node_attributes(G, edge_color1, 'color') 



def visualize_adjacency_list_graph(G, filename: str, status: str):
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

    if status == 'old':
        text = 'Visualisation of new correct graph'
    else:
        text = 'Visualisation of graph with initial (wrong) colors'
    plt.title(text, size=18)
    plt.axis('off')

    plt.savefig(filename, format="png", bbox_inches="tight") 
    print(f"\nPicture of the graph is saved in: {filename}")


visualize_adjacency_list_graph(G, 'graph.png')
