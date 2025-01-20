from graphviz import Digraph

# Create a new Digraph
dot = Digraph(comment='Career Choices')

# Add nodes for career choices
dot.node('Career_Choices', 'Career Choices')

# Add subgraphs for each semester
for semester in range(1, 5):
    with dot.subgraph(name=f'cluster_{semester}') as subgraph:
        subgraph.attr(label=f'Semester {semester}')
        subgraph.node(f'Semester_{semester}', f'Semester {semester}')

        # Add courses for each semester
        for i in range(1, 5):
            course = f'Course_{semester}_{i}'
            subgraph.node(course, f'Course {semester}-{i}')
            subgraph.edge(f'Semester_{semester}', course)

# Render the graph to a file
dot.render('career_choices_graph', format='png', cleanup=True)

print("Graph generated as 'career_choices_graph.png'")