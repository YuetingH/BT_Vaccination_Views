## Module Function

import warnings
warnings.filterwarnings('ignore')

import networkx as nx

# import module within the same file
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import Infomap_Process as IP
import NetworkX_Extension as nx_e
import BowTie as bt

def role_attribute(G, roles, roles_names, attribute_name):
    d = {}
    counter = 0
    for k in roles:
        v = roles_names
        d.update(dict(zip(k, [v[counter]]*len(k))))
        counter += 1
    
    nx.set_node_attributes(G, d, name = attribute_name)
    
def within_role(G):
    
    # Bow-tie Role Detection
    G_anti = nx_e.subgraph(G, list(G.nodes)[:317])
    G_pro = nx_e.subgraph(G, list(G.nodes)[1202:])
    G_neu = nx_e.subgraph(G, list(G.nodes)[317:1202])
    
    # Bow-tie Role Assignment
    S_within = bt.get_bowtie_components(G_anti)[0] + bt.get_bowtie_components(G_neu)[0] + bt.get_bowtie_components(G_pro)[0]
    IN_within = bt.get_bowtie_components(G_anti)[1] + bt.get_bowtie_components(G_neu)[1] + bt.get_bowtie_components(G_pro)[1]
    OUT_within = bt.get_bowtie_components(G_anti)[2] + bt.get_bowtie_components(G_neu)[2] + bt.get_bowtie_components(G_pro)[2]
    TUBES_within = bt.get_bowtie_components(G_anti)[3] + bt.get_bowtie_components(G_neu)[3] + bt.get_bowtie_components(G_pro)[3]
    INTENDRILS_within = bt.get_bowtie_components(G_anti)[4] + bt.get_bowtie_components(G_neu)[4] + bt.get_bowtie_components(G_pro)[4]
    OUTTENDRILS_within = bt.get_bowtie_components(G_anti)[5] + bt.get_bowtie_components(G_neu)[5] + bt.get_bowtie_components(G_pro)[5]
    OTHER_within = bt.get_bowtie_components(G_anti)[6] + bt.get_bowtie_components(G_neu)[6] + bt.get_bowtie_components(G_pro)[6] 
    
    # Add bow-tie role as an attribute to each node in a graph
    roles_within = [S_within, IN_within, OUT_within, TUBES_within, INTENDRILS_within, OUTTENDRILS_within, OTHER_within]
    roles_names = ['S', 'IN', 'OUT', 'TUBES', 'INTENDRILS', 'OUTTENDRILS', 'OTHERS']
    role_attribute(G, roles_within, roles_names, 'within_role')
    
def across_role(G, G_comm = None):
    
    if not G_comm:
        # Community
        G_comm = IP.process_infomap(G, resultPrint = False)
    
    # Add community assignent as an attribute to each node in a graph
    comm_names = [str(i) for i in range(len(G_comm))]
    role_attribute(G, G_comm, comm_names, 'infomap_comm')
    
    # Bow-tie Role Detection
    G_commgraph = []
    for comm in G_comm:
        G_commgraph.append(nx_e.subgraph(G, comm))
    
    # Bow-tie Role Assignment
    S_across = []; IN_across = []; OUT_across = []; TUBES_across = []; INTENDRILS_across = []; OUTENDRILS_across = []; OTHER_across = []; UNASSIGNED_across = [] 
    for commgraph in G_commgraph:
        if len(commgraph.nodes)>5:
            S_across += bt.get_bowtie_components(commgraph)[0]
            IN_across += bt.get_bowtie_components(commgraph)[1]
            OUT_across += bt.get_bowtie_components(commgraph)[2]
            TUBES_across += bt.get_bowtie_components(commgraph)[3]
            INTENDRILS_across += bt.get_bowtie_components(commgraph)[4]
            OUTENDRILS_across += bt.get_bowtie_components(commgraph)[5]
            OTHER_across += bt.get_bowtie_components(commgraph)[6]
        else:
            UNASSIGNED_across += list(commgraph.nodes)
            
    # Add bow-tie role as an attribute to each node in a graph
    roles_across = [S_across, IN_across, OUT_across, TUBES_across, INTENDRILS_across, OUTENDRILS_across, OTHER_across, UNASSIGNED_across]
    roles_names = ['S', 'IN', 'OUT', 'TUBES', 'INTENDRILS', 'OUTTENDRILS', 'OTHERS', 'UNASSIGNED']
    role_attribute(G, roles_across, roles_names, 'across_role')
    



