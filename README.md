# BT_Vaccination_Views
This repo documents the dataset and the programming code used in our paper titled "Modelling and Predicting Online Vaccination Views Using Bow-tie Decomposition".


## Dataset
In this paper, we investigate a temporal dataset that describes the Facebook vaccination views campaign in network representations, involving nearly 100 million users on Facebook from across countries, continents and languages. 

It was provided by [Johnson et al. (2020)](https://www.nature.com/articles/s41586-020-2281-1) and [Illari et al. (2022)](https://www.science.org/doi/10.1126/sciadv.abo8017) in two versions. The former contains two snapshots in February 2019 and October 2019 (before the COVID-19), and the latter contains another two snapshots in November 2019 and December 2020 (at the initial stage of the COVID-19). 
Both of them are openly available and documented in two papers separately of different formats (PDF & Excel), thus requiring intensive preprocessing. 

To make it easier for other researchers to use this dataset, here we reorganize both versions of this dataset in gpickle format (can be directly imported as attributed networks using Python) and in CSV format (for general use of the dataset).

### A. Description
<img src="Main Dataset/Figures/Data_Image.png" style="width:700px;"/>

Each node represents a public Facebook page that discusses vaccination topics. It is attributed with fan size, that is, the number of members who subscribe to the Facebook page, along with the other attribute polarity including **anti-vaccination (red), pro-vaccination (blue) and neutral (green)**. Whereas its polarity remains the same for February and October snapshots, its fan size changes.
A directed edge from node A to B means page A recommends B to all its members at the page level. 
During preprocessing, we define an edge weight to quantify the significance of each recommendation. It is obtained by the product of both ends fan size. 

Some basic info about four network snapshots:
- G1 (Feb 19): 1326 nodes, 5163 edges
- G2 (Oct 19): 1326 nodes, 7484 edges
- G3 (Nov 19): 1356 nodes, 7387 edges
- G4 (Dec 20): 1356 nodes, 7154 edges -- fan count unavailable

More details are available in our paper. Note that we study the first two snapshots in our main paper and present some results about the remaining two snapshots in Supplementary Info. 

### B. Usage via Python
Dataset import using Python is required to install package [NetworkX](https://networkx.org/). Details about using this dataset are available in our Jupyter notebooks. For convenience, we briefly mention some instructions here:

```python
import networkx as nx

G1 = nx.read_gpickle("Main Dataset/Data/Graphs/G1.gpickle")           # Feb 19 network
G2 = nx.read_gpickle("Main Dataset/Data/Graphs/G2.gpickle")           # Oct 19 network
G3 = nx.read_gpickle("Follow-up Dataset (SI)/Data/Graphs/G1.gpickle") # Nov 19 network
G4 = nx.read_gpickle("Follow-up Dataset (SI)/Data/Graphs/G2.gpickle") # Dec 20 network
```

<br/>

## Programming Resources
### A. Method Implementation
- **Bow-tie Detection**: https://github.com/alan-turing-institute/directedCorePeripheryPaper
- **Community Detection - Infomap**: [infomap](https://github.com/mapequation/infomap)
- **Newman's Directed Configuration Model**: [NetworkX](https://networkx.org/documentation/stable/reference/generated/networkx.generators.degree_seq.directed_configuration_model.html) 
- **Mutual Information (MI), Logistic Regression, Support Vector Regression (SVR), and Random Forest Regression (RFR)**: [sklearn](https://scikit-learn.org/stable/)
- **Feature Selection - Sequential Floating Forward Selection (SFFS)**: [mlxtend](https://rasbt.github.io/mlxtend/)

### B. Network Visualization
See my [homepage](https://github.com/YuetingH) for details.

### C. Analysis Techniques
- **Sankey Diagram**:  [pySankey](https://github.com/Pierre-Sassoulas/pySankey)
- **Violinplot**: [seaborn](https://seaborn.pydata.org/generated/seaborn.violinplot.html)
- **Ternary Plot**: [plotly](https://plotly.com/python/ternary-plots/)

<br/>

## Repo Structure
```bash
BT_Vaccination_Views
¦   README.md   
¦
+--- Main Dataset   
¦   ¦   1_Data_Preprocessing.ipynb                  # Data preprocessing and reorganizing
¦   ¦   2_Basic_Observations.ipynb                  # Figure 2 in the paper
¦   ¦   2_Results_BT_Decomposition.ipynb            # Figure 3 
¦   ¦   4_Results_ML.ipynb                          # Table 1 & 2
¦   ¦   5_Results_SIR.ipynb                         # Figure 4 & 5
¦   ¦   6_Results_SIR_SI.ipynb                      # SI (SIR robustness check)
¦   ¦
¦   +--- Data           
¦   ¦   ¦   Vaccination_data.xlsx                   # EXCEL version (converted from PDF in Johnson et al.)
¦   ¦   ¦   
¦   ¦   +--- Graphs
¦   ¦        ¦  G1.gpickle                          # Python readable graph (Feb 19)
¦   ¦        ¦  G1_bt.gpickle                       # Python readable graph with bt results
¦   ¦        ¦  G1_nodes.csv                        # CSV for general use of the dataset
¦   ¦        ¦  G1_edges.csv                        # CSV for general use of the dataset
¦   ¦        ¦  G2.gpickle                          # Python readable graph (Oct 19)
¦   ¦        ¦  G2_bt.gpickle
¦   ¦        ¦  G2_nodes.csv
¦   ¦        ¦  G2_edges.csv
¦   ¦
¦   +--- Figures
¦   ¦   ¦   ...
¦   ¦  
¦   +--- Modules                                    
¦   ¦   ¦   ...
¦   ¦
¦   +--- Results                                    # Store some time-consuming results (e.g., SFFS, SIR)
¦       ¦   ...
¦   
+--- Follow-up Dataset (SI)                        
¦   ¦   1_Data_Preprocessing.ipynb                 
¦   ¦   2_Results_BT_Decomposition.ipynb          
¦   ¦
¦   +--- Data           
¦   ¦   ¦   Edges at Nov 2019 for Fig.2(c).xlsx     # Original dataset from Illari et al (Nov 19)
¦   ¦   ¦   Edges at Dec 2020 for Fig.2(d).xlsx     # Original dataset from Illari et al (Dec 20)
¦   ¦   ¦   Nodes.xlsx
¦   ¦   ¦   
¦   ¦   +--- Graphs                                 # All formats remain consistant with the main dataset folder
¦   ¦        ¦  G1.gpickle                          
¦   ¦        ¦  G1_bt.gpickle
¦   ¦        ¦  G1_nodes.csv
¦   ¦        ¦  G1_edges.csv
¦   ¦        ¦  G2.gpickle
¦   ¦        ¦  G2_bt.gpickle
¦   ¦        ¦  G2_nodes.csv
¦   ¦        ¦  G2_edges.csv 
¦   ¦
¦   +--- Figures
¦   ¦   ¦   ...
¦   ¦  
¦   +--- Modules
¦   ¦   ¦   ...
             
```




