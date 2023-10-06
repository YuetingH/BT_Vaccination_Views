## Module Function

import warnings
warnings.filterwarnings('ignore')

import numpy as np
import networkx as nx


def subgraph(G, node_retain):
    '''
    Get subgraph
    
    Input:
        G: original graph
        node_retain: a list of nodes that the subgraph contains
    
    Output:
        subG: subgraph of G containing nodes in node_retain
    '''
    
    node_remove = list(set(G.nodes) - set(node_retain))
    subG = G.copy(); subG.remove_nodes_from(node_remove)
                
    return subG



