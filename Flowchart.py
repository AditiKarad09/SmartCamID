from graphviz import Digraph

# Create a vertical directed graph
diagram = Digraph('SmartCamID', format='png')
diagram.attr(rankdir='TB', size='5,7')  # Top-to-Bottom layout

# Nodes
diagram.node('Input', 'Camera Input\n(Laptop & iPhone)', shape='ellipse', style='filled', color='lightblue')
diagram.node('Capture', 'Feed Capture\n(Real-Time Video)', shape='box', style='filled', color='lightgreen')
diagram.node('Encryption', 'Metadata Encryption\n(Source Identification)', shape='box', style='filled', color='lightyellow')
diagram.node('Overlay', 'Metadata Overlay\non Video Frames', shape='box', style='filled', color='lightpink')
diagram.node('Output', 'Streaming Output\n(OBS Studio)', shape='ellipse', style='filled', color='lightcoral')

# Arrows
diagram.edge('Input', 'Capture', label='Multi-Camera Setup')
diagram.edge('Capture', 'Encryption', label='Process Live Feed')
diagram.edge('Encryption', 'Overlay', label='Embed Metadata')
diagram.edge('Overlay', 'Output', label='Stream to Platforms')

# Save and render
diagram.render('SmartCamID__Methodology', view=True)
