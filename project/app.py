# Import dependencies
from cProfile import label
from csv import reader
import pathlib
# from turtle import color
from matplotlib import pyplot as plt
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
import os


from helper_functions.csv_to_graph import csv_to_graph
# Read dataset
# from new import G, careers_list
G = nx.Graph(label=True)
net = Network(width='100vw', height='100vh')
sources = []    
targets = []
list_of_tuples = []
careers_list = []
G , careers_list = csv_to_graph(os.path.dirname(os.path.abspath('csv_files')))


st.title("STUDY GUIDE MAP FOR SELF-TAUGHT TECHIES")
# nx.star_graph(G)
selected_career = st.multiselect('Select Career to visualize', careers_list)
careers_graph = Network(directed=True, height='100vh', width='100vw')
if len(selected_career) == 1:
    new_graph = nx.DiGraph()
    for i in G.edges:
        if G.edges[list(i)]['name'] in selected_career:
            new_graph.add_edge(*i)
    careers_graph.from_nx(new_graph)
            
elif len(selected_career) > 1:
    st.text("Please choose 1 career path or clear selection to see the full network")


else:
    careers_graph.from_nx(G, default_node_size=50, default_edge_weight=10)
# careers_graph.show_buttons()
careers_graph.set_options('''{"nodes":
 {"font": {"size": 25 }},
 "edges": {"color": {"inherit": true},
 "smooth": false},"interaction": {"navigationButtons": true },
 "physics": {
 "minVelocity": 0.75, 
 "node_distance": "1000"
  }}''')


# Save and read graph as HTML file (on Streamlit Sharing)
try:
    path = '/tmp'
    careers_graph.save_graph(f'{path}/course_graph.html')
    HtmlFile = open(f'{path}/course_graph.html', 'r', encoding='utf-8')

# Save and read graph as HTML file (locally)
except:
    path = 'html_files'
    careers_graph.save_graph(f'{path}/course_graph.html')
    HtmlFile = open(f'{path}/course_graph.html', 'r', encoding='utf-8')

# Load HTML file in HTML component for display on Streamlit page
components.html(HtmlFile.read(), height=750)
# Footer
st.markdown(
    """
    <br>
    <h6><a href="https://github.com/MillicentMalinga/DSA_Summative" target="_blank">PUBLIC REPO</a></h6>
    <h6><a href="htt/h5>ps://.medium.com" target="_blank">Medium article</a></h6>
    <h5>Created by:</h5>
    <ul>
    <li>Millicent Malinga</li>
    <li>Ntutu Sekonyela</li>
    <li>Sarah Sunday Moses</li>
    <h6>Disclaimer: The data contained here is from research done by students. The path could change according to what you want.</h6>
    """, unsafe_allow_html=True
    )
