#use pyinstaller to make exe

from graphviz import Digraph

dot = Digraph()
dot.node('A', 'A')
dot.node('B', 'B')
dot.node('C', 'C')
dot.edge('A', 'B')
dot.edge('A', 'C')

dot.render('binary_tree.gv', view=True)
