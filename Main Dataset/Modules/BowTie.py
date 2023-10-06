## Module Function

import warnings
warnings.filterwarnings('ignore')

import numpy as np
import networkx as nx


def get_bowtie_components(G):
    GT = nx.reverse(G, copy=True)   # All edge directions are reversed
    
    strongly_con_comp = list(nx.strongly_connected_components(G))
    strongly_con_comp = max(strongly_con_comp, key=len)
    
    S = strongly_con_comp   # list of SCC
    
    v_any = list(S)[0]   # an arbitrary node in SCC 
    DFS_G = set(nx.dfs_tree(G,v_any).nodes())   # the set of nodes that v_any can reach (depth-first-search)
    DFS_GT = set(nx.dfs_tree(GT,v_any).nodes()) # the set of nodes that can reach v_any (depth-first-search)
    OUT = DFS_G - S
    IN = DFS_GT - S
    V_rest = set(G.nodes()) - S - OUT - IN
    
    
    TUBES = set()
    INTENDRILS = set()
    OUTTENDRILS = set()
    OTHER = set()
    
    for v in V_rest:
        irv = len(IN & set(nx.dfs_tree(GT,v).nodes())) is not 0
        vro = len(OUT & set(nx.dfs_tree(G,v).nodes())) is not 0
        if irv and vro:
            TUBES.add(v)
        elif irv and not vro:
            INTENDRILS.add(v)
        elif not irv and vro:
            OUTTENDRILS.add(v)
        elif not irv and not vro:
            OTHER.add(v)
    
    return list(S), list(IN), list(OUT), list(TUBES), list(INTENDRILS), list(OUTTENDRILS), list(OTHER)


def get_bowtie_components_num(G):
    S, IN, OUT, TUBES, INTENDRILS, OUTTENDRILS, OTHER = get_bowtie_components(G)
    
    return len(S), len(IN), len(OUT), len(TUBES), len(INTENDRILS), len(OUTTENDRILS), len(OTHER)


def get_bowtie_components_percent(G):
    S, IN, OUT, TUBES, INTENDRILS, OUTTENDRILS, OTHER = get_bowtie_components(G)
    sum_num = len(S) + len(IN) + len(OUT) + len(TUBES) + len(INTENDRILS) + len(OUTTENDRILS) + len(OTHER)
    
    return len(S)/sum_num, len(IN)/sum_num, len(OUT)/sum_num, len(TUBES)/sum_num, len(INTENDRILS)/sum_num, len(OUTTENDRILS)/sum_num, len(OTHER)/sum_num

