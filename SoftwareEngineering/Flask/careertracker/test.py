import pygraphviz as pgv
from io import BytesIO
def generate_tree(program_type):
    # Create a sample tree diagram (replace with your logic)
    graph = pgv.AGraph(directed=True)
    graph.add_node(program_type)
    graph.add_edge(program_type, "Prerequisite 1")
    graph.add_edge(program_type, "Prerequisite 2")
    graph.add_edge(program_type, "Elective 1")
    graph.add_edge(program_type, "Elective 2")

    # Render the graph to an image
    tree_image = BytesIO()
    graph.draw(tree_image, format="png", prog="dot")
    #tree_image.seek(0)


    #return tree_image
    return  print(graph)

generate_tree("Computer Science")