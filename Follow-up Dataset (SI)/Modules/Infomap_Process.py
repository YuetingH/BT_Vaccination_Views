## Module Function

import warnings
warnings.filterwarnings('ignore')


from infomap import Infomap
import networkx as nx


def infomap(G, num_trials = 100, seed = 0, resultPrint = True):
    im = Infomap("--two-level --directed", silent=True, num_trials = num_trials, seed = seed)
    mapping = im.add_networkx_graph(G)
    im.run()
    
    if resultPrint:
        print(f"Found {im.num_top_modules} modules")
        print('---------------------')
        print('Module codelength, Index codelength, Codelength:')
        print(im.module_codelength, im.index_codelength, im.codelength)
    
    comm = im.get_modules(depth_level=1)

    return {mapping[i]: comm[i] - 1 for i in mapping.keys()}

def sort_community(node_to_community, reverse = True):
    values = list(node_to_community.values())
    count_num = [values.count(i) for i in list(set(values))]
    sorted_index = sorted(range(len(count_num)), key=lambda k: count_num[k], reverse=reverse) # Permutation
    sorted_dict = {sorted_index[i]: list(set(values))[i] for i in range(len(list(set(values))))}

    return {item[0]: sorted_dict[item[1]] for item in node_to_community.items()}

def convert_community(comm):
    num = max(comm.values()) + 1
    convert_comm = []
    for i in range(num):
        k_list = [k for k,v in comm.items() if v == i]
        convert_comm.append(k_list)
    
    return convert_comm

def process_infomap(G, num_trials = 100, seed = 1, convert = True, resultPrint = True):
    '''
    Main function for Infomap community detection.
    
    Input: G (Directed graph), 
           seed & num_trials (Stochasticity of Infomap), 
           convert: if True, return [[node_A, node_B], [], [], ...]
                    else False, return [node_A: x, node_B: y, ...]
           resultPrint: print Infomap results. This includes module codelength, index codelength, codelength
    
    Return: community assignment result, depending on convert
    '''
    comm = infomap(G, num_trials, seed, resultPrint)
    
    if convert:
        sort_comm = sort_community(comm)
        return convert_community(sort_comm)
    else:
        sort_comm = sort_community(comm, reverse = False)
        return sort_comm
    
def rearrange_graph(G, comm):
    '''
    Post processing for drawing the adjacency matrix.
    
    Input: G (Directed graph), 
           comm (Dictionary representing community assignment)
           
    Return: Reorganized graph new_G such that the larger the community is, the nodes of the community will be added first when               constructing new_G
    '''
    new_G = nx.DiGraph() # Directed graph
    
    list_node_property = list(comm.values())
    sorted_index = sorted(range(len(list_node_property)), key=lambda k: list_node_property[k], reverse=True) # Permutation
    list_node = list(G.nodes.items())
    
    # Add nodes
    for index in sorted_index:
        new_G.add_nodes_from([list_node[index]])
    
    # Add edges
    for elem in G.edges.data():
        new_G.add_edges_from([elem])
    return new_G



