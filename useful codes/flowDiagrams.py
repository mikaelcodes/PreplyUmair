from graphviz import Digraph

dot = Digraph()

# Add nodes
dot.node('A', 'Mikael wakes up')

dot.node('B', 'Mikael goes to the bathroom')
dot.node('C', 'Mikael goes to the kitchen')
dot.node('D', 'Mikael goes to the living room')
dot.node('E', 'Mikael goes to the balcony')
dot.node('F', 'Mikael goes to the sleeping room')





# Save and render the graph
dot.render('graph', format='png', view=True)